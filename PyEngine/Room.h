#ifndef ROOM_H
#define ROOM_H

#include <Python.h>

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
    char* getDescription(); // Example. This might change later
    void callEnter(); // Example. This might change later
};

#endif