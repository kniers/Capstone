/****************************************************
 * Name: Command.hpp
 * Author: Collin Zurbrugg
 * Description: The header file for the Command class
****************************************************/

#ifndef COMMAND_HPP
#define COMMAND_HPP

#include <string>

class Command {
public:
    std::string verb;
    std::string dirObj;
    std::string indObj;
    char direction; //{n, s, e, w}

    /*******************
    * status * meaning *
    ********************
    * 0      * no error*
    * 1	     * error   *
    *******************/
    int status;

    Command(){
	direction = 0;
	verb = "NULL";
	dirObj = "NULL";
	indObj = "NULL";
    }
};

#endif
