#include <Python.h>
#include <dirent.h>
#include <string>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include "PyEngine.h"
#include "Item.h"
#include "Room.h"

// Singleton instance is null until referenced first time
PyEngine* PyEngine::instance = 0;

/*
    PyEngine is a singleton and can only be accessed through this function
*/
PyEngine* PyEngine::getInstance()
{
    if (instance == 0)
    {
        instance = new PyEngine();
        instance->inventory = new std::vector<Item*>();
        instance->verbs = new std::unordered_map<std::string, std::unordered_set<std::string>*>();
        instance->duplicateItem = new Item(NULL, false, true);
        instance->LoadPyFiles("Content");
        std::remove("err.txt");
    }
    return instance;
}

/*
    Run 1 line of Python code
    Return false if an error occurred
*/
bool PyEngine::debugConsole(std::string command)
{
    PyRun_SimpleString((char*)"import sys\nsys.stderr = open('err.txt', 'a')");

    int success = PyRun_SimpleString(command.c_str());
    
    PyRun_SimpleString((char*)"import sys\nsys.stderr.close()");
    return (success == 0);
}

/*
    Returns the list of all room names in the game
*/
std::string PyEngine::debugRooms()
{
    std::string ret = "";
    auto itr = rooms.begin();
    while (itr != rooms.end()) {
        Room* room = itr->second;
        itr++;
        ret = ret + room->getName();
        ret = ret + ", ";
    }
    ret = ret.substr(0, ret.size() - 2);
    return ret;
}

/*
    Returns the list of all non-door item names in the game
*/
std::string PyEngine::debugItems()
{
    std::string ret = "";
    auto itr = items.begin();
    while (itr != items.end()) {
        Item* item = itr->second;
        itr++;
        if (!item->isDoor()) {
            ret = ret + item->getName();
            ret = ret + ", ";
        }
    }
    ret = ret.substr(0, ret.size() - 2);
    return ret;
}

/*
    Returns the list of all door names in the game
*/
std::string PyEngine::debugDoors()
{
    std::string ret = "";
    auto itr = items.begin();
    while (itr != items.end()) {
        Item* item = itr->second;
        itr++;
        if (item->isDoor()) {
            ret = ret + item->getName();
            ret = ret + ", ";
        }
    }
    ret = ret.substr(0, ret.size() - 2);
    return ret;
}

/*
    Print out the details for a room
*/
std::string PyEngine::debugRoomDetails(std::string roomName)
{
    Room* room = getRoomByName(roomName);
    if (room == NULL) {
        return "Room not found";
    }
    std::string ret = "name = " + roomName + "\n";
    PyObject* roomPyObj = room->getPyRoom();
    if (PyObject_HasAttrString(roomPyObj, (char*)"aliases")) {
        PyObject* aliases = PyObject_GetAttrString(roomPyObj, (char*)"aliases");
        ret = ret + "aliases = " + printPyObject(aliases) + "\n";
    }
    if (PyObject_HasAttrString(roomPyObj, (char*)"items")) {
        PyObject* items = PyObject_GetAttrString(roomPyObj, (char*)"items");
        ret = ret + "items = " + printPyObject(items) + "\n";
    }
    if (PyObject_HasAttrString(roomPyObj, (char*)"droppedItems")) {
        PyObject* droppedItems = PyObject_GetAttrString(roomPyObj, (char*)"droppedItems");
        ret = ret + "droppedItems = " + printPyObject(droppedItems) + "\n";
    }
    if (PyObject_HasAttrString(roomPyObj, (char*)"doors")) {
        PyObject* doors = PyObject_GetAttrString(roomPyObj, (char*)"doors");
        ret = ret + "doors = " + printPyObject(doors) + "\n";
    }
    if (PyObject_HasAttrString(roomPyObj, (char*)"properties")) {
        PyObject* properties = PyObject_GetAttrString(roomPyObj, (char*)"properties");
        ret = ret + "properties = " + printPyObject(properties) + "\n";
    }
    if (PyObject_HasAttrString(roomPyObj, (char*)"visited")) {
        PyObject* visited = PyObject_GetAttrString(roomPyObj, (char*)"visited");
        ret = ret + "visited = " + printPyObject(visited) + "\n";
    }
    if (PyObject_HasAttrString(roomPyObj, (char*)"visible")) {
        PyObject* visible = PyObject_GetAttrString(roomPyObj, (char*)"visible");
        ret = ret + "visible = " + printPyObject(visible) + "\n";
    }
    return ret;
}

/*
    Print out the details for an item or door
*/
std::string PyEngine::debugItemDetails(std::string itemName)
{
    Item* item = getItemByName(itemName);
    if (item == NULL) {
        return "Item not found";
    }
    std::string ret = "name = " + itemName + "\n";
    PyObject* itemPyObj = item->getPyItem();
    if (PyObject_HasAttrString(itemPyObj, (char*)"aliases")) {
        PyObject* aliases = PyObject_GetAttrString(itemPyObj, (char*)"aliases");
        ret = ret + "aliases = " + printPyObject(aliases) + "\n";
    }
    if (PyObject_HasAttrString(itemPyObj, (char*)"properties")) {
        PyObject* properties = PyObject_GetAttrString(itemPyObj, (char*)"properties");
        ret = ret + "properties = " + printPyObject(properties) + "\n";
    }
    if (PyObject_HasAttrString(itemPyObj, (char*)"visible")) {
        PyObject* visible = PyObject_GetAttrString(itemPyObj, (char*)"visible");
        ret = ret + "visible = " + printPyObject(visible) + "\n";
    }
    if (item->isDoor() && PyObject_HasAttrString(itemPyObj, (char*)"roomConnections")) {
        PyObject* roomConnections = PyObject_GetAttrString(itemPyObj, (char*)"roomConnections");
        ret = ret + "roomConnections = " + printPyObject(roomConnections) + "\n"; 
    }
    if (PyObject_HasAttrString(itemPyObj, (char*)"globalAccess")) {
        PyObject* globalAccess = PyObject_GetAttrString(itemPyObj, (char*)"globalAccess");
        ret = ret + "globalAccess = " + printPyObject(globalAccess) + "\n";
    }

    return ret;
}

/*
    Turn a PyObject* to the string representation
*/
std::string printPyObject(PyObject* obj)
{
    if (obj == NULL) {
        return "";
    }
    PyObject* reprObject = PyObject_Repr(obj);
    std::string ret(getStringFromPyObject(reprObject));
    return ret;
    /*if (PyUnicode_Check(returnVal)) {
        ret = getStringFromPyObject(returnVal);
    } else if (PyBool_Check(returnVal) {
        if (PyObject_IsTrue(returnVal)) {
            ret = "True";
        } else {
            ret = "False";
        }
    } else if (PyList_Check(returnVal)) {
        ret = "[";
        Py_ssize_t num = PyList_Size(returnVal);
        for (Py_ssize_t i = 0; i < num; i++) {
            PyObject* element = PyList_GetItem(returnVal, i);
            const char* elementStr = getStringFromPyObject(element);
            ret = ret + elementStr;
            if (i < num - 1) {
                ret = ret + ", ";
            }
        }
        ret = ret + "]";
    } else if (PyDict_Check(returnVal)) {

    }*/
}

/*
    Internal access - get a Room object from the Py version
*/
Room* PyEngine::getRoom(PyObject* pyRoom)
{
    const char* roomName = getStringFromPyObject(pyRoom, (char*)"name");
    return getInstance()->getRoomByName(roomName);
}

/*
    Internal access - get an Item object from the Py version
*/
Item* PyEngine::getItem(PyObject* pyItem)
{
    const char* itemName = getStringFromPyObject(pyItem, (char*)"name");
    return getInstance()->getItemByName(itemName);
}

/*
    C++ API to get game score
*/
long PyEngine::getScore()
{
    return score;
}

/*
    C++ API to set game score
*/
void PyEngine::setScore(long newScore)
{
    score = newScore;
}

/*
    Python API to get game score
*/
PyObject* PyEngine::emb_getScore(PyObject *self, PyObject *args)
{
    return PyLong_FromLong(getInstance()->score);
}

/*
    Python API to set game score
*/
PyObject* PyEngine::emb_setScore(PyObject *self, PyObject *args)
{
    PyObject* newScore;
    PyArg_UnpackTuple(args, "", 1, 1, &newScore);
    getInstance()->score = PyLong_AsLong(newScore);
    return Py_BuildValue("");
}

/*
    Win the game - Python API only
    Prints out a message that includes the score
    Game will accept no more input after victory
*/
PyObject* PyEngine::emb_winGame(PyObject *self, PyObject *args)
{
    // This function is mostly a placeholder
    printf((char*)"Congratulations!\nFinal score: %ld\n", getInstance()->getScore());
    return Py_BuildValue("");
}

/*
    Lose the game - Python API only
    Loss actions yet to be determined. It might give the player another chance
*/
PyObject* PyEngine::emb_loseGame(PyObject *self, PyObject *args)
{
    printf((char*)"You lose!\n");
    return Py_BuildValue("");
}

/*
    Python API - add an item to the engine
*/
PyObject* PyEngine::emb_setupItem(PyObject *self, PyObject *args)
{
    PyObject* pyitem;
    Item* item = NULL;
    PyArg_UnpackTuple(args, "", 1, 1, &pyitem);
    Py_INCREF(pyitem);
    const char* itemName = getStringFromPyObject(pyitem, (char*)"name");
    if (strlen(itemName) > 0) {
        item = new Item(pyitem, false, false);
        PyEngine::getInstance()->items.insert(std::pair<std::string, Item*>(itemName, item));
    } else {
        assertThat(false, "Item must implement \"name\" attribute");
    }

    // Check for "look" function
    assertThat(item->hasVerb("look", false), "Item must implement \"look\" function!");

    // Check for aliases. Initialize to empty list if not found
    if (!PyObject_HasAttrString(pyitem, (char*)"aliases")) {
        PyObject* newAliasesList = PyList_New(0);
        PyObject_SetAttrString(pyitem, (char*)"aliases", newAliasesList);
    } else {
        PyObject* aliasesList = PyObject_GetAttrString(pyitem, (char*)"aliases");
        assertThat(PyList_Check(aliasesList), "Item attribute \"aliases\" must be a list!");
    }

    // Check for properties. Initialize to empty dictionary if not found
    if (!PyObject_HasAttrString(pyitem, (char*)"properties")) {
        PyObject* newPropertiesDict = PyDict_New();
        PyObject_SetAttrString(pyitem, (char*)"properties", newPropertiesDict);
    } else {
        PyObject* propertiesDict = PyObject_GetAttrString(pyitem, (char*)"properties");
        assertThat(PyDict_Check(propertiesDict), "Item attribute \"properties\" must be a dictionary!");
    }

    // Check for visible. Set to True if not found
    if (!PyObject_HasAttrString(pyitem, (char*)"visible")) {
        PyObject_SetAttrString(pyitem, (char*)"visible", Py_True);
    } else {
        PyObject* visibleFlag = PyObject_GetAttrString(pyitem, (char*)"visible");
        assertThat(PyBool_Check(visibleFlag), "Item attribute \"visible\" must be a boolean!");
    }

    // Check for global. Set to False if not found
    if (!PyObject_HasAttrString(pyitem, (char*)"globalAccess")) {
        PyObject_SetAttrString(pyitem, (char*)"globalAccess", Py_False);
    } else {
        PyObject* globalFlag = PyObject_GetAttrString(pyitem, (char*)"globalAccess");
        assertThat(PyBool_Check(globalFlag), "Item attribute \"globalAccess\" must be a boolean!");
    }

    PyObject* initialItem = copyObject(pyitem);
    getInstance()->initialItems.insert(std::pair<std::string, PyObject*>(itemName, initialItem));

    return Py_BuildValue("");
}

/*
    Python API - get an item by "name" property
*/
PyObject* PyEngine::emb_getItemByName(PyObject *self, PyObject *args)
{
    PyEngine* instance = PyEngine::getInstance();
    PyObject* itemName;
    PyArg_UnpackTuple(args, "", 1, 1, &itemName);
    const char* itemNamestr = getStringFromPyObject(itemName);
    Item* item = instance->getItemByName(itemNamestr);
    return item->getPyItem();
}

/*
    Python API - add a room to the engine
*/
PyObject* PyEngine::emb_setupRoom(PyObject *self, PyObject *args)
{
    PyObject* pyroom;
    PyArg_UnpackTuple(args, "", 1, 1, &pyroom);
    Py_INCREF(pyroom);
    const char* name = getStringFromPyObject(pyroom, (char*)"name");
    if (strlen(name) > 0) {
        Room* room = new Room(pyroom);
        getInstance()->rooms.insert(std::pair<std::string, Room*>(name, room));
    } else {
        assertThat(false, "Room must implement \"name\" attribute!");
    }

    // Check for "enterRoom" function
    PyObject* enterRoomFunction = PyObject_GetAttrString(pyroom, (char*)"enterRoom");
    if (!PyCallable_Check(enterRoomFunction)) {
        assertThat(PyCallable_Check(enterRoomFunction), "Room must implement \"enterRoom\" function!");
    }

    // Check for "look" function
    PyObject* lookFunction = PyObject_GetAttrString(pyroom, (char*)"look");
    if (!PyCallable_Check(lookFunction)) {
        assertThat(PyCallable_Check(lookFunction), "Room must implement \"look\" function!");
    }

    // Check for aliases. Initialize to empty list if not found
    if (!PyObject_HasAttrString(pyroom, (char*)"aliases")) {
        PyObject* newAliasesList = PyList_New(0);
        PyObject_SetAttrString(pyroom, (char*)"aliases", newAliasesList);
    } else {
        PyObject* aliasesList = PyObject_GetAttrString(pyroom, (char*)"aliases");
        assertThat(PyList_Check(aliasesList), "Room attribute \"aliases\" must be a list!");
    }

    // Check for properties. Initialize to empty dictionary if not found
    if (!PyObject_HasAttrString(pyroom, (char*)"properties")) {
        PyObject* newPropertiesDict = PyDict_New();
        PyObject_SetAttrString(pyroom, (char*)"properties", newPropertiesDict);
    } else {
        PyObject* propertiesDict = PyObject_GetAttrString(pyroom, (char*)"properties");
        assertThat(PyDict_Check(propertiesDict), "Room attribute \"properties\" must be a dictionary!");
    }

    // Check for items. Initialize to empty list if not found
    if (!PyObject_HasAttrString(pyroom, (char*)"items")) {
        PyObject* newItemsList = PyList_New(0);
        PyObject_SetAttrString(pyroom, (char*)"items", newItemsList);
    } else {
        PyObject* itemsList = PyObject_GetAttrString(pyroom, (char*)"items");
        assertThat(PyList_Check(itemsList), "Room attribute \"items\" must be a list!");
    }

    // Check for doors. Initialize to empty dictionary if not found
    if (!PyObject_HasAttrString(pyroom, (char*)"doors")) {
        PyObject* newDoorsDict = PyDict_New();
        PyObject_SetAttrString(pyroom, (char*)"doors", newDoorsDict);
    } else {
        PyObject* doorsDict = PyObject_GetAttrString(pyroom, (char*)"doors");
        assertThat(PyDict_Check(doorsDict), "Room attribute \"doors\" must be a dictionary!");
    }

    // Check for visible. Set to False if not found
    if (!PyObject_HasAttrString(pyroom, (char*)"visible")) {
        PyObject_SetAttrString(pyroom, (char*)"visible", Py_False);
    } else {
        PyObject* visibleFlag = PyObject_GetAttrString(pyroom, (char*)"visible");
        assertThat(PyBool_Check(visibleFlag), "Room attribute \"visible\" must be a boolean!");
    }

    // Check for visited. Set to false if not found
    if (!PyObject_HasAttrString(pyroom, (char*)"visited")) {
        PyObject_SetAttrString(pyroom, (char*)"visited", Py_False);
    } else {
        PyObject* visitedFlag = PyObject_GetAttrString(pyroom, (char*)"visited");
        assertThat(PyBool_Check(visitedFlag), "Room attribute \"visited\" must be a boolean!");
    }

    // Add an array for items dropped in a room
    if (!PyObject_HasAttrString(pyroom, (char*)"droppedItems")) {
        PyObject* newDroppedItemsList = PyList_New(0);
        PyObject_SetAttrString(pyroom, (char*)"droppedItems", newDroppedItemsList);
    } else {
        PyObject* droppedItemsList = PyObject_GetAttrString(pyroom, (char*)"droppedItems");
        assertThat(PyList_Check(droppedItemsList), "Room attribute \"droppedItems\" must be a list!");
    }

    PyObject* initialRoom = copyObject(pyroom);
    getInstance()->initialRooms.insert(std::pair<std::string, PyObject*>(name, initialRoom));

    return Py_BuildValue("");
}

/*
    Python API - get a room by "name" property
*/
PyObject* PyEngine::emb_getRoomByName(PyObject *self, PyObject *args)
{
    PyObject* roomName;
    PyArg_UnpackTuple(args, "", 1, 1, &roomName);
    const char* roomNamestr = getStringFromPyObject(roomName);
    Room* room = getInstance()->getRoomByName(roomNamestr);
    return room->getPyRoom();
}

/*
    Python API - get the room the player is currently standing in
*/
PyObject* PyEngine::emb_getCurrentRoom(PyObject *self, PyObject *args)
{
    return getInstance()->getCurrentRoom()->getPyRoom();
}

/*
    Python API - move player to a different room. Always succeeds
*/
PyObject* PyEngine::emb_goToRoom(PyObject *self, PyObject *args)
{
    PyObject *pyroom;
    PyArg_UnpackTuple(args, "", 1, 1, &pyroom);
    Room* room = getInstance()->getRoom(pyroom);
    if (room != NULL)
    {
        getInstance()->currentRoom = room;
        PyObject* returnedString = room->callEnter();
        room->setVisited();
        return returnedString;
    }
    return Py_BuildValue("");
}

/*
    Python API - add item to player inventory
*/
PyObject* PyEngine::emb_addToInventory(PyObject* self, PyObject *args)
{
    PyObject* pyitem;
    PyArg_UnpackTuple(args, "", 1, 1, &pyitem);
    Item* item = getInstance()->getItem(pyitem);
    if (item != NULL)
    {
        std::vector<Item*>* inventory = getInstance()->inventory;
        inventory->push_back(item);

        // Remove from current room
        Room* currentRoom = getInstance()->getCurrentRoom();
        std::vector<Item*> droppedItems = currentRoom->getDroppedItems();
        std::vector<Item*> items = currentRoom->getItems();
        if (std::find(droppedItems.begin(), droppedItems.end(), item) != droppedItems.end()) {
            // remove from droppedItems
            PyObject* pyRoom = currentRoom->getPyRoom();
            PyObject* itemList = PyObject_GetAttrString(pyRoom, (char*)"droppedItems");
            assertThat(PyList_Check(itemList), "Error! droppedItems must be a list of item names!");
            
            std::vector<Item*> items;

            Py_ssize_t size = PyList_Size(itemList);
            for (Py_ssize_t i = 0; i < size; i++) {
                PyObject* itemName = PyList_GetItem(itemList, i);
                const char* itemNameStr = getStringFromPyObject(itemName);
                Item* checkItem = PyEngine::getInstance()->getItemByName(itemNameStr);
                assertThat((checkItem != NULL), "Error! Item in room not found");
                if (item == checkItem) {
                    // Remove this item
                    PyObject_DelItem(itemList, PyLong_FromLong(i));
                    break;
                }
            }
        } else if (std::find(items.begin(), items.end(), item) != items.end()) {
            // remove from items
            PyObject* pyRoom = currentRoom->getPyRoom();
            PyObject* itemList = PyObject_GetAttrString(pyRoom, (char*)"items");
            assertThat(PyList_Check(itemList), "Error! items must be a list of item names!");
            
            std::vector<Item*> items;

            Py_ssize_t size = PyList_Size(itemList);
            for (Py_ssize_t i = 0; i < size; i++) {
                PyObject* itemName = PyList_GetItem(itemList, i);
                const char* itemNameStr = getStringFromPyObject(itemName);
                Item* checkItem = PyEngine::getInstance()->getItemByName(itemNameStr);
                assertThat((checkItem != NULL), "Error! Item in room not found");
                if (item == checkItem) {
                    // Remove this item
                    PyObject_DelItem(itemList, PyLong_FromLong(i));
                    break;
                }
            }
        }
    }
    return Py_BuildValue("");
}

/*
    Python API - remove item from player inventory
*/
PyObject* PyEngine::emb_removeFromInventory(PyObject *self, PyObject *args)
{
    PyObject* pyitem;
    PyArg_UnpackTuple(args, "", 1, 1, &pyitem);
    Item* item = getInstance()->getItem(pyitem);
    if (item != NULL && getInstance()->inInventory(item))
    {
        std::vector<Item*>* inventory = getInstance()->inventory;
        std::vector<Item*>::iterator itr = std::find(inventory->begin(), inventory->end(), item);
        if (itr != inventory->end()) 
        {
            inventory->erase(itr);
        }
    }
    return Py_BuildValue("");
}

/*
    Python API - return true if item is in inventory
*/
PyObject* PyEngine::emb_inInventory(PyObject *self, PyObject *args)
{
    PyObject* pyitem;
    PyArg_UnpackTuple(args, "", 1, 1, &pyitem);
    Item* item = getInstance()->getItem(pyitem);
    if (item != NULL)
    {
        if (getInstance()->inInventory(item))
        {
            Py_RETURN_TRUE;
        }
    } 
    Py_RETURN_FALSE;
}

/*
    Python API - remove an item from the inventory and add it as a dropped item in the current room
*/
PyObject* PyEngine::emb_dropItem(PyObject *self, PyObject *args)
{
    PyObject* pyitem;
    PyArg_UnpackTuple(args, "", 1, 1, &pyitem);
    Item* item = getInstance()->getItem(pyitem);
    if (item != NULL)
    {
        // Remove from inventory if in inventory
        if (emb_inInventory(self, args)) {
            emb_removeFromInventory(self, args);
        }
        // Add to current room's droppedItems
        Room* currentRoom = getInstance()->getCurrentRoom();
        PyObject* pyroom = currentRoom->getPyRoom();
        PyObject* droppedItemsList = PyObject_GetAttrString(pyroom, (char*)"droppedItems");
        const char* itemName = item->getName().c_str();
        PyObject* pyItemName = PyUnicode_FromString(itemName);
        PyList_Append(droppedItemsList, pyItemName);
    }
    return Py_BuildValue("");
}

/*
    Setup a new instance of a door item
*/
PyObject* PyEngine::emb_setupDoor(PyObject *self, PyObject *args)
{
    PyObject* pyitem;
    Item* item = NULL;
    PyArg_UnpackTuple(args, "", 1, 1, &pyitem);
    Py_INCREF(pyitem);
    const char* doorName = getStringFromPyObject(pyitem, (char*)"name");
    if (strlen(doorName) > 0) {
        item = new Item(pyitem, true, false);
        PyEngine::getInstance()->items.insert(std::pair<std::string, Item*>(doorName, item));
    } else {
        assertThat(false, "Door must implement \"name\" attribute");
    }

    // Check for "look" function
    assertThat(item->hasVerb("look", false), "Door must implement \"look\" function!");
    
    // Check for "go" function
    assertThat(item->hasVerb("go", false), "Door must implement \"go\" function!");

    // Check for aliases. Initialize to empty list if not found
    if (!PyObject_HasAttrString(pyitem, (char*)"aliases")) {
        PyObject* newAliasesList = PyList_New(0);
        PyObject_SetAttrString(pyitem, (char*)"aliases", newAliasesList);
    } else {
        PyObject* aliasesList = PyObject_GetAttrString(pyitem, (char*)"aliases");
        assertThat(PyList_Check(aliasesList), "Door attribute \"aliases\" must be a list!");
    }

    // Check for properties. Initialize to empty dictionary if not found
    if (!PyObject_HasAttrString(pyitem, (char*)"properties")) {
        PyObject* newPropertiesDict = PyDict_New();
        PyObject_SetAttrString(pyitem, (char*)"properties", newPropertiesDict);
    } else {
        PyObject* propertiesDict = PyObject_GetAttrString(pyitem, (char*)"properties");
        assertThat(PyDict_Check(propertiesDict), "Door attribute \"properties\" must be a dictionary!");
    }

    // Check for visible. Set to True if not found
    if (!PyObject_HasAttrString(pyitem, (char*)"visible")) {
        PyObject_SetAttrString(pyitem, (char*)"visible", Py_True);
    } else {
        PyObject* visibleFlag = PyObject_GetAttrString(pyitem, (char*)"visible");
        assertThat(PyBool_Check(visibleFlag), "Door attribute \"visible\" must be a boolean!");
    }

    // Check for roomConnections
    assertThat(PyObject_HasAttrString(pyitem, (char*)"roomConnections"), "Door must implement \"roomConnections\" dictionary!");
    PyObject* roomConnectionsDict = PyObject_GetAttrString(pyitem, (char*)"roomConnections");
    assertThat(PyDict_Check(roomConnectionsDict), "Door attribute \"roomConnections\" must be a dictionary!");

    PyObject* initialItem = copyObject(pyitem);
    getInstance()->initialItems.insert(std::pair<std::string, PyObject*>(doorName, initialItem));

    return Py_BuildValue("");
}

/*
    Setup verbs and synonyms
*/
PyObject* PyEngine::emb_setVerbs(PyObject *self, PyObject *args)
{
    PyEngine* eng = PyEngine::getInstance();
    PyObject* verbDictionary;
    PyArg_UnpackTuple(args, "", 1, 1, &verbDictionary);
    if (PyDict_Check(verbDictionary))
    {
        PyObject* keyList = PyDict_Keys(verbDictionary);
        Py_ssize_t numVerbs = PyList_Size(keyList);
        for (Py_ssize_t i = 0; i < numVerbs; i++)
        {
            PyObject* verb = PyList_GetItem(keyList, i);
            const char* verbString = getStringFromPyObject(verb);
            auto verbItr = eng->verbs->find(verbString);
            if (verbItr == eng->verbs->end())
            {
                // Add it to the set
                std::unordered_set<std::string>* newSet = new std::unordered_set<std::string>();
                newSet->insert(verbString);
                eng->verbs->insert({verbString, newSet});
                verbItr = eng->verbs->find(verbString);
            }
            std::unordered_set<std::string>* synonymSet = verbItr->second;
            PyObject* synonyms = PyDict_GetItem(verbDictionary, verb);
            Py_ssize_t numSynonyms = PySet_Size(synonyms);
            for (Py_ssize_t j = 0; j < numSynonyms; j++)
            {
                PyObject* synonym =  PySet_Pop(synonyms);
                const char* synonymString = getStringFromPyObject(synonym);
                std::string newstr(strdup(synonymString));
                synonymSet->insert(newstr);
            }
        }
    }
    return Py_BuildValue("");
}

/*
    Collection of Python APIs
*/
PyMethodDef PyEngine::EmbMethods[] = 
{
    {"getScore", emb_getScore, METH_VARARGS, ""},
    {"setScore", emb_setScore, METH_VARARGS, ""},
    {"setupItem", emb_setupItem, METH_VARARGS, ""},
    {"getItemByName", emb_getItemByName, METH_VARARGS, ""},
    {"winGame", emb_winGame, METH_VARARGS, ""},
    {"loseGame", emb_loseGame, METH_VARARGS, ""},
    {"setupRoom", emb_setupRoom, METH_VARARGS, ""},
    {"getRoomByName", emb_getRoomByName, METH_VARARGS, ""},
    {"getCurrentRoom", emb_getCurrentRoom, METH_VARARGS, ""},
    {"goToRoom", emb_goToRoom, METH_VARARGS, ""},
    {"addToInventory", emb_addToInventory, METH_VARARGS, ""},
    {"removeFromInventory", emb_removeFromInventory, METH_VARARGS, ""},
    {"inInventory", emb_inInventory, METH_VARARGS, ""},
    {"dropItem", emb_dropItem, METH_VARARGS, ""},
    {"setVerbs", emb_setVerbs, METH_VARARGS, ""},
    {"setupDoor", emb_setupDoor, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}
};

/*
    Definition of Python module to expose game APIs
*/
PyModuleDef PyEngine::EmbModule = 
{
    PyModuleDef_HEAD_INIT, "eng", NULL, -1, EmbMethods, NULL, NULL, NULL, NULL
};

/*
    Function to create our Python extension module
*/
PyObject* PyEngine::PyInit_emb(void)
{
    return PyModule_Create(&EmbModule);
}

/*
    Constructor (private)
    Extends Python with our game API and initializes engine
*/
PyEngine::PyEngine()
{
    PyImport_AppendInittab("eng", &PyInit_emb);
    Py_Initialize();
}

/*
    Destructor
    Not even sure if this is needed. It would only be called when the game closes
*/
PyEngine::~PyEngine()
{
    Py_Finalize();
}

/*
    Load Python files in the given directory and all subdirectories
*/
void PyEngine::LoadPyFiles(std::string directoryName)
{
    DIR* contentDir = opendir(directoryName.c_str());
    struct dirent* dp;
    while ((dp = readdir(contentDir)) != NULL) {
        if (strcmp(dp->d_name, ".") != 0 && strcmp(dp->d_name, "..") != 0) {
            if (dp->d_type == DT_DIR) LoadPyFiles(directoryName + "/" + dp->d_name);
            else {
                // Load py file
                FILE* fp;
                std::string filename = directoryName + "/" + dp->d_name;
                if (filename.size() >= 3 && filename.compare(filename.size() - 3, 3, ".py") == 0) {
                    fp = _Py_fopen(filename.c_str(), "r");
                    if (fp != NULL) {
                        currentFile = strdup(filename.c_str());
                        printf("Reading file: %s\n", currentFile);
                        fflush(stdout);
                        int failure = PyRun_SimpleFile(fp, filename.c_str());
                        if (failure) {
                            printf("^^^Error in file!^^^\n\n");
                        }
                    } else {
                        fprintf(stderr, "Could not open file \n");
                    }       
                }
            }
        }
    }
    currentFile = (char*)"?";
    closedir(contentDir);
    //printf("Done reading files\n");
    //fflush(stdout);
}

/*
    Get item by "name" property
*/
Item* PyEngine::getItemByName(std::string itemName)
{
    Item* item = NULL;
    std::map<std::string, Item*>::iterator itr = items.find(itemName);
    if (itr != items.end()) 
    {
        item = itr->second;
        Py_INCREF(item->getPyItem());
    }
    return item;
}

/*
    Get room by "name" property
*/
Room* PyEngine::getRoomByName(std::string roomName)
{
    Room* room = NULL;
    std::map<std::string, Room*>::iterator itr = rooms.find(roomName);
    if (itr != rooms.end())
    {
        room = itr->second;
        Py_INCREF(room->getPyRoom());
    }
    return room;
}

/*
    Get the room the player is currently in
*/
Room* PyEngine::getCurrentRoom()
{
    return currentRoom;
}

/*
    Put player in new room
*/
void PyEngine::goToRoom(Room* room)
{
    currentRoom = room;
    room->callEnter();
}

/*
    Check if item is in inventory
*/
bool PyEngine::inInventory(Item* item)
{
    return (std::find(inventory->begin(), inventory->end(), item) != inventory->end());
}

/*
    Get the whole inventory as a vector Items. Items can be added or removed
*/
std::vector<Item*>* PyEngine::getInventory()
{
    return inventory;
}

/*
    Get the collection of globally accessible items
*/
std::vector<Item*> PyEngine::getGlobalItems()
{
    std::vector<Item*> globals;

    auto itr = items.begin();
    while (itr != items.end()) {
        Item* item = itr->second;
        if (!item->isDoor() && item->isGlobal()) {
            globals.push_back(item);
        }
        itr++;
    }

    return globals;
}

/*
    Get an item by name. Only returns items that are in current room, in inventory,
    or globally accessible. Also gives you an item if the itemName matches an item alias.
    Items must have their "visible" attribute set to True.

    Gives a door item if the input is a direction and matches one in the Room's "doors" attribute
    Gives a door item if the input is a room name or alias and a door connects the current room to that room 
        (only if the room's "visible" attribute is also set to true or the player has been there before)
*/
Item* PyEngine::getAccessibleItem(std::string itemName)
{
    Item* item = NULL;
    itemName = lowercase(itemName);

    // Check items in room
    std::vector<Item*> itemsInRoom = getCurrentRoom()->getItems();
    for (uint i = 0; i < itemsInRoom.size(); i++)
    {
        Item* testItem = itemsInRoom[i];
        if (testItem->isVisible()) {
            if (lowercase(testItem->getName()).compare(itemName) == 0 || testItem->hasAlias(itemName))
            {
                if (item == NULL) {
                    item = testItem;
                } else if (item != testItem) {
                    item = duplicateItem;
                }
            }
        }
    }

    // Check inventory
    std::vector<Item*> itemsInInventory = *getInventory();
    for (uint i = 0; i < itemsInInventory.size(); i++)
    {
        Item* testItem = itemsInInventory[i];
        if (testItem->isVisible()) {
            if (lowercase(testItem->getName()).compare(itemName) == 0 || testItem->hasAlias(itemName))
            {
                if (item == NULL) {
                    item = testItem;
                } else if (item != testItem) {
                    item = duplicateItem;
                }            
            }
        }
    }

    // Check global
    std::vector<Item*> globalItems = getGlobalItems();
    for (uint i = 0; i < globalItems.size(); i++)
    {
        Item* testItem = globalItems[i];
        if (testItem->isVisible()) {
            if (lowercase(testItem->getName()).compare(itemName) == 0 || testItem->hasAlias(itemName))
            {
                if (item == NULL) {
                    item = testItem;
                } else if (item != testItem) {
                    item = duplicateItem;
                }            
            }
        }
    }

    // Check doors
    std::vector<Item*> doors = getCurrentRoom()->getDoors();
    for (uint i = 0; i < doors.size(); i++)
    {
        Item* testItem = doors[i];
        if (testItem->isVisible()) {
            if (lowercase(testItem->getName()).compare(itemName) == 0 || testItem->hasAlias(itemName))
            {
                if (item == NULL) {
                    item = testItem;
                } else if (item != testItem) {
                    item = duplicateItem;
                }            
            }
        }
    }

    // Check direction or room
    Item* door = getDoorTo(itemName);
    if (door != NULL && door->isVisible())
    {
        if (item == NULL) {
            item = door;
        } else if (item != door) {
            item = duplicateItem;
        }
    }

    // Check current room
    Room* currentRoom = getCurrentRoom();
    if (lowercase(currentRoom->getName()).compare(itemName) == 0 || currentRoom->hasAlias(itemName)) {
        Item* currentRoomItem = getItemByName("room");
        if (item == NULL) {
            item = currentRoomItem;
        } else if (item != currentRoomItem) {
            item = duplicateItem;
        }
    }


    return item;
}

/*
    Get the official version of a verb. Returns empty string if verb not defined
*/
std::string PyEngine::getVerb(std::string verb)
{
    verb = lowercase(verb);
    auto itr = verbs->begin();
    while (itr != verbs->end())
    {
        std::unordered_set<std::string>* synonyms = itr->second;
        auto synonymItr = synonyms->begin();
        while (synonymItr != synonyms->end())
        {
            std::string compareVerb(*synonymItr);
            compareVerb = lowercase(compareVerb);
            if (verb.compare(compareVerb) == 0)
            {
                return itr->first;
            }
            synonymItr++;
        }
        itr++;
    }
    return "";
}

/*
    Internal usage - Get a door item based on direction or the next room name
*/
Item* PyEngine::getDoorTo(std::string directionOrRoom)
{
    directionOrRoom = lowercase(directionOrRoom);
    PyObject* pyRoom = getCurrentRoom()->getPyRoom();
    PyObject* doorsDict = PyObject_GetAttrString(pyRoom, (char*)"doors");
    assertThat(PyDict_Check(doorsDict), "Error! doors must be a dictionary!");

    // Check if it's a valid direction
    PyObject* directionString = PyUnicode_FromString(directionOrRoom.c_str());
    if (PyDict_Contains(doorsDict, directionString)) {
        PyObject* doorName = PyDict_GetItem(doorsDict, directionString);
        const char* doorNameStr = getStringFromPyObject(doorName);
        Item* door = PyEngine::getInstance()->getItemByName(doorNameStr);
        assertThat(door != NULL, "Error! Door not found");
        return door;
    }

    Item* returnDoor = NULL;

    // Check if it's a visible connecting room
    PyObject* doorList = PyDict_Values(doorsDict);
    Py_ssize_t numDoors = PyList_Size(doorList);
    for (Py_ssize_t i = 0; i < numDoors; i++) {
        PyObject* doorName = PyList_GetItem(doorList, i);
        const char* doorNameStr = getStringFromPyObject(doorName);
        Item* door = getItemByName(doorNameStr);
        assertThat(door != NULL, "Error! Door not found");

        // Each door has 2 connections. Find that one that isn't this
        Room* otherRoom = getOppositeRoom(getCurrentRoom(), door);
        if (otherRoom->isVisible()) {
            if (lowercase(otherRoom->getName()).compare(directionOrRoom) == 0 || otherRoom->hasAlias(directionOrRoom)) {
                if (returnDoor == NULL) {
                    returnDoor = door;
                } else if (returnDoor != door) {
                    returnDoor = duplicateItem;
                }
            }
        }
    }

    return returnDoor;
}

/*
    Internal usage - get the room on the opposite side of a door
*/
Room* PyEngine::getOppositeRoom(Room* firstRoom, Item* door)
{
    assertThat(door->isDoor(), "Error! This isn't a door");

    PyObject* roomConnections = PyObject_GetAttrString(door->getPyItem(), (char*)"roomConnections");
    assertThat(PyDict_Check(roomConnections), "Error! roomConnections is not a dictionary");

    PyObject* roomList = PyDict_Values(roomConnections);
    Py_ssize_t numRooms = PyList_Size(roomList);
    assertThat(numRooms == 2, "Error! A door must have exactly 2 rooms");

    bool success = false; // the input room must be one of them to be successful
    Room* otherRoom = NULL;
    for (Py_ssize_t i = 0; i < numRooms; i++) {
        PyObject* roomName = PyList_GetItem(roomList, i);
        const char* roomNameStr = getStringFromPyObject(roomName);
        Room* room = getRoomByName(roomNameStr);
        assertThat(room != NULL, "Error! Room not found");

        if (room == firstRoom) success = true;
        else otherRoom = room;
    }

    assertThat(success, "Error! Door doesn't connect to this room");
    return otherRoom;
}

/*
    Save game to .save
    Only records the difference betweeen the current state and the initial state
*/
void PyEngine::saveGame()
{
    std::ofstream file(".save");

    // Header - score, current room, inventory
    file << "score: " << getScore() << std::endl;
    file << "currentRoom: " << getClassName(getCurrentRoom()->getPyRoom()) << std::endl;
    file << "inventory:";
    for (auto& item : *inventory) {
        file << " " << getClassName(item->getPyItem());
    }
    file << std::endl;

    // Items
    for (auto& kv : items) {
        PyObject* pyObj = kv.second->getPyItem();
        PyObject* initialValues = initialItems[kv.first];
        std::string className = getClassName(pyObj);
        file << className << ": ";
        
        PyObject* visible = PyObject_GetAttrString(pyObj, (char*)"visible");
        PyObject* initVisible = PyDict_GetItemString(initialValues, (char*)"visible");
        if (visible != initVisible) {
            file << "visible=";
            if (visible == Py_True) {
                file << "True\t";
            } else {
                file << "False\t";
            }
        }

        PyObject* properties = PyObject_GetAttrString(pyObj, (char*)"properties");
        PyObject* initProperties = PyDict_GetItemString(initialValues, (char*)"properties");
        PyObject* propertyKeys = PyDict_Keys(initProperties);
        Py_ssize_t size = PyList_Size(propertyKeys);
        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject* propName = PyList_GetItem(propertyKeys, i);
            PyObject* propValue = PyDict_GetItem(properties, propName);
            PyObject* initPropValue = PyDict_GetItem(initProperties, propName);
            if (PyBool_Check(propValue)) {
                if (propValue != initPropValue) {
                    file << "properties_" << getStringFromPyObject(propName) << "=";
                    if (propValue == Py_True) file << "True\t";
                    else file << "False\t";
                }
            } else if (PyLong_Check(propValue)) {
                long propLong = PyLong_AsLong(propValue);
                long initPropLong = PyLong_AsLong(initPropValue);
                if (propLong != initPropLong) {
                    file << "properties_" << getStringFromPyObject(propName) << "=" << propLong << "\t";
                }
            } else {
                std::string propStr = getStringFromPyObject(propValue);
                std::string initPropStr = getStringFromPyObject(initPropValue);
                if (propStr.compare(initPropStr) != 0) {
                    file << "properties_" << getStringFromPyObject(propName) << "=\"" << propStr << "\"\t";
                }
            }
        }

        file << std::endl;
    }

    for (auto& kv : rooms) {
        PyObject* pyObj = kv.second->getPyRoom();
        PyObject* initialValues = initialRooms[kv.first];
        std::string className = getClassName(pyObj);
        file << className << ": ";
        
        PyObject* visible = PyObject_GetAttrString(pyObj, (char*)"visible");
        PyObject* initVisible = PyDict_GetItemString(initialValues, (char*)"visible");
        if (visible != initVisible) {
            file << "visible=";
            if (visible == Py_True) {
                file << "True\t";
            } else {
                file << "False\t";
            }
        }

        PyObject* visited = PyObject_GetAttrString(pyObj, (char*)"visited");
        PyObject* initVisited = PyDict_GetItemString(initialValues, (char*)"visited");
        if (visited != initVisited) {
            file << "visited=";
            if (visible == Py_True) {
                file << "True\t";
            } else {
                file << "False\t";
            }
        }

        PyObject* properties = PyObject_GetAttrString(pyObj, (char*)"properties");
        PyObject* initProperties = PyDict_GetItemString(initialValues, (char*)"properties");
        PyObject* propertyKeys = PyDict_Keys(initProperties);
        Py_ssize_t size = PyList_Size(propertyKeys);
        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject* propName = PyList_GetItem(propertyKeys, i);
            PyObject* propValue = PyDict_GetItem(properties, propName);
            PyObject* initPropValue = PyDict_GetItem(initProperties, propName);
            if (PyBool_Check(propValue)) {
                if (propValue != initPropValue) {
                    file << "properties_" << getStringFromPyObject(propName) << "=";
                    if (propValue == Py_True) file << "True\t";
                    else file << "False\t";
                }
            } else if (PyLong_Check(propValue)) {
                long propLong = PyLong_AsLong(propValue);
                long initPropLong = PyLong_AsLong(initPropValue);
                if (propLong != initPropLong) {
                    file << "properties_" << getStringFromPyObject(propName) << "=" << propLong << "\t";
                }
            } else {
                std::string propStr = getStringFromPyObject(propValue);
                std::string initPropStr = getStringFromPyObject(initPropValue);
                if (propStr.compare(initPropStr) != 0) {
                    file << "properties_" << getStringFromPyObject(propName) << "=\"" << propStr << "\"\t";
                }
            }
        }

        PyObject* items = PyObject_GetAttrString(pyObj, (char*)"items");
        PyObject* initItems = PyDict_GetItemString(initialValues, (char*)"items");
        
        // Turn both lists into vectors
        std::vector<std::string> itemsVector;
        std::vector<std::string> initItemsVector;
        size = PyList_Size(items);
        for (Py_ssize_t i = 0; i < size; i++) {
            itemsVector.push_back(getStringFromPyObject(PyList_GetItem(items, i)));
        }
        size = PyList_Size(initItems);
        for (Py_ssize_t i = 0; i < size; i++) {
            initItemsVector.push_back(getStringFromPyObject(PyList_GetItem(initItems, i)));
        }

        for (auto& itemName : itemsVector) {
            if (std::find(initItemsVector.begin(), initItemsVector.end(), itemName) == initItemsVector.end()) {
                file << "items+" << itemName << "\t";
            }
        }
        for (auto& itemName : initItemsVector) {
            if (std::find(itemsVector.begin(), itemsVector.end(), itemName) == itemsVector.end()) {
                file << "items-" << itemName << "\t";
            }
        }

        PyObject* droppedItems = PyObject_GetAttrString(pyObj, (char*)"droppedItems");
        std::vector<std::string> droppedItemsVector;
        size = PyList_Size(droppedItems);
        for (Py_ssize_t i = 0; i < size; i++) {
            droppedItemsVector.push_back(getStringFromPyObject(PyList_GetItem(droppedItems, i)));
        }
        for (auto& itemName : droppedItemsVector) {
            file << "droppedItems+" << itemName << "\t";
        }

        file << std::endl;
    }

    file.close();
}

/*
    Load game from save file
    Reloads all the rooms and items from file, then applies the changes from .save
*/
void PyEngine::loadGame()
{
    instance->inventory->clear();
    instance->verbs = new std::unordered_map<std::string, std::unordered_set<std::string>*>();
    instance->items.clear();
    instance->rooms.clear();
    instance->LoadPyFiles("Content");

    // Open file
    std::ifstream savefile;
    savefile.open(".save");
    if (!savefile.good()) {
        printf("loadgame failed. Save file missing\n");
        return;
    }

    // Set score
    std::string scoreLine;
    std::getline(savefile, scoreLine);
    //printf("Score line:: %s\n", scoreLine.c_str());
    long score = std::stol(scoreLine.substr(7));
    setScore(score);

    // Set current room
    std::string currentRoomLine;
    std::getline(savefile, currentRoomLine);
    //printf("Current room line:: %s\n", currentRoomLine.c_str());
    std::string roomName = currentRoomLine.substr(13);
    //printf("Class name for current room: %s\n", roomName.c_str());
    // Iterate through rooms to find the correct one
    for (const auto& roomItr : rooms) {
        Room* room = roomItr.second;
        PyObject* pyroom = room->getPyRoom();
        PyObject* pyclass = PyObject_GetAttrString(pyroom, (char*)"__class__");
        PyObject* className = PyObject_GetAttrString(pyclass, (char*)"__name__");
        const char* classNameCStr = getStringFromPyObject(className);
        std::string classNameCppStr(classNameCStr);
        //printf("Class name found: %s\n", classNameCStr);
        if (roomName.compare(classNameCppStr) == 0) {
            //printf("Going to %s\n", ssss.c_str());
            goToRoom(room);
        }

    }

    // Set inventory
    inventory->clear();
    std::string inventoryLine;
    std::getline(savefile, inventoryLine);
    //printf("Inventory line:: %s\n", inventoryLine.c_str());
    std::stringstream inventoryStream;
    inventoryStream << inventoryLine;
    std::string word;
    std::getline(inventoryStream, word, ' '); // read past inventory:
    while (std::getline(inventoryStream, word, ' ')) {
        //printf("Item: %s\n", word.c_str());
        for (const auto& itemItr : items) {
            Item* item = itemItr.second;
            PyObject* pyitem = item->getPyItem();
            PyObject* pyclass = PyObject_GetAttrString(pyitem, (char*)"__class__");
            PyObject* className = PyObject_GetAttrString(pyclass, (char*)"__name__");
            const char* classNameCStr = getStringFromPyObject(className);
            std::string classNameCppStr(classNameCStr);        
            if (word.compare(classNameCppStr) == 0) {
                inventory->push_back(item);
            }
        }
    }

    // Set all the content
    std::string line;
    while (std::getline(savefile, line)) {
        std::stringstream stream;
        stream << line;
        std::string objectClassName;
        std::getline(stream, objectClassName, ' ');
        objectClassName = objectClassName.substr(0, objectClassName.length() - 1); // get rid of ':'
        //printf("Class line:: %s\n", line.c_str());
        PyObject* pyObj = NULL; // Item or Room object
        for (const auto& roomItr : rooms) {
            Room* room = roomItr.second;
            PyObject* pyroom = room->getPyRoom();
            PyObject* pyclass = PyObject_GetAttrString(pyroom, (char*)"__class__");
            PyObject* className = PyObject_GetAttrString(pyclass, (char*)"__name__");
            const char* classNameCStr = getStringFromPyObject(className);
            std::string classNameCppStr(classNameCStr);
            if (objectClassName.compare(classNameCppStr) == 0) {
                pyObj = pyroom;
            }
        }
        for (const auto& itemItr : items) {
            Item* item = itemItr.second;
            PyObject* pyitem = item->getPyItem();
            PyObject* pyclass = PyObject_GetAttrString(pyitem, (char*)"__class__");
            PyObject* className = PyObject_GetAttrString(pyclass, (char*)"__name__");
            const char* classNameCStr = getStringFromPyObject(className);
            std::string classNameCppStr(classNameCStr);
            if (objectClassName.compare(classNameCppStr) == 0) {
                pyObj = pyitem;
            }
        }

        if (pyObj == NULL) {
            //printf("Did not find class %s\n", objectClassName.c_str());
            continue;
        }
        //printf("Found %s\n", objectClassName.c_str());
        std::string propertyChange;
        while (std::getline(stream, propertyChange, '\t')) {
            // Visible flag
            if (strncmp(propertyChange.c_str(), (char*)"visible", 7) == 0) {
                std::string value = propertyChange.substr(8);
                if (strncmp(value.c_str(), (char*)"T", 1) == 0) {
                    PyObject_SetAttrString(pyObj, (char*)"visible", Py_True);
                } else {
                    PyObject_SetAttrString(pyObj, (char*)"visible", Py_False);
                }
            }

            // Visited flag
            if (strncmp(propertyChange.c_str(), (char*)"visited", 7) == 0) {
                std::string value = propertyChange.substr(8);
                if (strncmp(value.c_str(), (char*)"T", 1) == 0) {
                    PyObject_SetAttrString(pyObj, (char*)"visited", Py_True);
                } else {
                    PyObject_SetAttrString(pyObj, (char*)"visited", Py_False);
                }
            }

            // Properties
            if (strncmp(propertyChange.c_str(), (char*)"properties", 10) == 0) {
                size_t equalsPosition = propertyChange.find("=", 0);
                std::string propertyName = propertyChange.substr(11, equalsPosition - 11);
                std::string newValue = propertyChange.substr(equalsPosition + 1);
                //printf("Property name: %s\n", propertyName.c_str());
                //printf("New value: %s\n", newValue.c_str());
                PyObject* pyProperties = PyObject_GetAttrString(pyObj, (char*)"properties");
                PyObject* pyValue = NULL;
                if (newValue.compare("True") == 0) {
                    pyValue = Py_True;
                } else if (newValue.compare("False") == 0) {
                    pyValue = Py_False;
                } else if (newValue.find("\"") == 0) {
                    std::string newValueString = newValue.substr(1, newValue.length() - 2);
                    pyValue = PyUnicode_FromString(newValueString.c_str());
                } else {
                    // try making it a number
                    long newValueLong = atol(newValue.c_str());
                    pyValue = PyLong_FromLong(newValueLong);
                }
                PyDict_SetItemString(pyProperties, propertyName.c_str(), pyValue);
            }

            // Items
            if (strncmp(propertyChange.c_str(), (char*)"items", 5) == 0) {
                bool add = false; // Item is being added or removed
                if (propertyChange.find("+") < propertyChange.length()) add = true;
                // Get item name
                std::string name = "";
                if (add) {
                    size_t plusLocation = propertyChange.find("+");
                    name = propertyChange.substr(plusLocation + 1);
                } else {
                    size_t minusLocation = propertyChange.find("-");
                    name = propertyChange.substr(minusLocation + 1);
                }
                // Find current index (if exists)
                int itemIndex = -1;
                PyObject* itemList = PyObject_GetAttrString(pyObj, (char*)"items");
                Py_ssize_t size = PyList_Size(itemList);
                for (Py_ssize_t i = 0; i < size; i++) {
                    PyObject* itemName = PyList_GetItem(itemList, i);
                    const char* itemNameStr = getStringFromPyObject(itemName);
                    if (name.compare(itemNameStr) == 0) {
                        itemIndex = i;
                        break;
                    }
                }

                // Add item
                if (add && itemIndex == -1) {
                    PyList_Append(itemList, PyUnicode_FromString(name.c_str()));
                }
                // remove item
                if (!add && itemIndex != -1) {
                    PyObject_DelItem(itemList, PyLong_FromLong(itemIndex));
                }
            }

            // Dropped items
            if (strncmp(propertyChange.c_str(), (char*)"droppedItems", 5) == 0) {
                bool add = false; // Item is being added or removed
                if (propertyChange.find("+") < propertyChange.length()) add = true;
                // Get item name
                std::string name = "";
                if (add) {
                    size_t plusLocation = propertyChange.find("+");
                    name = propertyChange.substr(plusLocation + 1);
                } else {
                    size_t minusLocation = propertyChange.find("-");
                    name = propertyChange.substr(minusLocation + 1);
                }
                // Find current index (if exists)
                int itemIndex = -1;
                PyObject* itemList = PyObject_GetAttrString(pyObj, (char*)"droppedItems");
                Py_ssize_t size = PyList_Size(itemList);
                for (Py_ssize_t i = 0; i < size; i++) {
                    PyObject* itemName = PyList_GetItem(itemList, i);
                    const char* itemNameStr = getStringFromPyObject(itemName);
                    if (name.compare(itemNameStr) == 0) {
                        itemIndex = i;
                        break;
                    }
                }

                // Add item
                if (add && itemIndex == -1) {
                    PyList_Append(itemList, PyUnicode_FromString(name.c_str()));
                }
                // remove item
                if (!add && itemIndex != -1) {
                    PyObject_DelItem(itemList, PyLong_FromLong(itemIndex));
                }
            }
        }
    }

    savefile.close();
}

/*
    Helper to turn Python object into string
*/
const char* getStringFromPyObject(PyObject* strObj)
{
    if (strObj == NULL) {
        return (char*)"";
    }
    if (PyUnicode_Check(strObj)) {
        PyObject* bytes = PyUnicode_AsEncodedString(strObj, "UTF-8", "strict");
        return strdup(PyBytes_AS_STRING(bytes));
    } else {
        return "";
    }
}

/*
    Helper to get a string from a Python object
    Returns empty string if property not found or not a string
*/
const char* getStringFromPyObject(PyObject* obj, const char* propertyName)
{
    if (PyObject_HasAttrString(obj, propertyName))
    {
        PyObject* property = PyObject_GetAttrString(obj, propertyName);
        return getStringFromPyObject(property);
    } 
    else
    {
        return "";
    }
}

/*
    Returns a new lowercase version of a string. Used to make things case insensitive
*/
std::string lowercase(std::string inputString)
{
    std::string lowerString(inputString);
    for (std::string::size_type i = 0; i < inputString.length(); i++) {
        lowerString[i] = std::tolower(inputString[i]);
    }
    return lowerString;
}

/*
    Error checking
*/
void assertThat(bool assertion, const char* message)
{
    if (!assertion) {
        printf("Assertion in file %s\n", PyEngine::getInstance()->currentFile);
        printf("%s\n", message);
        exit(1);
    }
}

/*
    Make a copy of a room or item, but only for the things that can be saved
*/  
PyObject* copyObject(PyObject* in)
{
    PyObject* dictionary = PyDict_New();

    // Visible flag
    PyDict_SetItemString(dictionary, (char*)"visible", PyObject_GetAttrString(in, (char*)"visible"));

    // Visited flag
    if (PyObject_HasAttrString(in, (char*)"visited")) {
        PyDict_SetItemString(dictionary, (char*)"visited", PyObject_GetAttrString(in, (char*)"visited"));
    }

    // Properties dictionary
    PyDict_SetItemString(dictionary, (char*)"properties", PyDict_Copy(PyObject_GetAttrString(in, (char*)"properties")));

    // Items list
    if (PyObject_HasAttrString(in, (char*)"items")) {
        PyObject* newList = PyList_New(0);
        PyObject* inList = PyObject_GetAttrString(in, (char*)"items");
        Py_ssize_t size = PyList_Size(inList);
        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject* itemName = PyList_GetItem(inList, i);
            PyList_Append(newList, itemName);
        }
        PyDict_SetItemString(dictionary, (char*)"items", newList);
    }

    return dictionary;
}

std::string getClassName(PyObject* obj)
{
    PyObject* pyclass = PyObject_GetAttrString(obj, (char*)"__class__");
    PyObject* className = PyObject_GetAttrString(pyclass, (char*)"__name__");
    const char* classNameCStr = getStringFromPyObject(className);
    std::string str(classNameCStr);
    return str;
}

// Main just for testing
/*
int main() {
    PyEngine* p = PyEngine::getInstance();
    //Room* room1 = p->getRoomByName("dungeon");
    
    //p->goToRoom(room1);
}
*/


