#include <ncurses.h>

int main() {
initscr();
wborder(stdscr, '|', '|', '-', '-', '+', '+', '+', '+'); 
move(2, 2);
printw("Hello World !!!");
refresh();
getch();
endwin();
return 0;
}
