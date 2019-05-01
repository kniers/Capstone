#include <Python.h>
#include <vector>
#include "Item.h"
#include "Room.h"
#include "PyEngine.h"

/*
    Create a room - a wrapper around a room class made in Python
*/
Room::Room(PyObject* _pyRoom)
{
    pyRoom = _pyRoom;
}

/*
    For internal access - get the Python version
*/
PyObject* Room::getPyRoom()
{
    return pyRoom;
}

/*
    Get the "name" attribute of a room
*/
std::string Room::getName()
{
    std::string name(strdup(getStringFromPyObject(pyRoom, (char*)"name")));
    return name;
}

/*
    Get the "description" property of the room as a string
*/
/*const char* Room::getDescription()
{
    return getStringFromPyObject(pyRoom, (char*)"description");
}*/

/*
    Call the "enterRoom" function
*/
PyObject* Room::callEnter()
{
    PyObject* callable = PyObject_GetAttrString(pyRoom, (char*)"enterRoom");
    assertThat(PyCallable_Check(callable), "Room attribute \"enterRoom\" must be a function!");
    return PyObject_CallFunction(callable, NULL);
}

/*
    Get the "visible" attribute of the room
*/
bool Room::isVisible()
{
    PyObject* visibleFlag = PyObject_GetAttrString(pyRoom, (char*)"visible");
    assertThat(PyBool_Check(visibleFlag), "Error! visible is not a boolean");
    if (PyObject_IsTrue(visibleFlag)) return true;
    else return false;
}

/*
    Check if the input string is an alias of the room. Case insensitive
*/
bool Room::hasAlias(std::string roomName)
{
    roomName = lowercase(roomName);
    PyObject* aliasList = PyObject_GetAttrString(pyRoom, (char*)"aliases");
    assertThat(PyList_Check(aliasList), "Error! aliases must be a list");

    Py_ssize_t listSize = PyList_Size(aliasList);
    for (Py_ssize_t i = 0; i < listSize; i++)
    {
        PyObject* aliasString = PyList_GetItem(aliasList, i);
        const char* alias = getStringFromPyObject(aliasString);
        std::string aliasStr(alias);
        aliasStr = lowercase(aliasStr);
        if (roomName.compare(alias) == 0)
        {
            return true;
        }
    }
    
    return false;
}

/*
    Get a copy of the items list for the room
*/
std::vector<Item*> Room::getItems()
{
    PyObject* itemList = PyObject_GetAttrString(pyRoom, (char*)"items");
    assertThat(PyList_Check(itemList), "Error! items must be a list of item names!");
    
    std::vector<Item*> items;

    Py_ssize_t size = PyList_Size(itemList);
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject* itemName = PyList_GetItem(itemList, i);
        const char* itemNameStr = getStringFromPyObject(itemName);
        Item* item = PyEngine::getInstance()->getItemByName(itemNameStr);
        assertThat((item != NULL), "Error! Item in room not found");
        items.push_back(item);
    }

    return items;
}

/*
    Get a list of doors in the room
*/
std::vector<Item*> Room::getDoors()
{
    PyObject* doorDict = PyObject_GetAttrString(pyRoom, (char*)"doors");
    assertThat(PyDict_Check(doorDict), "Error! doors must be a dictionary");
    PyObject* doorList = PyDict_Values(doorDict);

    std::vector<Item*> doors;

    Py_ssize_t size = PyList_Size(doorList);
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject* doorName = PyList_GetItem(doorList, i);
        const char* doorNameStr = getStringFromPyObject(doorName);
        Item* door = PyEngine::getInstance()->getItemByName(doorNameStr);
        assertThat((door != NULL), "Error! Door in room not found");
        doors.push_back(door);
    }

    return doors;
}

/*
    Flag the room as visited by the player
*/
void Room::setVisited()
{
    PyObject_SetAttrString(pyRoom, (char*)"visited", Py_True);
    PyObject_SetAttrString(pyRoom, (char*)"visible", Py_True);
}