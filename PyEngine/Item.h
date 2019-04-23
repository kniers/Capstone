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
    const char* getDescription(); // Example. This might change later
    bool hasVerb(const char* verb);
    void runVerb(const char* verb);
    void runVerb(const char* verb, Item* indirectObj);
    bool hasAlias(const char* itemName);
    bool isVisible();
};

#endif