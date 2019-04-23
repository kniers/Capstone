#include <Python.h>
#include "Room.h"
#include "PyEngine.h"

/*
    Create a room - a wrapper around a room class made in Python
*/
Room::Room(PyObject* _pyRoom)
{
    pyRoom = _pyRoom;
}

PyObject* Room::getPyRoom()
{
    return pyRoom;
}

/*
    Get the "description" property of the room as a string
*/
const char* Room::getDescription()
{
    return getStringFromPyObject(pyRoom, (char*)"description");
}

/*
    If room has an "enter" function, call it
*/
void Room::callEnter()
{
    PyObject* callable = PyObject_GetAttrString(pyRoom, (char*)"enter");
    if (PyCallable_Check(callable))
    {
        PyObject_CallFunction(callable, NULL);
    }
}