#include <Python.h>
#include <dirent.h>
#include <string>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
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
        instance->globalItems = new std::vector<Item*>();
        instance->verbs = new std::unordered_map<std::string, std::unordered_set<std::string>*>();
        instance->LoadPyFiles("Content");
    }
    return instance;
}

/*
    Internal access - get a Room object from the Py version
*/
Room* PyEngine::getRoom(PyObject* pyRoom)
{
    const char* roomName = getStringFromPyObject(pyRoom, (char*)"rootID");
    return getInstance()->getRoomByID(roomName);
}

/*
    Internal access - get an Item object from the Py version
*/
Item* PyEngine::getItem(PyObject* pyItem)
{
    const char* itemName = getStringFromPyObject(pyItem, (char*)"itemID");
    return getInstance()->getItemByID(itemName);
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
    PyArg_UnpackTuple(args, "", 1, 1, &pyitem);
    Py_INCREF(pyitem);
    const char* id = getStringFromPyObject(pyitem, (char*)"itemID");
    if (strlen(id) > 0) {
        Item* item = new Item(pyitem);
        PyEngine::getInstance()->items.insert(std::pair<std::string, Item*>(id, item));
    }
    return Py_BuildValue("");
}

/*
    Python API - get an item by "itemID" property
*/
PyObject* PyEngine::emb_getItemByID(PyObject *self, PyObject *args)
{
    PyEngine* instance = PyEngine::getInstance();
    PyObject* itemID;
    PyArg_UnpackTuple(args, "", 1, 1, &itemID);
    const char* itemIDstr = getStringFromPyObject(itemID);
    Item* item = instance->getItemByID(itemIDstr);
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
    const char* id = getStringFromPyObject(pyroom, (char*)"roomID");
    if (strlen(id) > 0) {
        Room* room = new Room(pyroom);
        getInstance()->rooms.insert(std::pair<std::string, Room*>(id, room));
    }
    return Py_BuildValue("");
}

/*
    Python API - get a room by "roomID" property
*/
PyObject* PyEngine::emb_getRoomByID(PyObject *self, PyObject *args)
{
    PyObject* roomID;
    PyArg_UnpackTuple(args, "", 1, 1, &roomID);
    const char* roomIDstr = getStringFromPyObject(roomID);
    Room* room = getInstance()->getRoomByID(roomIDstr);
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
        room->callEnter();
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
    {"getItemByID", emb_getItemByID, METH_VARARGS, ""},
    {"winGame", emb_winGame, METH_VARARGS, ""},
    {"loseGame", emb_loseGame, METH_VARARGS, ""},
    {"setupRoom", emb_setupRoom, METH_VARARGS, ""},
    {"getRoomByID", emb_getRoomByID, METH_VARARGS, ""},
    {"getCurrentRoom", emb_getCurrentRoom, METH_VARARGS, ""},
    {"goToRoom", emb_goToRoom, METH_VARARGS, ""},
    {"addToInventory", emb_addToInventory, METH_VARARGS, ""},
    {"removeFromInventory", emb_removeFromInventory, METH_VARARGS, ""},
    {"inInventory", emb_inInventory, METH_VARARGS, ""},
    {"setVerbs", emb_setVerbs, METH_VARARGS, ""},
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
                        PyRun_SimpleFile(fp, filename.c_str()); 
                    } else {
                        fprintf(stderr, "Could not open file \n");
                    }       
                }
            }
        }
    }
    closedir(contentDir);
}

/*
    Get item by "itemID" property
*/
Item* PyEngine::getItemByID(std::string itemID)
{
    Item* item = NULL;
    std::map<std::string, Item*>::iterator itr = items.find(itemID);
    if (itr != items.end()) 
    {
        item = itr->second;
    }
    return item;
}

/*
    Get room by "roomID" property
*/
Room* PyEngine::getRoomByID(std::string roomID)
{
    Room* room = NULL;
    std::map<std::string, Room*>::iterator itr = rooms.find(roomID);
    if (itr != rooms.end())
    {
        room = itr->second;
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
std::vector<Item*>* PyEngine::getGlobalItems()
{
    return globalItems;
}

/*
    Get a collection of all the items in a room
*/
std::vector<Item*> PyEngine::getItemsInRoom(Room* room)
{
    // Items in a room haven't been defined yet
    std::vector<Item*> items;
    return items;
}

/*
    Get an item by name. Only returns items that are in current room, in inventory,
    or globally accessible. Also gives you an item if the itemName matches an item alias
*/
// This will probably have to do something about checking for duplicates
// For instance there could be multiple items with alias "key"
// One solution: have a global item called key that just tells you to be more specific
Item* PyEngine::getAccessibleItem(const char* itemName)
{
    // item aliases haven't been defined yet, but there's a function for it
    Item* item = NULL;
    std::vector<Item*> itemsInRoom = getItemsInRoom(getCurrentRoom());
    for (uint i = 0; i < itemsInRoom.size(); i++)
    {
        Item* testItem = itemsInRoom[i];
        if (testItem->hasAlias(itemName) && testItem->isVisible())
        {
            item = testItem;
        }
    }
    std::vector<Item*> itemsInInventory = *getInventory();
    for (uint i = 0; i < itemsInInventory.size(); i++)
    {
        Item* testItem = itemsInInventory[i];
        if (testItem->hasAlias(itemName) && testItem->isVisible())
        {
            item = testItem;
        }
    }
    std::vector<Item*> globalItems = *getGlobalItems();
    for (uint i = 0; i < globalItems.size(); i++)
    {
        Item* testItem = globalItems[i];
        if (testItem->hasAlias(itemName) && testItem->isVisible())
        {
            item = testItem;
        }
    }
    return item;
}

const char* PyEngine::getVerb(const char* verb)
{
    auto itr = verbs->begin();
    while (itr != verbs->end())
    {
        std::unordered_set<std::string>* synonyms = itr->second;
        auto synonymItr = synonyms->begin();
        while (synonymItr != synonyms->end())
        {
            if (strcmp(verb, (*synonymItr).c_str()) == 0)
            {
                return itr->first.c_str();
            }
            synonymItr++;
        }
        itr++;
    }
    return NULL;
}

/*
    Helper to turn Python object into string
*/
const char* getStringFromPyObject(PyObject* strObj)
{
    if (PyUnicode_Check(strObj)) {
        PyObject* bytes = PyUnicode_AsEncodedString(strObj, "UTF-8", "strict");
        return strdup(PyBytes_AS_STRING(bytes));
    } else {
        return '\0';
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
        return '\0';
    }
}



// Main just for testing
/*
int main() {
    PyEngine* p = PyEngine::getInstance();
    Room* room1 = p->getRoomByID("room1");
    Room* room2 = p->getRoomByID("room2");
    Item* item1 = p->getItemByID("item1");
    
    printf("%s\n", p->getVerb((char*)"eat"));
    fflush(stdout);
}
*/

