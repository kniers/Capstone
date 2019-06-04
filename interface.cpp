/* filename: interface.cpp
 * description: ncurses user interface for TBA3 Capstone project
 * version: 2019-06-03.1
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
	//Set colors
	int row = 5;
	int col = 0;
	//PrevWord k and reset for tracking words for wraping text
	int prevWord;
	int k = 0;
	int reset = k;
	//Intro game message
	char buf[MAXSTR] = "You are a mobster on a mission to sneak into the CEO of MacGuffin Inc's mansion, steal the secret plans hidden within, and get out undetected. Feel free to steal anything else you can hold. Try not to spill any blood like last time. The Boss doesn't like to clean up messes. If you don't get enough loot, the Boss will be angry. You know what happened to the last guy that made Big Al mad...  Press ENTER to continue.\n (Notice: Play game in fully maximized screen with 14-point or less.)\n";
	initscr();

	start_color();
	init_pair(1, COLOR_WHITE, COLOR_BLACK);	
	attron(COLOR_PAIR(1));
	
	intro = createNewOutput(LINES - 1,COLS - 1,1,1);
mvwprintw(intro,0,0,"  ______    ______    ______   __    __  ________   ______   ______  __\n /      \\  /      \\  /      \\ |  \\  /  \\|        \\ /      \\ |      \\|  \\\n|  ######\\|  ######\\|  ######\\| ## /  ## \\########|  ######\\ \\######| ##\n| ##   \\##| ##  | ##| ##   \\##| ##/  ##    | ##   | ##__| ##  | ##  | ##\n| ##      | ##  | ##| ##      | ##  ##     | ##   | ##    ##  | ##  | ##\n| ##   __ | ##  | ##| ##   __ | #####\\     | ##   | ########  | ##  | ##\n| ##__/  \\| ##__/ ##| ##__/  \\| ## \\##\\    | ##   | ##  | ## _| ##_ | ##_____\n \\##    ## \\##    ## \\##    ##| ##  \\##\\   | ##   | ##  | ##|   ## \\| ##     \\\n  \\######   \\######   \\######  \\##   \\##    \\##    \\##   \\## \\###### \\########\n\n           __    __  ________  ______   ______  ________\n          |  \\  |  \\|        \\|      \\ /      \\|        \\\n          | ##  | ##| ######## \\######|  ######\\\\########\n          | ##__| ##| ##__      | ##  | ##___\\##  | ##\n          | ##    ##| ##  \\     | ##   \\##    \\   | ##\n          | ########| #####     | ##   _\\######\\  | ##\n          | ##  | ##| ##_____  _| ##_ |  \\__| ##  | ##\n          | ##  | ##| ##     \\|   ## \\ \\##    ##  | ##\n           \\##   \\## \\######## \\######  \\######    \\##\n");    
	wrefresh(intro);
	sleep(3);
	werase(intro);
	//Print intro game message in window
	for(int i = 0; i < strlen(buf); i++){
		//If newline go to next row
		if(buf[i] == '\n'){
			row++;
			col = 0;
			k = 0;
			reset = 0;
		}
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

	//sleep(1);
	
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
void gameStateWin(){
	int xCoord = 0, yCoord = 0, height = 4, width = COLS;
	createNewWin(height,width,yCoord,xCoord);
}

WINDOW *extraOutput(){
	WINDOW *extOut;
	int xCoord = 1, yCoord = 1, height = 2, width = ((COLS / 6) * 5) - 1;
	return extOut = createNewOutput(height,width,yCoord,xCoord);
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
/* function: printMap
 * description: prints map of house and current location with red $
 * parameters: WINDOW to print map in, char  current room
 * returns: void
 */
void printMap(WINDOW *graphicOut, char *cRoomName){
	//Show mansion floor plan
	mvwprintw(graphicOut,0,0,"                    00000000000000\n                    0|||||  0    0\n                    000000  0    0\n        0000000000  0    0  0_0000\n        0        0  0    |  0    0\n0000000000_0000000  000000  0    0\n0            |   0  0    0  |    0\n0000         0   0  0 0_ 0  0    0\n0  |         0   |  000     0    0\n000000_0000000_000  0 0 _0000_0000\n    0  |||0      0  0       0    0\n    |     |      0  00000000000000\n    0     0      0   SECOND FLOOR\n00000_000000_00000_00000\n0   0    0 0     0     0\n0   0    000     0     0\n0   |      |     |     0\n000000000000000000000000\n      FIRST FLOOR\n");
	//Get player location	
	//Set position char to red
	wattron(graphicOut,COLOR_PAIR(2));
	if(strcmp("Bar",cRoomName) == 0){
		mvwprintw(graphicOut,7,15,"$");
	}	
	if(strcmp("Ballroom",cRoomName) == 0){
		mvwprintw(graphicOut,7,10,"$");	
	}	
	if(strcmp("Foyer",cRoomName) == 0){
		mvwprintw(graphicOut,11,7,"$");
	}	
	if(strcmp("Library",cRoomName) == 0){
		mvwprintw(graphicOut,15,7,"$");	
	}
	if(strcmp("Study",cRoomName) == 0){
		mvwprintw(graphicOut,15,2,"$");
	}	
	if(strcmp("Portrait Gallery",cRoomName) == 0){
		mvwprintw(graphicOut,11,15,"$");	
	}
	if(strcmp("Billiard Room",cRoomName) == 0){
		mvwprintw(graphicOut,15,14,"$");
	}	
	if(strcmp("Kitchen",cRoomName) == 0){
		mvwprintw(graphicOut,4,10,"$");	
	}
	if(strcmp("Bathroom",cRoomName) == 0){
		mvwprintw(graphicOut,8,1,"$");
	}	
	if(strcmp("Secret Room",cRoomName) == 0){
		mvwprintw(graphicOut,14,10,"$");	
	}
	if(strcmp("Conservatory",cRoomName) == 0){
		mvwprintw(graphicOut,15,20,"$");
	}	
	if(strcmp("Gardens",cRoomName) == 0){
		mvwprintw(graphicOut,12,19,"$");	
	}
	if(strcmp("Billiard Room",cRoomName) == 0){
		mvwprintw(graphicOut,15,14,"$");
	}	
	if(strcmp("Hallway",cRoomName) == 0){
		mvwprintw(graphicOut,5,26,"$");	
	}
	if(strcmp("Master Bedroom",cRoomName) == 0){
		mvwprintw(graphicOut,6,30,"$");	
	}	
	if(strcmp("Master Bathroom",cRoomName) == 0){
		mvwprintw(graphicOut,2,30,"$");	
	}
	if(strcmp("Second Bedroom",cRoomName) == 0){
		mvwprintw(graphicOut,4,22,"$");
	}	
	if(strcmp("Guest Bedroom",cRoomName) == 0){
		mvwprintw(graphicOut,6,22,"$");	
	}
	if(strcmp("Office",cRoomName) == 0){
		mvwprintw(graphicOut,10,22,"$");	
	}
	if(strcmp("Front Porch",cRoomName) == 0){
		mvwprintw(graphicOut,11,2,"$");
	}
	wrefresh(graphicOut);
	attron(COLOR_PAIR(1));
}
/* function: printItems
 * description: prints an array of c string items
 * parameters: WINDOW to print in, c string array of items, number of items, starting point in row, width of WINDOW
 * returns: void
 */

void printItems(WINDOW *outWin, char items[MAXITEM][32], int numItems,  int strlength, int col){
	//count rows
	int newRow = 0;
	for(int i = 0; i < numItems; i++){
		if(strlength >= col || strlength + strlen(items[i]) + 1 > col){
			newRow++;
			strlength = 0;
		}
		mvwprintw(outWin, newRow, strlength," %s |", items[i]);
		strlength = strlength + strlen(items[i]) + 3;
	}	
	wrefresh(outWin); // Refresh window to display items
} 

/*Display Current Room or Item Description, game state, input window, graphic of room or item
* Parameters: bool inventory command, int roomID, string roomName, string Description, string inventory (userItems), int numItems, string items dropped in room, int number of items in room, string doors in room, int number of doors in the room, int user score 
*/
std::string  gameUI(bool inv, int roomID, std::string roomName, std::string cppDes, std::string userItems[MAXITEM], int numItems, std::string itemsInRoom[MAXITEM], int numItemsInRoom, std::string doorsInRoom[MAXDOORS], int numDoors, int score){
	//Convert C++ strings to C strings
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
	
	//Start and set color attributes
	start_color();	
	init_pair(1, COLOR_WHITE, COLOR_BLACK);
	init_pair(2, COLOR_RED, COLOR_BLACK);
	attron(COLOR_PAIR(1));
	//Create output windows
	WINDOW *desOutput;
	WINDOW *roomItemsWin;
	WINDOW *doorsOut;
	WINDOW *extOut;
	WINDOW *scoreOut;
	WINDOW *graphicOut;
	WINDOW *input;
	char inputStr[256]; //C-string for input
	memset(inputStr,'\0',256);
	//Load game windows
	gameStateWin(); // show user held items and current score
	extOut = extraOutput();
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
	mvwprintw(scoreOut, 0,0,"Score: %d",score);
	wrefresh(scoreOut);	
	mvwprintw(roomItemsWin, 0, 0, "Items dropped in room:");
	//Print all items dropped in room
	strlength = 22; //1 + Items in room:
	//Print items dropped in room
	printItems(roomItemsWin, cItemsInRoom, numItemsInRoom, strlength,((COLS/5)*3)+1);
	//Output doors available in room
	mvwprintw(doorsOut, 0, 0, "Doors in room: ");
	strlength = 14; //Doors in room: 
	//Print doors in room
	printItems(doorsOut, cDoorsInRoom, numDoors, strlength, ((COLS/5)*3)+1);
	if(inv){
		// loop items from array
		mvwprintw(graphicOut, 0, 0,"Inventory:");
		//Print all user held items
		strlength = 10; //Items: 
		//Print inventory
		printItems(graphicOut, cUserItems, numItems, strlength, ((COLS/5)*2)-2);
	}
	if(!inv){
		//Print Map if in inventory
		for(int i = 0; i < numItems; i++){
			if(strcmp(cUserItems[i], "blueprints") == 0){
				//Print Map
				printMap(graphicOut,cRoomName);
			}
		}
	}
	//Prompt User for command
	mvwprintw(input, 0,0,"What would you like to do? ");
	wrefresh(input);
	wgetstr(input, inputStr); //Get string from user
	cppString = inputStr;
	//This is to test input remove above
	//wgetch(input); //Any key to exit
	//sleep(1);
	endwin(); //end curses mode
	return cppString;

}
/*
//Main for testing interface
int main(){
	std::string input;
	std::string description; // room or item description
	int  score;
	bool inv = 0;
	std::string userItems[MAXITEM];
	std::string roomItems[MAXITEM];
	std::string doors[MAXDOORS];
	std::string roomName;
	int roomID;
	description = "This upstairs bedroom\n has blue walls and oak wood floor. There are two windows to the south letting in natural light. In the center of the room on the west wall there is a queen sized bed with a gray spread. On the east wall there is a dresser and mirror.\n"; 
	roomID = 1;
	roomName = "Master Bedroom";
	score = 5500;
	userItems[0] = "blueprints";
	userItems[1] = "Key";
	userItems[2] = "golden comb";
	userItems[3] = "beer of life"; 	
	userItems[4] = "ninja star";
	userItems[5] = "jump rope";
	userItems[6] = "lance";
	userItems[7] = "mobile suit"; 
	userItems[8] = "bonekey";
	userItems[9] = "french flag";
	userItems[10] = "bear brush";
	userItems[11] = "friend in need"; 
	userItems[12] = "wooden stake";
	userItems[13] = "everlasting gobstoppers";
	userItems[14] = "lint";
	userItems[15] = "cat fur"; 

	roomItems[0] = "Bottle of Red Wine";
	roomItems[1] = "ruby slippers";
	roomItems[2] = "Runic Sword";
	roomItems[3] = "Bowling Ball";

	doors[0] = "North door";
	doors[1] = "East door";
	doors[2] = "ladder up"; 
	introWindow();
	while(1){
		input = gameUI(inv, roomID, roomName, description, userItems, 16, roomItems, 4, doors, 3, score);
		std::cout << input << std::endl;
		inv = 0;
		if(input == "inventory"){	
			inv = 1;
		}
	}
	return 0;
}
*/
