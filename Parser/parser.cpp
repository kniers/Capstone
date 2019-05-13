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

    std::stringstream tokenStream;
    std::string token;
    std::string firstWord;
    tokenStream << parseMe;

    bool twoWords = false;
    bool hasPrep = false;

    //get first token
    getline(tokenStream, token, ' ');

    //ignore "the"
    if (token.compare("the") == 0){
	if (!getline(tokenStream, token, ' ')){
	    com->status = 1;
	    com->errMessage = "You've said nothing of value.";
	    return com;
	}
    }

    //is it a valid door/item?
    if (aahhhh->getAccessibleItem(token) != NULL){
	//check for ambiguous items
	if (aahhhh->getAccessibleItem(token)->isDuplicate() == true){
	    com->errMessage = "Which " + token + "?";
	    com->status = 1;
	    return com;
	}
	//if direction item, save direction
	if (token.compare("north") == 0 ||
	     token.compare("south") == 0 ||
	     token.compare("east") == 0 ||
	     token.compare("west") == 0) {
	    com->direction = token.at(0);
	}

	com->verb = "nope"; //no verb = describe item/enter door
	com->dirObj = aahhhh->getAccessibleItem(token);
	com->indObj = NULL;
	com->dirDoorFlag = com->dirObj->isDoor();
    }
    //else is it a valid verb
    else if (aahhhh->getVerb(token).compare("") != 0){
	//save token as verb
	com->verb = aahhhh->getVerb(token);
    }
    //if we don't recognize the token, we assume
    //it's the first word of a two word item
    else {
	twoWords = true;
	firstWord = token;
    }

    //get rest of tokens
    while (getline(tokenStream, token, ' ')){
	//ignore "the"
	if (token.compare("the") == 0){
	    continue;
	}

	//combine two-word things into one token
	if (twoWords == true){
	    //twoWords = false;
	    token = firstWord + " " + token;
	}
	//a verb will always be the first word,
	//so if we have another verb, error
	if (aahhhh->getVerb(token).compare("") != 0){
	    //print error
	    com->errMessage = "I don't understand that command. Make sure any action begins your command.";
	    com->status = 1;
	    return com;
	}
	//is it an item?
	else if (aahhhh->getAccessibleItem(token) != NULL){
	    if (twoWords == true)
		twoWords = false;

	    //check for duplicate item
	    Item* addMe = aahhhh->getAccessibleItem(token);
	    if (addMe->isDuplicate() == true){
	        if (addMe->isDoor() == false || com->direction == 0){
		    com->errMessage = "Which one?";
		    com->status = 1;
		    return com;
		}
	    }
	    //make sure we have only one door
	    if (addMe->isDoor() == true){
		if (com->direction == 0){
		    //if we already have a door
		    if (com->indDoorFlag == true || com->dirDoorFlag == true){
			com->status = 1;
			com->errMessage = "You can only have one door in a command!";
			return com;
		    }
		    //otherwise we are good
		}
		//if there is a direction, first door has already been recorded
		else {
		    continue;
		    //FIXME: what about second door?
		}
	    }

	    //update direction if necessary
	    if (token.compare("north") == 0 ||
	        token.compare("south") == 0 ||
	        token.compare("east") == 0 ||
	        token.compare("west") == 0) {
	        if (com->direction == 0) //if first direction
	            com->direction = token.at(0);
	        else {
	            //second direction means error
	            com->status = 1;
	            com->errMessage = "I don't understand that command. You listed two directions.";
	            return com;
	        }
	    }

	    //now that we've checked the object, we place it
	    //if our first object
	    if (com->dirObj == NULL){
		com->dirObj = addMe;
		com->dirDoorFlag = com->dirObj->isDoor();
	    }
	    //else if our second object
	    else if (com->indObj == NULL){
		//if <verb> <dirObj> <preposition> <indObj>,
		//save token as indirect object
		if (hasPrep == true){
		    com->indObj = addMe;
		    com->indDoorFlag = com->indObj->isDoor();
		}
		//otherwise, swap direct and indirect objects
		else {
		    //error because we don't like commands with
		    //two objects, a direction, and no preposition
		    if (com->direction != 0){
			com->status = 1;
			com->errMessage = "Huh?";
			return com;
		    }
		    com->indObj = com->dirObj;
		    com->indDoorFlag = com->dirDoorFlag;
		    com->dirObj = addMe;
		    com->dirDoorFlag = com->dirObj->isDoor();
		}
	    }
	    //if this is the third object, we have a problem
	    else {
		//print error
		com->errMessage = "I don't understand that command. Make sure you have at most two items in comands.";
		com->status = 1;
		return com;
	    }
	}
        //else check for preposition or two word things
        else {
	    //FIXME: deal with too many prepositions

	    //We can associate prepositions with particular verbs
	    //later, but it may be uneccessary. Sometimes the
	    //illusion of an intelligent program is sufficient.
	    if (token.compare("with") == 0)
	    	hasPrep = true;
	    else if (token.compare("to") == 0)
		hasPrep = true;
	    else if (token.compare("at") == 0)
		hasPrep = true;
	    else if (token.compare("on") == 0)
		hasPrep = true;
	    //FIXME: more prepositions
	    //if we don't recognize the word, assume we have two words
	    else if (twoWords == false){
		firstWord = token;
		twoWords = true;
	    }
	    //two uncaught words
	    else {
		com->errMessage = "There's a word in there I don't recognize.";
		com->status = 1;
		return com;
	    }
	}

    }

    //uncaught first word
    if (twoWords == true){
	com->errMessage = "There's a word in there I don't understand.";
	com->status = 1;
	return com;
    }

    //check for action with no object
    if (com->verb.compare("nope") != 0 && com->dirObj == NULL){
	com->errMessage = "I don't understand that command. Make sure actions have objects.";
	com->status = 1;
	return com;
    }

    return com;
}
