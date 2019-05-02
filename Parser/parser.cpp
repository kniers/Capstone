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
 * Example: "taco" (describes taco)
 * (3) <verb> <dirObj> (preposition) <indObj>
 * Example: "show taco to Alice"
 * (4) <verb> <indObj> <dirObj>
 * Example: "give Alice taco"
 * (5) <direction>
 * Example: "north"
 * (6) <verb> <direction>
 * Example: "go north"
 * (7) <direction> <dirObj>
 * Example: "north door"
 * (8) <verb> <direction> <dirObj>
 * Example: "open north door"
 * (9) <verb> <direction> <dirObj> (prep) <indObj>
 * Example: "open north door with key"
****************************************/

Command* parseIt(std::string parseMe, Command* com){

    PyEngine* aahhhh = PyEngine::getInstance();

    //FIXME: make all lowercase
    std::stringstream tokenStream;
    std::string token;
    tokenStream << parseMe;

    bool twoWords = false;
    bool hasPrep = false;

    //get first token
    getline(tokenStream, token, ' ');

    //is it a valid door/item?
    if (aahhhh->getItemByName(token) != NULL){
	com->verb = "nope"; //no verb = describe item/enter door
	com->dirObj = aahhhh->getItemByName(token);
	com->indObj = NULL;
	com->dirDoorFlag = com->dirObj->isDoor();
	//FIXME: check for two words
    }
    //else is it a valid direction
    else if (token.compare("north") == 0 ||
	     token.compare("south") == 0 ||
	     token.compare("east") == 0 ||
	     token.compare("west") == 0) {
	com->direction = token.at(0);
    }
    //else is it a valid verb
    else if (aahhhh->getVerb(token).compare("") != 0){
	//save token as verb
	com->verb = aahhhh->getVerb(token);
	//FIXME: check for two words
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
	//If the verb is not filled in, then we have a command of format
	//<dirObj>. If this is the case, then we shouldn't have any more
	//tokens, and therefore shouldn't have entered this loop.
	else if (com->verb.compare("nope") == 0){
	    //print error
	    cout << "I don't understand that command\n";
	    cout << "If you're not examining an object, make sure you have an action in your command.\n";
	    com->status = 1;
	    return com;
	}
	//else is it a valid direction
	else if (token.compare("north") == 0 ||
	         token.compare("south") == 0 ||
	         token.compare("east") == 0 ||
	         token.compare("west") == 0) {
	    if (com->direction == 0) //if first direction
		com->direction = token.at(0);
	    else {
		//second direction means error
		com->status = 1;
		cout << "I don't understand that command\n";
		cout << "You listed two directions.\n";
		return com;
	    }
	}
	//is it an item?
	else if (aahhhh->getItemByName(token) != NULL){
	    //if direct object is blank
	    if (com->dirObj == NULL){
		com->dirObj = aahhhh->getItemByName(token);
		com->dirDoorFlag = com->dirObj->isDoor();
	    }
	    else if (com->indObj == NULL){
		//if <verb> <dirObj> <preposition> <indObj>,
		//save token as indirect object
		if (hasPrep == true){
		    com->indObj = aahhhh->getItemByName(token);
		    com->indDoorFlag = com->indObj->isDoor();
		}
		//otherwise, swap direct and indirect objects
		else {
		    //error because there's no valid command with
		    //two objects, a direction, and no preposition
		    if (com->direction != 0){
			com->status = 1;
			cout << "Huh?\n";
			return com;
		    }
		    com->indObj = com->dirObj;
		    com->indDoorFlag = com->dirDoorFlag;
		    com->dirObj = aahhhh->getItemByName(token);
		    com->dirDoorFlag = com->dirObj->isDoor();
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
	    //FIXME: more prepositions
	    else {
		cout << "There's a word in there I don't recognize\n";
		com->status = 1;
		return com;
	    }
	}

	//check for action with no object
	if (com->verb.compare("nope") != 0 && com->dirObj == NULL){
	    cout << "I don't understand that command\n";
	    cout << "Make sure actions have objects\n";
	    com->status = 1;
	    return com;
	}
    }

    return com;
}
