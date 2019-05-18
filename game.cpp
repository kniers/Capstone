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
        // Refresh info to display on UI

        // Current room
        Room* currentRoom = eng->getCurrentRoom();

        // Current score
        long score = eng->getScore();

        // Inventory list
        inventorySize = inventory->size();
        auto inventoryItr = inventory->begin();
        int inventoryIndex = 0;
        while (inventoryItr != inventory->end()) {
            inventoryItems[inventoryIndex] = (*inventoryItr)->getName();
            inventoryItr++;
            inventoryIndex++;
        }

        // Obvious exits. Only displays the direction of doors that are visible in the room
        vector<string> doors = currentRoom->getDirections();
        doorsInRoomSize = doors.size();
        auto doorsItr = doors.begin();
        int doorIndex = 0;
        while (doorsItr != doors.end()) {
            doorsInRoom[doorIndex] = *doorsItr;
            doorsItr++;
            doorIndex++;
        }

        // Items that were dropped by the player
        vector<Item*> droppedItemsVector = currentRoom->getDroppedItems();
        droppedItemsSize = droppedItemsVector.size();
        auto droppedItr = droppedItemsVector.begin();
        int droppedIndex = 0;
        while (droppedItr != droppedItemsVector.end()) {
            droppedItems[droppedIndex] = (*droppedItr)->getName();
            droppedItr++;
            droppedIndex++;
        }

        // Show different room name if in debug mode
        if (debugMode) {
            roomName = "debug";
        } else {
            roomName = currentRoom->getName();
        }

        // Update UI
        string input = gameUI(0, roomName, description, inventoryItems, inventorySize, droppedItems, droppedItemsSize, doorsInRoom, doorsInRoomSize, score);

        // Handle high level commands
        if (input.compare("quit") == 0 || input.compare("exit") == 0) exit(1); // exit game
        if (input.compare("debug") == 0 && !debugMode) { // Enter debug mode
            debugMode = true;
        }
        if (debugMode && input.compare("python") == 0) { // Enter python console from debug mode
            debugConsole = true;
        }
        if (!debugMode && input.compare("look") == 0) {
            description = eng->getItemByName("room")->runVerb("look");
            continue;
        }
        if (!debugMode && input.compare("help") == 0) {
            description = "Here's where I'd put a help menu. IF I HAD ONE!";
            continue;
        }
        if (input.compare("loadgame") == 0) {
            eng->loadGame();
            description = eng->getItemByName("room")->runVerb("look");
            continue;
        } else if (input.compare("savegame") == 0) {
            eng->saveGame();
            description += "\n\nGame saved";
            continue;
        }

        // Normal route
        if (!debugMode) {
            delete command; // Parser doesn't reset comman between calls
            Command* command = new Command();
            command->status = 0; // uninitialized unless this is here
            parseIt(input, command); // Call text parser

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
                description = command->errMessage;
            }
        } else {
            // Debug mode
            if (debugConsole) {
                if (input.compare("python") == 0) {
                    description = "PYTHON CONSOLE\nAll input will be interpreted as Python code. To go back to debug mode, type \".exit\"";
                } else if (input.compare(".exit") == 0) {
                    debugConsole = false;
                    description = "DEBUG MODE\nend - end debug mode\nhelp - print help menu\nrooms - print out room names\nitems - print out item names\ndoors - print out door names\n<room name> - details on a room\n<item or door name> - details on an item\npython - run python code";
                } else {
                    bool success = eng->debugConsole(input);
                    if (success) {
                        description = "PYTHON CONSOLE\nAll input will be interpreted as Python code. To go back to debug mode, type \".exit\"";
                    }
                    else {
                        description = "An error occurred. See err.txt for details. Type \".exit\" to exit python console";
                    }
                }
            } else {
                if (input.compare("debug") == 0 || input.compare("help") == 0) {
                    description = "DEBUG MODE\nend - end debug mode\nhelp - print help menu\nrooms - print out room names\nitems - print out item names\ndoors - print out door names\n<room name> - details on a room\n<item or door name> - details on an item\npython - run python code";
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
}
