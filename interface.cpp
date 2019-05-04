/* filename: interface.cpp
 * description: ncurses user interface for TBA3 Capstone project
 * version: 2019-05-03.1
 * compile: g++ interface.cpp -o uiinit -lncurses: test run with uiinit
 * author: Adam Deaton
 */

#include "interface.hpp"

/* createNewWin function takes four parameters and produces a box on screen
 * parameters: height of box, width of box, starting top right corner y-coordinates, starting top right x-coordinates
 * returns: ncurses WINDOW
*/
WINDOW *createNewWin(int h, int w, int y, int x){
	WINDOW *newBoxWin; // Create a local window to be drawn

	newBoxWin = newwin(h,w,y,x); // make new window
	wborder(newBoxWin,'|', '|','-','-','+','+','+','+'); // make box with characters for horizontal and vertical lines
	wrefresh(newBoxWin);

	return newBoxWin;
}

WINDOW *createNewOutput(int h, int w, int y, int x){
	WINDOW *newBoxWin; // Create a local window to be drawn

	newBoxWin = newwin(h,w,y,x); // make new window
	wborder(newBoxWin,' ', ' ',' ',' ',' ',' ',' ',' '); // make box with characters for horizontal and vertical lines
	wrefresh(newBoxWin);

	return newBoxWin;
}

//Opening TBA3 Game Intro Window
void introWindow(){
	WINDOW *intro;
	initscr();
        	
	intro = createNewOutput(LINES/2,COLS/2,LINES/4,COLS/4);
	mvwprintw(intro,2,2,"COCKTAIL HEIST\n");
	wrefresh(intro);
	sleep(1);
	mvwprintw(intro,8,2,"You are a mobster on a mission to sneak into the CEO of Old Money Corporation's mansion steal the wealth within and get out undetected. If you don't get enough loot, the boss will be angry. You know what happened to the last guy that made Big Al mad...\n");
	wrefresh(intro);
	wgetch(intro);

	sleep(1);
	
	clear();
	endwin();
}

//Graphic bordered window
void graphicWin(){
	WINDOW *graphic;
	int xCoord = 0, yCoord = 2, height = LINES - 2, width = COLS / 2;
	createNewWin(height, width, yCoord, xCoord);

}


//Graphics output window
WINDOW *graphicOutput(){
	WINDOW *graphicOut;
	int xCoord = 1, yCoord = 3, height = LINES - 4, width = (COLS / 2) - 2;
	return graphicOut = createNewOutput(height, width, yCoord, xCoord);

}

//Description bordered window
void *descriptionWin(){
	WINDOW * desWin;
	int xCoord = (COLS / 2) - 1, yCoord = 2, height = LINES - 10, width = (COLS / 2) + 1;
	createNewWin(height,width,yCoord,xCoord);
}

//Description output window
WINDOW *descriptionOutput(){
	WINDOW * desOutput;
	int xCoord = (COLS / 2), yCoord = 3, height = LINES - 9, width = (COLS / 2) - 1;
	return desOutput = createNewOutput(height,width,yCoord,xCoord);
}

//Room Items bordered window
void *itemsWin(){
	WINDOW * itemWin;
	int xCoord = (COLS / 2) - 1, yCoord = LINES - 16, height = 5, width = (COLS / 2) + 1;
	createNewWin(height,width,yCoord,xCoord);
}

//Room items output window
WINDOW *itemsOutput(){
	WINDOW * itemOutput;
	int xCoord = (COLS / 2), yCoord = LINES - 15, height = 3, width = (COLS / 2) - 1;
	return itemOutput = createNewOutput(height,width,yCoord,xCoord);
}


//Room Doors bordered window
void *doorsWin(){
	WINDOW * doorsWin;
	int xCoord = (COLS / 2) - 1, yCoord = LINES - 12, height = 4, width = (COLS / 2) + 1;
	createNewWin(height,width,yCoord,xCoord);
}

//Room doors output window
WINDOW *doorsOutput(){
	WINDOW * doorsOutput;
	int xCoord = (COLS / 2), yCoord = LINES - 11, height = 2, width = (COLS / 2) - 1;
	return doorsOutput = createNewOutput(height,width,yCoord,xCoord);
}

//Game State Windows showing user items and current score
WINDOW *gameStateWin(){
	WINDOW *stateWin;
	int xCoord = 0, yCoord = 0, height = 3, width = COLS;
	return stateWin = createNewWin(height,width,yCoord,xCoord);

}

WINDOW *scoreOutput(){
	WINDOW *stateOut;
	int xCoord = (COLS / 6) * 5, yCoord = 1, height = 1, width = (COLS / 6) - 1;
	return stateOut = createNewOutput(height,width,yCoord,xCoord);

}


//Input window
void *inputWin(){
	WINDOW *inWin;
	int xCoord = (COLS / 2) - 1, yCoord = LINES - 9, height = 9, width = (COLS / 2) + 1;
	createNewWin(height,width,yCoord,xCoord); 
}

//Input screen for commands
WINDOW *inputScr(){
	WINDOW *input;
	int xCoord = (COLS / 2), yCoord = LINES - 8, height = 7, width = (COLS / 2) - 1;
	return input = createNewOutput(height,width,yCoord,xCoord); 
}
//TBD function may not need
/*
void itemsWin(){
	
}
*/


/*Display Current Room or Item Description, game state, input window, graphic of room or item
* Parameters: cppString cppDescription
*/
std::string  gameUI(int roomID, std::string roomName, std::string cppDes, std::string userItems[MAXITEM], int numItems, std::string itemsInRoom[MAXITEM], int numItemsInRoom, int score){
	std::string cppString;
	char cDes[cppDes.size() + 1]; //c string to hold cppDes cpp string
	strcpy(cDes, cppDes.c_str()); //copy cppDes into cDes for output with ncurses;
	char cRoomName[roomName.size() + 1]; 
	strcpy(cRoomName, roomName.c_str()); //copy cppString contents int c string
	//Move cpp user items strings into c string char array
	char cUserItems[numItems][32]; //char array of user held items
	for(int i = 0; i < numItems; i++){ 
		strcpy(cUserItems[i], userItems[i].c_str()); //Copy each item name into char array
	}
	//Move cpp items strings into c string char array
	char cItemsInRoom[numItemsInRoom][32];
	for(int i = 0; i < numItemsInRoom; i++){
		strcpy(cItemsInRoom[i], itemsInRoom[i].c_str());
	}
	int strlength = 0;  //to track string lengths in output windows
	//Initialize ncurses
	initscr();
	WINDOW *desOutput;
	WINDOW *roomItemsWin;
	WINDOW *doorsOut;
	WINDOW *stateWin;
	WINDOW *scoreOut;
	WINDOW *graphicOut;
	WINDOW *input;
	char inputStr[256]; //C-string for input
	memset(inputStr,'\0',256);
	//Load game windows
	stateWin = gameStateWin(); // show user held items and current score
	scoreOut = scoreOutput();
	graphicWin(); // show room graphics
	graphicOut = graphicOutput(); // graphic output window
	descriptionWin(); // room description window bordered
	desOutput = descriptionOutput(); //output room description
	itemsWin();
	roomItemsWin = itemsOutput();
	doorsWin();
	doorsOut = doorsOutput();
	inputWin(); //input window bordered
	input = inputScr(); //game waits for input
	mvwprintw(desOutput, 0, 0, "%s\n%s", cRoomName, cDes);
	wrefresh(desOutput);
	//Will need to loop items from array
	mvwprintw(stateWin, 1, 1,"Items: ");
	//Print all user held items
	strlength = 8; //1 + Items: 
	for(int i = 0; i < numItems; i++){
		mvwprintw(stateWin, 1, strlength,"%s ", cUserItems[i]);
		strlength = strlength + strlen(cUserItems[i]) + 1;
	}	
	wrefresh(stateWin); // Refresh stateWin to display items
	mvwprintw(scoreOut, 0,0,"Score: %d",score);
	wrefresh(scoreOut);	
	mvwprintw(roomItemsWin, 0, 0, "Items in room: ");
	wrefresh(roomItemsWin);
	//Print all items in room
	strlength = 16; //1 + Items in room:
	for(int i = 0; i < numItemsInRoom; i++){
		mvwprintw(roomItemsWin, 0, strlength,"%s, ", cItemsInRoom[i]);
		strlength = strlength + strlen(cItemsInRoom[i]) + 2; //strlength is equal to previous strings and ,+space
	}	
	wrefresh(roomItemsWin);
	//Output doors available in room
	mvwprintw(doorsOut, 0, 0, "Doors in room: ");
	wrefresh(doorsOut);
	mvwprintw(input, 0,0,"What would you like to do? ");
	wrefresh(input);
	wgetstr(input, inputStr); //Get string from user
	cppString = inputStr;
	//Remove this is to test input
	mvwprintw(graphicOut,0,0,"%s",inputStr);
	wrefresh(graphicOut);
	//This is to test input remove above
	//wgetch(input); //Any key to exit
	sleep(1);
	endwin(); //end curses mode
	return cppString;

}
/*
//Main for testing interface
int main(){
	std::string input;
	std::string description; // room or item description
	int  score;
	std::string userItems[MAXITEM];
	std::string roomItems[MAXITEM];
	std::string roomName;
	int roomID;
	description = "This upstairs bedroom has blue walls and oak wood floor. There are two windows to the south letting in natural light. In the center of the room on the west wall there is a queen sized bed with a gray spread. On the east wall there is a dresser and mirror.\n"; 
	roomID = 1;
	roomName = "Bedroom";
	score = 5500;
	userItems[0] = "Hammer";
	userItems[1] = "Key";
	userItems[2] = "Ring"; 

	roomItems[0] = "Bottle of Red Wine";
	roomItems[1] = "Backpack";
	roomItems[2] = "Sword"; 
	introWindow();
	while(1){
		input = gameUI(roomID, roomName, description, userItems,3, roomItems, 3, score);
		std::cout << input << std::endl;
	}
	return 0;
}*/
