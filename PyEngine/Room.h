#ifndef ROOM_H
#define ROOM_H

#include <Python.h>
#include <vector>
#include "Item.h"


class Room
{
private:
    PyObject* pyRoom;

public:
    // Constructor and direct accessor should only be called by PyEngine classes
    Room(PyObject* _pyRoom);
    PyObject* getPyRoom();

    /*
        C++ Accessors
    */
    std::string getName();
    //const char* getDescription();
    PyObject* callEnter(); // Call enterRoom function
    bool isVisible();
    bool hasAlias(std::string roomName);
    std::vector<Item*> getItems();
    std::vector<Item*> getDoors();
    void setVisited();
};

#endif