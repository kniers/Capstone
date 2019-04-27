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

    //FIXME: make all lowercase
    std::stringstream tokenStream;
    std::string token;
    tokenStream << parseMe;

    bool twoWords = false;
    bool hasPrep = false;

    std::string addMe;

    //get first token
    getline(tokenStream, token, ' ');

    //is it a valid object/door?
    addMe = getAccessibleItem(token)->name; //FIXME: function name
    if (addMe.compare("NULL") == 0)
	addMe = getAccessibleDoor(token)->name; //FIXME: function name
    if (addMe.compare("NULL") != 0){
	com->verb = "nope"; //no verb = describe item/enter door
	com->dirObj = addMe;
	com->indObj = "NULL";
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
    else if (getVerb(token) != NULL){//FIXME: getVerb return value
	//save token as verb
	com->verb = getVerb(token);
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
	    if (com->direction == 0)
		com->direction = token.at(0);
	    else {
		com->status = 1;
		cout << "I don't understand that command\n";
		cout << "You listed two directions.\n";
		return com;
	    }
	}
	//is it an item?
	else if (getAccessibleItem(token) != NULL ||
			getAccessibleDoor(token) != NULL){//FIXME: change l8r
	    //if direct object is blank
	    if (com->dirObj.compare("NULL") == 0){
		com->dirObj = token;
	    }
	    else if (com->indObj.compare("NULL") == 0){
		//if <verb> <dirObj> <preposition> <indObj>,
		//save token as indirect object
		if (hasPrep == true)
		    com->indObj = token;
		//otherwise, swap direct and indirect objects
		else {
		    if (com->direction != 0){
			com->status = 1;
			cout << "Huh?\n";
			return com;
		    }
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
	    else {
		cout << "There's a word in there I don't recognize\n";
		com->status = 1;
		return com;
	    }
	}

	//check for other errors
	if (com->verb.compare("nope") != 0 && com->dirObj.compare("NULL") == 0){
	    cout << "I don't understand that command\n";
	    cout << "Make sure actions have objects\n";
	    com->status = 1;
	    return com;
	}
    }

    return com;
}
