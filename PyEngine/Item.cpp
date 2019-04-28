#include <Python.h>
#include <string>
#include "Item.h"
#include "PyEngine.h"

/*
    Create an Item - a wrapper around an Item class made in Python
*/
Item::Item(PyObject* _pyItem, bool _door, bool _duplicate)
{
    pyItem = _pyItem;
    doorObj = _door;
    duplicate = _duplicate; // The duplicate item is a singleton
}

/*
    Internal access - get the Python version
*/
PyObject* Item::getPyItem()
{
    return pyItem;
}

/*
    Get the "name" attribute of the item
*/
std::string Item::getName()
{
    std::string name(getStringFromPyObject(pyItem, (char*)"name"));
    return name;
}

/*
    Get the "description" property of the item as a string
*/
/*const char* Item::getDescription()
{
    return getStringFromPyObject(pyItem, (char*)"description");
}*/

/*
    Check if an item has a verb defined. If withIndObj is true, it makes sure the item can accept an item argument
*/
bool Item::hasVerb(std::string verb, bool withIndObj)
{
    if (!PyObject_HasAttrString(pyItem, verb.c_str())) return false;
    PyObject* callable = PyObject_GetAttrString(pyItem, verb.c_str());
    if (PyCallable_Check(callable)) {
        PyObject* fc = PyObject_GetAttrString(callable, (char*)"__code__");
        if (fc) {
            PyObject* ac = PyObject_GetAttrString(fc, (char*)"co_argcount");
            if (ac) {
                const long numParameters = PyLong_AsLong(ac);
                if (withIndObj) {
                    if (numParameters == 2) return true;
                } else {
                    if (numParameters == 1 || numParameters == 2) return true;
                }
            }
        }
    }

    return false;
}

/*
    Run a function on an Item with no argument
    If the function accepts an argument, this will pass the "None" object
*/
std::string Item::runVerb(std::string verb)
{
    if (hasVerb(verb, true)) {
        PyObject* returnString = PyObject_CallMethodObjArgs(pyItem, PyUnicode_FromString(verb.c_str()), Py_None, NULL);
        std::string ret(getStringFromPyObject(returnString));
        return ret;
    } else if (hasVerb(verb, false)) {
        PyObject* returnString = PyObject_CallMethod(pyItem, verb.c_str(), NULL);
        std::string ret(getStringFromPyObject(returnString));
        return ret;
    }
    return "";
}

/*
    Run a function on an Item while passing in another item
*/
std::string Item::runVerb(std::string verb, Item* indirectObject)
{
    if (hasVerb(verb, true)) {
        PyObject* returnString = PyObject_CallMethodObjArgs(pyItem, PyUnicode_FromString(verb.c_str()), indirectObject->getPyItem(), NULL);
        std::string ret(getStringFromPyObject(returnString));
        return ret;
    }
    return "";
}

/*
    Returns true if the itemName is an alias for the item. Case insensitive
*/
bool Item::hasAlias(std::string itemName)
{
    itemName = lowercase(itemName);
    PyObject* aliasList = PyObject_GetAttrString(pyItem, (char*)"aliases");
    if (PyList_Check(aliasList))
    {
        Py_ssize_t listSize = PyList_Size(aliasList);
        for (Py_ssize_t i = 0; i < listSize; i++)
        {
            PyObject* aliasString = PyList_GetItem(aliasList, i);
            const char* alias = getStringFromPyObject(aliasString);
            std::string aliasStr(alias);
            aliasStr = lowercase(aliasStr);
            if (itemName.compare(alias) == 0)
            {
                return true;
            }
        }
    }
    return false;
}

/*
    Returns true if item is visible to player
*/
bool Item::isVisible()
{
    PyObject* visibleFlag = PyObject_GetAttrString(pyItem, (char*)"visible");
    assertThat(PyBool_Check(visibleFlag), "Error! visible is not a boolean");
    if (PyObject_IsTrue(visibleFlag)) return true;
    else return false;
}

/*
    Returns true if the item can be accessed anywhere in the game without being in the player's inventory
    Does not work for doors
*/
bool Item::isGlobal()
{
    PyObject* globalFlag = PyObject_GetAttrString(pyItem, (char*)"globalAccess");
    assertThat(PyBool_Check(globalFlag), "Error! globalAccess is not a boolean");
    if (PyObject_IsTrue(globalFlag)) return true;
    else return false;
}

/*
    Check if this item is a door
*/
bool Item::isDoor()
{
    return doorObj;
}

/*
    If this is true, there was more than 1 result when looking for an item and all other function calls on the item will cause segfault
*/
bool Item::isDuplicate()
{
    return duplicate;
}