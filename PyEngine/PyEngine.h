#ifndef PYENGINE_H
#define PYENGINE_H

#include <Python.h>
#include <string>
#include <map>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include "Item.h"
#include "Room.h"

class PyEngine
{
private:
    static PyEngine* instance; // Singleton

    /****************************************
     *      Engine Data Members
    ****************************************/
    long score;
    std::map<std::string, Item*> items;
    std::map<std::string, Room*> rooms;
    Room* currentRoom;
    std::vector<Item*>* inventory;
    std::unordered_map<std::string, std::unordered_set<std::string>*>* verbs;
    Item* duplicateItem;

    // Initial states for saving game
    std::map<std::string, PyObject*> initialItems;
    std::map<std::string, PyObject*> initialRooms;

    /****************************************
     *      Internal access
    ****************************************/
    Room* getRoom(PyObject* pyRoom);
    Item* getItem(PyObject* pyItem);

    Item* getDoorTo(std::string directionOrRoom);
    Room* getOppositeRoom(Room* firstRoom, Item* door);

    /****************************************
     *      Python API
    ****************************************/
    // Score
    static PyObject* emb_getScore(PyObject *self, PyObject *args);
    static PyObject* emb_setScore(PyObject *self, PyObject *args);

    // Win/Loss
    static PyObject* emb_winGame(PyObject *self, PyObject *args);
    static PyObject* emb_loseGame(PyObject *self, PyObject *args);

    // Verbs
    static PyObject* emb_setVerbs(PyObject* self, PyObject *args);

    // Item
    static PyObject* emb_setupItem(PyObject *self, PyObject *args);
    static PyObject* emb_getItemByName(PyObject *self, PyObject *args);
    static PyObject* emb_addToInventory(PyObject *self, PyObject *args);
    static PyObject* emb_removeFromInventory(PyObject *self, PyObject *args);
    static PyObject* emb_inInventory(PyObject *self, PyObject *args);
    static PyObject* emb_dropItem(PyObject *self, PyObject *args);

    // Door
    static PyObject* emb_setupDoor(PyObject *self, PyObject *args);

    // Room
    static PyObject* emb_setupRoom(PyObject *self, PyObject *args);
    static PyObject* emb_getRoomByName(PyObject *self, PyObject *args);
    static PyObject* emb_getCurrentRoom(PyObject *self, PyObject *args);
    static PyObject* emb_goToRoom(PyObject *self, PyObject *args);

    /****************************************
     *      Python Module Setup
    ****************************************/
    static PyMethodDef EmbMethods[];
    static PyModuleDef EmbModule;
    static PyObject* PyInit_emb(void); 
    void LoadPyFiles(std::string directoryName);
    PyEngine();
    ~PyEngine();

public:
    /****************************************
     *      Engine Access
    ****************************************/
    static PyEngine* getInstance();
    char* currentFile;

    /****************************************
     *      Debug API
    ****************************************/
    bool debugConsole(std::string command);
    std::string debugRooms();
    std::string debugItems();
    std::string debugDoors();
    std::string debugRoomDetails(std::string roomName);
    std::string debugItemDetails(std::string itemName);


    /****************************************
     *      C++ API
    ****************************************/
    // Save / Load
    void saveGame();
    void loadGame();

    // Score   
    long getScore();
    void setScore(long newScore);

    // Verb
    std::string getVerb(std::string verb);

    // Item
    Item* getItemByName(std::string itemName);
    bool inInventory(Item* item);
    std::vector<Item*>* getInventory();
    std::vector<Item*> getGlobalItems();
    Item* getAccessibleItem(std::string itemName);

    // Room
    Room* getRoomByName(std::string roomName);
    Room* getCurrentRoom();
    void goToRoom(Room* room);
};

// Python3 string conversion
const char* getStringFromPyObject(PyObject* strObj);
const char* getStringFromPyObject(PyObject* obj, const char* propertyName);
std::string printPyObject(PyObject* obj);

PyObject* copyObject(PyObject* in);
std::string getClassName(PyObject* obj);

std::string lowercase(std::string inputString);

void assertThat(bool assertion, const char* message);

#endif