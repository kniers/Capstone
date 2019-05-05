#include <Python.h>
#include <dirent.h>
#include <string>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
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
        instance->locals = PyDict_New();
        instance->globals = PyDict_New();
        std::remove("err.txt");
    }
    return instance;
}

/*
    Run 1 line of Python code
*/
void PyEngine::debugConsole(std::string command)
{
    PyRun_SimpleString(command.c_str());
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
    return PyLong_AsLong(score);
}

/*
    C++ API to set game score
*/
void PyEngine::setScore(long newScore)
{
    score = PyLong_FromLong(newScore);
    Py_INCREF(score);
}

/*
    Python API to get game score
*/
PyObject* PyEngine::emb_getScore(PyObject *self, PyObject *args)
{
    Py_INCREF(PyEngine::getInstance()->score);
    return PyEngine::getInstance()->score;
}

/*
    Python API to set game score
*/
PyObject* PyEngine::emb_setScore(PyObject *self, PyObject *args)
{
    PyArg_UnpackTuple(args, "", 1, 1, &(PyEngine::getInstance()->score));
    Py_INCREF(PyEngine::getInstance()->score);
    return PyEngine::getInstance()->score;
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
    Item* item;
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
    Setup a new instance of a door item
*/
PyObject* PyEngine::emb_setupDoor(PyObject *self, PyObject *args)
{
    PyObject* pyitem;
    Item* item;
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
                        PyRun_SimpleFile(fp, filename.c_str()); 
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

// Main just for testing
/*
int main() {
    PyEngine* p = PyEngine::getInstance();
    //Room* room1 = p->getRoomByName("dungeon");
    
    //p->goToRoom(room1);
}
*/


