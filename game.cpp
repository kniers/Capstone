/*
    Main loop to get us started
*/
#include <iostream>
#include "PyEngine.h"
//#include "parser.hpp"
//#include "Command.hpp"

using namespace std;

int main()
{
    PyEngine* eng = PyEngine::getInstance();

    std::string verb;
    std::string object;
    std::string indirectObject;

    while (true) {
        std::cout << std::endl;

        std::cout << "verb: ";
        std::getline(std::cin, verb);

        if (verb.compare("quit") == 0) exit(0);

        std::cout << "object: ";
        std::getline(std::cin, object);

        if (object.compare("quit") == 0) exit(0);

        std::cout << "indirect object: ";
        std::getline(std::cin, indirectObject); 

        std::cout << std::endl;

        Item* item = eng->getAccessibleItem(object);

        Item* indItem = NULL;
        if (indirectObject.length() > 0) {
            indItem = eng->getAccessibleItem(indirectObject);
        }

        if (indirectObject.length() > 0) {
            if (indItem == NULL) {
                std::cout << "Indirect object not recognized" << std::endl;
                continue;
            } else if (indItem->isDuplicate()) {
                std::cout << "Which " << indirectObject << "?" << std::endl;
                continue;
            }
        }
        
        if (item == NULL) {
            std::cout << "Object not recognized" << std::endl;
            continue;
        } else if (item->isDuplicate()) {
            std::cout << "Which " << object << "?" << std::endl;
            continue;
        } else {
            if (verb.length() > 0) {
                std::string officialVerb = eng->getVerb(verb);
                if (officialVerb.length() > 0) {
                    if (indItem == NULL && item->hasVerb(officialVerb, false)) {
                        std::cout << item->runVerb(officialVerb);
                    } else if (indItem != NULL && item->hasVerb(officialVerb, true)) {
                        std::cout << item->runVerb(officialVerb, indItem);
                    } else {
                        std::cout << "Doesn't have verb" << std::endl;
                        continue;
                    }
                } else {
                    std::cout << "Verb not recognized" << std::endl;
                    continue;
                }
            } else {
                if (item->isDoor()) {
                    std::cout << item->runVerb("go") << std::endl;
                } else {
                    std::cout << item->runVerb("look") << std::endl;
                }
            }
        }

        std::cout << std::endl;
    }
}