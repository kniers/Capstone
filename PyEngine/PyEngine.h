#ifndef PYENGINE_H
#define PYENGINE_H

#include <Python.h>
#include <string>
#include <map>
#include "Item.h"

class PyEngine
{
private:
    static PyEngine* instance; // Singleton

    /****************************************
     *      Engine Data Members
    ****************************************/
    PyObject* score;
    std::map<std::string, Item*> items;

    /****************************************
     *      Python API
    ****************************************/
    // Score
    static PyObject* emb_getScore(PyObject *self, PyObject *args);
    static PyObject* emb_setScore(PyObject *self, PyObject *args);

    // Item
    static PyObject* emb_setupItem(PyObject *self, PyObject *args);
    static PyObject* emb_getItemByID(PyObject *self, PyObject *args);

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
};

// Python3 string conversion
char* getStringFromPyObject(PyObject* strObj);
char* getStringFromPyObject(PyObject* obj, char* propertyName);

#endif