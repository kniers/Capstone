#ifndef ITEM_H
#define ITEM_H

#include <Python.h>

class Item
{
private:
    PyObject* pyItem;

public:
    // Constructor and direct accessor should only be called by PyEngine classes
    Item(PyObject* _pyItem);
    PyObject* getPyItem();

    /*
        C++ Accessors
    */
    char* getDescription(); // Example. This might change later
    bool hasVerb(char* verb);
    void runVerb(char* verb);
    void runVerb(char* verb, Item* indirectObj);
};

#endif