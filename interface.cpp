/* filename: interface.cpp
 * description: ncurses user interface for TBA3 Capstone project
 * version: 2019-05-17.1
 * compile: g++ interface.cpp -o uiinit -lncurses: test run with uiinit
 * author: Adam Deaton
 */

#include "interface.hpp"

/* printInWin takes a window and string and prints the string in the window while wrapping text
 * parameters: pointer to WINDOW, char array, width of message, and row to start printing on in window
 * returns: void
 */
void printInWin(WINDOW *win, char buf[MAXSTR], int width, int row){
	int col = 0;
	int prevWord;
	int k = 0;
	int reset = k;
	for(int i = 0; i < strlen(buf); i++){
		//If newline increase row by one and reset all tracking variables
		if(buf[i] == '\n'){
			row++;
			k = 0;
			reset = k;
			col = 0;
		}
		if(buf[i] == ' '){
			prevWord = i + 1; //track next word
			reset = k + 1; //track col position
		}
		//If line has ended
		if(k % ((width)) == 0 && k != 0){
			if(buf[i] != ' '){
				i = prevWord;
				while(buf[prevWord] != ' '){
					mvwprintw(win,row,reset," ");
					//increment thru word
					prevWord++;
					//increment thru line
					reset++;
				}
				//Reset k and reset
				k = 0;
				reset = k;
			}
			//Reset col and increase rows
			row++;
			col = 0;
			k = 0;
			reset = 0;
		}
		//Prevent space on first character of a line
		if(col == 0 && buf[i] == ' '){
			i++;
		}
		mvwprintw(win,row,col,"%c",buf[i]);
		col = col + 1;
		k++;
	}
	wrefresh(win);
}


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
	int row = 20;
	int col = 0;
	//PrevWord k and reset for tracking words for wraping text
	int prevWord;
	int k = 0;
	int reset = k;
	//Intro game message
	char buf[MAXSTR] = "You are a mobster on a mission to sneak into the CEO of Old Money Corporation's mansion, steal the wealth within and get out undetected. Try not to spill any blood like last time. The Boss doesn't like to clean up any messes. If you don't get enough loot, the Boss will be angry. You know what happened to the last guy that made Big Al mad...\n";
	initscr();
        	
	intro = createNewOutput(LINES - 1,COLS - 1,1,1);
mvwprintw(intro,0,0,"  ______    ______    ______   __    __  ________   ______   ______  __\n /      \\  /      \\  /      \\ |  \\  /  \\|        \\ /      \\ |      \\|  \\\n|  ######\\|  ######\\|  ######\\| ## /  ## \\########|  ######\\ \\######| ##\n| ##   \\##| ##  | ##| ##   \\##| ##/  ##    | ##   | ##__| ##  | ##  | ##\n| ##      | ##  | ##| ##      | ##  ##     | ##   | ##    ##  | ##  | ##\n| ##   __ | ##  | ##| ##   __ | #####\\     | ##   | ########  | ##  | ##\n| ##__/  \\| ##__/ ##| ##__/  \\| ## \\##\\    | ##   | ##  | ## _| ##_ | ##_____\n \\##    ## \\##    ## \\##    ##| ##  \\##\\   | ##   | ##  | ##|   ## \\| ##     \\\n  \\######   \\######   \\######  \\##   \\##    \\##    \\##   \\## \\###### \\########\n\n           __    __  ________  ______   ______  ________\n          |  \\  |  \\|        \\|      \\ /      \\|        \\\n          | ##  | ##| ######## \\######|  ######\\\\########\n          | ##__| ##| ##__      | ##  | ##___\\##  | ##\n          | ##    ##| ##  \\     | ##   \\##    \\   | ##\n          | ########| #####     | ##   _\\######\\  | ##\n          | ##  | ##| ##_____  _| ##_ |  \\__| ##  | ##\n          | ##  | ##| ##     \\|   ## \\ \\##    ##  | ##\n           \\##   \\## \\######## \\######  \\######    \\##\n");    
	wrefresh(intro);
	sleep(1);
	//Print intro game message in window
	for(int i = 0; i < strlen(buf); i++){
		if(buf[i] == ' '){
			prevWord = i + 1; //track next word
			reset = k + 1; //track col position
		}
		if(k % ((COLS - 4)) == 0 && k != 0){
			if(buf[i] != ' '){
				i = prevWord;
				while(buf[prevWord] != ' '){
					mvwprintw(intro,row,reset," ");
					prevWord++;
					reset++;
				}
				k = 0;
				reset = k;
		}
			//Reset col and increase rows
			row++;
			col = 0;
			k = 0;
			reset = 0;
		}
		//Prevent space on first char of a line
		if(col == 0 && i == ' '){
			i++;
		}
		mvwprintw(intro,row,col,"%c",buf[i]);
		col = col + 1;
		k++;
	}
	wrefresh(intro);
	wgetch(intro);

	sleep(1);
	
	clear();
	endwin();
}

//Graphic bordered window
void graphicWin(){
	//Set coordinates and size of window
	int xCoord = 0, yCoord = 3, height = LINES - 3, width = (COLS / 5) * 2;
	createNewWin(height, width, yCoord, xCoord);

}


//Graphics output window
WINDOW *graphicOutput(){
	WINDOW *graphicOut;
	int xCoord = 1, yCoord = 4, height = LINES - 5, width = ((COLS/5) * 2) - 2;
	return graphicOut = createNewOutput(height, width, yCoord, xCoord);

}

//Description bordered window
void descriptionWin(){
	int xCoord = ((COLS / 5)*2) - 1, yCoord = 3, height = LINES - 14, width = ((COLS / 5) * 3) + 3;
	createNewWin(height,width,yCoord,xCoord);
}

//Description output window
WINDOW *descriptionOutput(){
	WINDOW * desOutput;
	int xCoord = ((COLS / 5)*2), yCoord = 4, height = LINES - 12, width = ((COLS / 5) * 3) + 1;
	return desOutput = createNewOutput(height,width,yCoord,xCoord);
}

//Room Items bordered window
void itemsWin(){
	int xCoord = ((COLS / 5) * 2) - 1, yCoord = LINES - 13, height = 5, width = ((COLS / 5) * 3) + 3;
	createNewWin(height,width,yCoord,xCoord);
}

//Room items output window
WINDOW *itemsOutput(){
	WINDOW * itemOutput;
	int xCoord = (COLS / 5) * 2, yCoord = LINES - 12, height = 3, width = ((COLS / 5) * 3) + 1;
	return itemOutput = createNewOutput(height,width,yCoord,xCoord);
}


//Room Doors bordered window
void doorsWin(){
	//Get coordinates and size
	int xCoord = ((COLS / 5) * 2) - 1, yCoord = LINES - 9, height = 5, width = ((COLS / 5) * 3) + 3;
	createNewWin(height,width,yCoord,xCoord);
}

//Room doors output window
WINDOW *doorsOutput(){
	WINDOW * doorsOutput;
	int xCoord = (COLS / 5) * 2, yCoord = LINES - 8, height = 3, width = ((COLS / 5) * 3) + 1;
	return doorsOutput = createNewOutput(height,width,yCoord,xCoord);
}

//Game State Windows showing user items and current score
void *gameStateWin(){
	int xCoord = 0, yCoord = 0, height = 4, width = COLS;
	createNewWin(height,width,yCoord,xCoord);

}

WINDOW *inventoryOutput(){
	WINDOW *invOut;
	int xCoord = 1, yCoord = 1, height = 2, width = ((COLS / 6) * 5) - 1;
	return invOut = createNewOutput(height,width,yCoord,xCoord);
}

WINDOW *scoreOutput(){
	WINDOW *stateOut;
	int xCoord = (COLS / 6) * 5, yCoord = 1, height = 1, width = (COLS / 6) - 1;
	return stateOut = createNewOutput(height,width,yCoord,xCoord);

}


//Input window
void inputWin(){
	int xCoord = ((COLS / 5) * 2) - 1, yCoord = LINES - 5, height = 5, width = ((COLS / 5) * 3) + 3;
	createNewWin(height,width,yCoord,xCoord); 
}

//Input screen for commands
WINDOW *inputScr(){
	WINDOW *input;
	int xCoord = (COLS / 5) * 2, yCoord = LINES - 4, height = 3, width = ((COLS / 5) * 3) + 1;
	return input = createNewOutput(height,width,yCoord,xCoord); 
}

/*Display Current Room or Item Description, game state, input window, graphic of room or item
* Parameters: int roomID, string roomName, string Description, string inventory (userItems), int numItems, string items dropped in room, int number of items in room, string doors in room, int number of doors in the room, int user score 
*/
std::string  gameUI(int roomID, std::string roomName, std::string cppDes, std::string userItems[MAXITEM], int numItems, std::string itemsInRoom[MAXITEM], int numItemsInRoom, std::string doorsInRoom[MAXDOORS], int numDoors, int score){
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
	//Move cpp doors strings into c string char array
	char cDoorsInRoom[numDoors][32]; //char array of doors in room
	for(int i = 0; i < numDoors; i++){ 
		strcpy(cDoorsInRoom[i], doorsInRoom[i].c_str()); //Copy each door name into char array
	}
	int strlength = 0;  //to track string lengths in output windows
	//Initialize ncurses
	initscr();
	WINDOW *desOutput;
	WINDOW *roomItemsWin;
	WINDOW *doorsOut;
	WINDOW *invOut;
	WINDOW *scoreOut;
	WINDOW *graphicOut;
	WINDOW *input;
	char inputStr[256]; //C-string for input
	memset(inputStr,'\0',256);
	//Load game windows
	gameStateWin(); // show user held items and current score
	invOut = inventoryOutput();
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
	mvwprintw(desOutput, 0, 0, "%s\n", cRoomName);
	wrefresh(desOutput);
	printInWin(desOutput,cDes,((COLS/5) * 3) + 1,1);
	//Will need to loop items from array
	mvwprintw(invOut, 0, 0,"Inventory: ");
	//Print all user held items
	strlength = 11; //1 + Items: 
	for(int i = 0; i < numItems; i++){
		mvwprintw(invOut, 0, strlength,"%s ", cUserItems[i]);
		strlength = strlength + strlen(cUserItems[i]) + 1;
	}	
	wrefresh(invOut); // Refresh stateWin to display items
	mvwprintw(scoreOut, 0,0,"Score: %d",score);
	wrefresh(scoreOut);	
	mvwprintw(roomItemsWin, 0, 0, "Items dropped in room: ");
	//Print all items dropped in room
	strlength = 23; //1 + Items in room:
	for(int i = 0; i < numItemsInRoom; i++){
		mvwprintw(roomItemsWin, 0, strlength,"%s, ", cItemsInRoom[i]);
		strlength = strlength + strlen(cItemsInRoom[i]) + 2; //strlength is equal to previous strings and ,+space
	}	
	wrefresh(roomItemsWin);
	//Output doors available in room
	mvwprintw(doorsOut, 0, 0, "Doors in room: ");
	strlength = 15; //1 + Doors in room: 
	for(int i = 0; i < numDoors; i++){
		mvwprintw(doorsOut, 0, strlength,"%s, ", cDoorsInRoom[i]);
		strlength = strlength + strlen(cDoorsInRoom[i]) + 2; //strlength is equal to previous strings and ,+space
	}	
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
	std::string doors[MAXDOORS];
	std::string roomName;
	int roomID;
	description = "This upstairs bedroom\n has blue walls and oak wood floor. There are two windows to the south letting in natural light. In the center of the room on the west wall there is a queen sized bed with a gray spread. On the east wall there is a dresser and mirror.\n"; 
	roomID = 1;
	roomName = "Bedroom";
	score = 5500;
	userItems[0] = "Hammer";
	userItems[1] = "Key";
	userItems[2] = "Ring"; 

	roomItems[0] = "Bottle of Red Wine";
	roomItems[1] = "Backpack";
	roomItems[2] = "Sword";

	doors[0] = "North door";
	doors[1] = "East door";
	doors[2] = "ladder up"; 
	introWindow();
	while(1){
		input = gameUI(roomID, roomName, description, userItems,3 , roomItems, 3, doors, 3, score);
		std::cout << input << std::endl;
	}
	return 0;
}
*/
