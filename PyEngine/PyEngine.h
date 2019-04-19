#ifndef PYENGINE_H
#define PYENGINE_H

#include <Python.h>
#include <string>
#include <map>
#include <vector>
#include "Item.h"
#include "Room.h"

class PyEngine
{
private:
    static PyEngine* instance; // Singleton

    /****************************************
     *      Engine Data Members
    ****************************************/
    PyObject* score;
    std::map<std::string, Item*> items;
    std::map<std::string, Room*> rooms;
    Room* currentRoom;
    std::vector<Item*>* inventory;

    /****************************************
     *      Internal access
    ****************************************/
    Room* getRoom(PyObject* pyRoom);
    Item* getItem(PyObject* pyItem);

    /****************************************
     *      Python API
    ****************************************/
    // Score
    static PyObject* emb_getScore(PyObject *self, PyObject *args);
    static PyObject* emb_setScore(PyObject *self, PyObject *args);

    // Win/Loss
    static PyObject* emb_winGame(PyObject *self, PyObject *args);
    static PyObject* emb_loseGame(PyObject *self, PyObject *args);

    // Item
    static PyObject* emb_setupItem(PyObject *self, PyObject *args);
    static PyObject* emb_getItemByID(PyObject *self, PyObject *args);
    static PyObject* emb_addToInventory(PyObject *self, PyObject *args);
    static PyObject* emb_removeFromInventory(PyObject *self, PyObject *args);
    static PyObject* emb_inInventory(PyObject *self, PyObject *args);

    // Room
    static PyObject* emb_setupRoom(PyObject *self, PyObject *args);
    static PyObject* emb_getRoomByID(PyObject *self, PyObject *args);
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

    /****************************************
     *      C++ API
    ****************************************/
    // Score   
    long getScore();
    void setScore(long newScore);

    // Item
    Item* getItemByID(std::string itemID);
    bool inInventory(Item* item);
    std::vector<Item*>* getInventory();

    // Room
    Room* getRoomByID(std::string roomID);
    Room* getCurrentRoom();
    void goToRoom(Room* room);
};

// Python3 string conversion
char* getStringFromPyObject(PyObject* strObj);
char* getStringFromPyObject(PyObject* obj, char* propertyName);

#endif