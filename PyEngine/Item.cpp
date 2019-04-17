#include <Python.h>
#include "Item.h"
#include "PyEngine.h"

/*
    Create an Item - a wrapper around an Item class made in Python
*/
Item::Item(PyObject* _pyItem)
{
    pyItem = _pyItem;
}

PyObject* Item::getPyItem()
{
    return pyItem;
}

/*
    Get the "description" property of the item as a string
*/
char* Item::getDescription()
{
    return getStringFromPyObject(pyItem, (char*)"description");
}

/*
    Check if an item has a verb defined
*/
bool Item::hasVerb(char* verb)
{
    PyObject* callable = PyObject_GetAttrString(pyItem, verb);
    return PyCallable_Check(callable);
}

/*
    Run a function on an Item
*/
void Item::runVerb(char* verb)
{
    PyObject_CallMethod(pyItem, verb, NULL);
}

/*
    Run a function on an Item while passing in another item
*/
void Item::runVerb(char* verb, Item* indirectObject)
{
    PyObject_CallMethodObjArgs(pyItem, PyUnicode_FromString(verb), indirectObject->getPyItem(), NULL);
}