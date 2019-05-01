#ifndef ITEM_H
#define ITEM_H

#include <Python.h>
#include <string>

class Item
{
private:
    PyObject* pyItem;
    bool doorObj;
    bool duplicate;

public:
    // Constructor and direct accessor should only be called by PyEngine classes
    Item(PyObject* _pyItem, bool door, bool duplicate);
    PyObject* getPyItem();

    /*
        C++ Accessors
    */
    std::string getName();
    //const char* getDescription();
    bool hasVerb(std::string verb, bool withIndObj);
    std::string runVerb(std::string verb);
    std::string runVerb(std::string verb, Item* indirectObj);
    bool hasAlias(std::string itemName);
    bool isVisible();
    bool isGlobal();
    bool isDoor();
    bool isDuplicate(); // If this is true, all other function calls will cause segfault!
};

#endif