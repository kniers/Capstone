/**********************************************
 * Name: parser.cpp
 * Author: Collin Zurbrugg
 * Description: A text parser for a text-based
 * adventure game
**********************************************/

#include "parser.hpp"

using std::cout;

/****************************************
 * Valid command formats *
 * (1) <verb> <dirObj>
 * Example: "eat taco"
 * (2) <dirObj>
 * Example: "north" (goes north)
 * Example: "taco" (describes taco)
 * (3) <verb> <dirObj> (preposition) <indObj>
 * Example: "show taco to Alice"
 * (4) <verb> <indObj> <dirObj>
 * Example: "give Alice taco"
****************************************/

/*******************************************
 * Name: isVerb
 * Description: If a string is a valid verb,
 * returns the string or its base synonym.
 * Otherwise, returns "nope"
*******************************************/

std::string isVerb(std::string checkMe){
    //this is a placeholder function for now
    if (checkMe.compare("eat") != 0 && checkMe.compare("give") != 0)
	return "nope";

    return checkMe;
}

/*******************************************
 * Name: isItem
 * Description: If a string is a valid item,
 * returns the string.
 * Otherwise, returns "nope"
*******************************************/

std::string isItem(std::string checkMe){
    //this is a placeholder function for now
    if (checkMe.compare("taco") != 0 && checkMe.compare("Alice") != 0)
	return "nope";

    return checkMe;
}

Command* parseIt(std::string parseMe, Command* com){

    std::stringstream tokenStream;
    std::string token;
    tokenStream << parseMe;

    bool twoWords = false;
    bool hasPrep = false;


    //get first token
    getline(tokenStream, token, ' ');

    //is it a valid verb?
    if (isVerb(token).compare("nope") != 0){
	//save token as verb
	com->verb = token;
    }
    //else is it a valid object?
    else if (isItem(token).compare("nope") != 0){
	com->verb = "nope"; //no verb = describe item/enter door
	com->dirObj = token;
	com->indObj = "nope";
    }
    else {
	//print error
	cout << "I don't understand that command\n";
	cout << "Make sure your commands reference a valid item or action\n";
	com->status = 1;
	return com;
    }

    //get rest of tokens
    while (getline(tokenStream, token, ' ')){
	//skip the next token for two-word things
	if (twoWords == true){
	    twoWords = false;
	}
	//if the verb is not filled in, then we have a command of format
	//<dirObj>. If this is the case, then we shouldn't have any more tokens
	else if (com->verb.compare("nope") == 0){
	    //print error
	    cout << "I don't understand that command\n";
	    cout << "Actions are only allowed at the start of a command\n";
	    com->status = 1;
	    return com;
	}
	//is it an item?
	else if (isItem(token).compare("nope") != 0){
	    //if direct object is blank
	    if (com->dirObj.compare("null") == 0){
		com->dirObj = token;
	    }
	    else if (com->indObj.compare("null") == 0){
		//if <verb> <dirObj> <preposition> <indObj>,
		//save token as indirect object
		if (hasPrep == true)
		    com->indObj = token;
		//otherwise, swap direct and indirect objects
		else {
		    com->indObj = com->dirObj;
		    com->dirObj = token;
		}
	    }
	    //if this is the third object, we have a problem
	    else {
		//print error
		cout << "I don't understand that command\n";
		cout << "Make sure you have at most two items in commands\n";
		com->status = 1;
		return com;
	    }
	}
        //else check for preposition
        else {
	    //FIXME: deal with too many prepositions

	    //We can associate prepositions with particular verbs
	    //later, but it may be uneccessary. Sometimes the
	    //illusion of an intelligent program is sufficient.
	    if (token.compare("with") == 0)
	    	hasPrep = true;
	    else if (token.compare("to") == 0)
		hasPrep = true;
	}

	//check for other errors
	if (com->verb.compare("nope") != 0 && com->dirObj.compare("null") == 0){
	    cout << "I don't understand that command\n";
	    cout << "Make sure actions have objects\n";
	    com->status = 1;
	    return com;
	}
    }

    return com;
}
