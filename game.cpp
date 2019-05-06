/*
    Main loop to get us started
*/
#include <iostream>
#include "PyEngine.h"
#include "interface.hpp"
#include "parser.hpp"
#include "Command.hpp"

using namespace std;

int main()
{
    PyEngine* eng = PyEngine::getInstance();
    introWindow();

    string roomName = eng->getCurrentRoom()->getName();
    string description = eng->getItemByName("room")->runVerb("look");
    Command* command = NULL;
    string inventoryItems[MAXITEM];
    string droppedItems[MAXITEM];
    string doorsInRoom[MAXDOORS];
    int inventorySize = 0;
    int droppedItemsSize = 0;
    int doorsInRoomSize = 0;
    bool debugMode = false;
    bool debugConsole = false;

    vector<Item*>* inventory = eng->getInventory();

    // Main loop
    while (true) {
        //long score = eng->getScore(); // Getting the score causes a problem with error reporting. I'll fix it later
        long score = -1;
        inventorySize = inventory->size();
        auto inventoryItr = inventory->begin();
        int inventoryIndex = 0;
        while (inventoryItr != inventory->end()) {
            inventoryItems[inventoryIndex] = (*inventoryItr)->getName();
            inventoryItr++;
        }
        if (debugMode) {
            roomName = "debug";
        } else {
            roomName = eng->getCurrentRoom()->getName();
        }

        string input = gameUI(0, roomName, description, inventoryItems, inventorySize, droppedItems, droppedItemsSize, doorsInRoom, doorsInRoomSize, score);
        if (input.compare("quit") == 0) exit(1);
        if (input.compare("debug") == 0 && !debugMode) {
            debugMode = true;
        }
        if (debugMode && input.compare("python") == 0) {
            debugConsole = true;
        }

        if (!debugMode) {
            delete command; // Parser doesn't reset comman between calls
            Command* command = new Command();
            command->status = 0; // uninitialized unless this is here
            parseIt(input, command);

            // Success
            if (command->status == 0) {
                // Check if we can call the verb function
                if (command->dirObj == NULL) {
                    // If no object, assume current room
                    command->dirObj = eng->getItemByName("room");
                }

                // If duplicate item, return error message
                if (command->dirObj->isDuplicate()) {
                    description = "Which one?";
                    continue;
                }
                if (command->indObj != NULL && command->indObj->isDuplicate()) {
                    description = "Which one?";
                    continue;
                }

                // If verb invalid, assume "go" for doors and "look" for other items
                if (eng->getVerb(command->verb).compare("") == 0) {
                    if (command->dirObj->isDoor()) {
                        command->verb = "go";
                    } else {
                        command->verb = "look";
                    }
                }

                // If there is an indirect object
                if (command->indObj != NULL) {
                    // If dirObj can handle verb with an argument
                    if (command->dirObj->hasVerb(command->verb, true)) {
                        description = command->dirObj->runVerb(command->verb, command->indObj);
                    } else {
                        description = "That won't work";
                    }
                } else { // No indirect object
                    if (command->dirObj->hasVerb(command->verb, false)) {
                        description = command->dirObj->runVerb(command->verb);
                    } else {
                        description = "That won't work";
                    }
                }
            } else { // Failure from parser
                // Print error message from parser. Right now it goes to cout
                description = "-parser error-";
            }
        } else {
            // Debug mode
            if (debugConsole) {
                if (input.compare("python") == 0) {
                    description = "ENTERING PYTHON CONSOLE\nAll input will be interpreted as Python code. To go back to debug mode, type \".exit\"";
                } else if (input.compare(".exit") == 0) {
                    debugConsole = false;
                    description = "ENTERING DEBUG MODE\nend - end debug mode\nhelp - print help menu\nrooms - print out room names\nitems - print out item names\ndoors - print out door names\n<room name> - details on a room\n<item or door name> - details on an item\npython - run python code";
                } else {
                    eng->debugConsole(input);
                    description = "ENTERING PYTHON CONSOLE\nAll input will be interpreted as Python code. To go back to debug mode, type \".exit\"";
                }
            } else {
                if (input.compare("debug") == 0 || input.compare("help") == 0) {
                    description = "ENTERING DEBUG MODE\nend - end debug mode\nhelp - print help menu\nrooms - print out room names\nitems - print out item names\ndoors - print out door names\n<room name> - details on a room\n<item or door name> - details on an item\npython - run python code";
                } else if (input.compare("end") == 0) {
                    description = eng->getItemByName("room")->runVerb("look");
                    debugMode = false;
                }else if (input.compare("rooms") == 0) {
                    description = eng->debugRooms();
                } else if (input.compare("items") == 0) {
                    description = eng->debugItems();
                } else if (input.compare("doors") == 0) {
                    description = eng->debugDoors();
                } else {
                    Item* debugItem = eng->getItemByName(input);
                    Room* debugRoom = eng->getRoomByName(input);
                    if (debugItem != NULL) {
                        description = eng->debugItemDetails(input);
                    } else if (debugRoom != NULL) {
                        description = eng->debugRoomDetails(input);
                    } else {
                        description = "Did not recognize a command, room, or item";
                    }
                }
            }
        }
    }

    /* The first version, no UI or parser
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
    */
}