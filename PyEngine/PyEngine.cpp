#include <Python.h>
#include <dirent.h>
#include <string>
#include <map>
#include "PyEngine.h"
#include "Item.h"

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
        instance->LoadPyFiles("Content");
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
    Python API - add an item to the engine
*/
PyObject* PyEngine::emb_setupItem(PyObject *self, PyObject *args)
{
    PyObject* pyitem;
    PyArg_UnpackTuple(args, "", 1, 1, &pyitem);
    Py_INCREF(pyitem);
    char* id = getStringFromPyObject(pyitem, (char*)"itemID");
    Item* item = new Item(pyitem);
    PyEngine::getInstance()->items.insert(std::pair<std::string, Item*>(id, item));
    return PyLong_FromLong(0);
}

/*
    Python API - get an item by "itemID" property
*/
PyObject* PyEngine::emb_getItemByID(PyObject *self, PyObject *args)
{
    PyEngine* instance = PyEngine::getInstance();
    PyObject* itemID;
    PyArg_UnpackTuple(args, "", 1, 1, &itemID);
    char* itemIDstr = getStringFromPyObject(itemID);
    Item* item = instance->getItemByID(itemIDstr);
    return item->getPyItem();
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
    Helper to turn Python object into string
*/
char* getStringFromPyObject(PyObject* strObj)
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
char* getStringFromPyObject(PyObject* obj, char* propertyName)
{
    PyObject* property = PyObject_GetAttrString(obj, propertyName);
    return getStringFromPyObject(property);
}



// Main just for testing
/*
int main() {
    PyEngine* p = PyEngine::getInstance();
    Item* item = p->getItemByID("exampleitem");
    printf("%s\n", item->getDescription());
    item->runVerb("cook", p->getItemByID("ex2"));
    if (item->hasVerb("look")) printf("Has look!\n");
}
*/
