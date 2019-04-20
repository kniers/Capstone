/*
    Main loop to get us started
*/
#include <iostream>
#include "PyEngine.h"
#include "parser.hpp"
#include "Command.hpp"

using namespace std;

int main()
{
    PyEngine* eng = PyEngine::getInstance();
    Command* command = new Command();

    while (true)
    {
        string input;
        cin >> input;
        if (input.compare("quit") == 0) return 0;
        parseIt(input, command);

        if (command->status == 0)
        {
            Item* dirObj = eng->getAccessibleItem(command->dirObj.c_str());
            Item* indObj = eng->getAccessibleItem(command->indObj.c_str());
            if (dirObj != NULL && dirObj->hasVerb(command->verb.c_str()))
            {
                if (indObj != NULL)
                {
                    dirObj->runVerb(command->verb.c_str(), indObj);
                }
                else
                {
                    dirObj->runVerb(command->verb.c_str());
                }
            }
        }
    }
}