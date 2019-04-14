#include <Python.h>
#include "PyEngine.h"

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
    }
    return instance;
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
    Collection of Python APIs
*/
PyMethodDef PyEngine::EmbMethods[] = 
{
    {"getScore", emb_getScore, METH_VARARGS, ""},
    {"setScore", emb_setScore, METH_VARARGS, ""},
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


// Main just for testing
/*
int main() {
    PyEngine* p = PyEngine::getInstance();
    p->setScore(123);
    p->setScore(p->getScore() + 5);
    PyRun_SimpleString("import eng");
    PyRun_SimpleString("eng.setScore(eng.getScore() + 100)");
    PyRun_SimpleString("print(eng.getScore())");
    printf("Score: %ld\n", p->getScore());
}
*/