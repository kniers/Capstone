#ifndef PYENGINE_H
#define PYENGINE_H

#include <Python.h>

class PyEngine
{
private:
    static PyEngine* instance; // Singleton

    /****************************************
     *      Engine Data Members
    ****************************************/
    PyObject* score;

    /****************************************
     *      Python API
    ****************************************/
    // Score
    static PyObject* emb_getScore(PyObject *self, PyObject *args);
    static PyObject* emb_setScore(PyObject *self, PyObject *args);

    /****************************************
     *      Python Module Setup
    ****************************************/
    static PyMethodDef EmbMethods[];
    static PyModuleDef EmbModule;
    static PyObject* PyInit_emb(void); 
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
};

#endif