/* filename: interface.cpp
 * description: ncurses user interface for TBA3 Capstone project
 * version: 2019-04-27.1
 * compile: g++ interface.cpp -o uiinit -lncurses: test run with uiinit
 * author: Adam Deaton
 */

#include <ncurses.h>
#include <unistd.h>

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
	intro = createNewOutput(LINES/2,COLS/2,LINES/4,COLS/4);
	mvwprintw(intro,2,2,"COCKTAIL HEIST\nYou are a mobster on a mission to sneak into the CEO of Old  Money Corporation's mansion steal the wealth within and get  out undetected. If you don't get enough loot, the boss will be angry. You know what happened to the last guy that made Big Al mad...\n");
	wrefresh(intro);
	wgetch(intro);

	sleep(1);
	
	clear();
}

//Window for graphics
void graphicWin(){
	WINDOW *graphic;
	int xCoord = 0, yCoord = 2, height = LINES - 2, width = COLS / 2;
	graphic = createNewWin(height, width, yCoord, xCoord);

}

//Description of room window
WINDOW *descriptionWin(){
	WINDOW * desWin;
	int xCoord = (COLS / 2) - 1, yCoord = 2, height = LINES - 10, width = (COLS / 2) + 1;
	return desWin = createNewWin(height,width,yCoord,xCoord);
}

//Description of room window
WINDOW *descriptionOutput(){
	WINDOW * desOutput;
	int xCoord = (COLS / 2), yCoord = 3, height = LINES - 9, width = (COLS / 2) - 1;
	return desOutput = createNewOutput(height,width,yCoord,xCoord);
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
WINDOW *inputWin(){
	WINDOW *inWin;
	int xCoord = (COLS / 2) - 1, yCoord = LINES - 9, height = 9, width = (COLS / 2) + 1;
	return inWin = createNewWin(height,width,yCoord,xCoord); 
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
* Parameters: check game engine to termine and then update
*/
void gameUI(){
	//Initialize ncurses
	initscr();
	//cbreak();
	noecho(); // suppress echo
	WINDOW *desWin;
	WINDOW *desOutput;
	WINDOW *stateWin;
	WINDOW *scoreOut;
	WINDOW *inWin;
	WINDOW *input;
	//Load game windows
	introWindow();
	stateWin = gameStateWin(); // show user held items and current score
	scoreOut = scoreOutput();
	graphicWin(); // show room graphics
	desWin = descriptionWin(); // room description window
	desOutput = descriptionOutput(); //output room description
	inWin = inputWin(); //input window
	input = inputScr(); //game waits for input
	mvwprintw(desOutput, 0, 0,"BEDROOM:\nThis bedroom has blue walls and a oak wood floor. There are two windows to the south letting in natural light. In the center of the room on the west wall there is a queen sized bed with a gray spread. On the east wall there is a dresser and mirror.\n Items in the room:");
	wrefresh(desOutput);
	//Will need to loop items from array
	mvwprintw(stateWin, 1, 1,"Items:%s ", "Hammer");	
	wrefresh(stateWin);
	mvwprintw(scoreOut, 0,0,"Score: %d",5500);
	wrefresh(scoreOut);	
	mvwprintw(input, 0,0,"What would you like to do? ");
	wrefresh(input);
	wgetch(input);
	sleep(1);
	endwin(); //end curses mode

}

//Main for testing interface
int main(){
	gameUI();

}
