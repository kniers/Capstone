/****************************************
 * A program for testing the text parser
****************************************/

#include <iostream>
#include "parser.hpp"

using std::cout;

int main(){

    Command c1;
    parseIt("north", &c1);
    cout << c1.verb << ", " << c1.dirObj << ", " << c1.indObj << ", " << c1.direction << ", " << c1.status;

    Command c2;
    parseIt("taco", &c2);
    cout << c2.verb << ", " << c2.dirObj << ", " << c2.indObj << ", " << c2.direction << ", " << c2.status;

    Command c3;
    parseIt("eat taco", &c3);
    cout << c3.verb << ", " << c3.dirObj << ", " << c3.indObj << ", " << c3.direction << ", " << c3.status;

    Command c4;
    parseIt("give alice taco", &c4);
    cout << c4.verb << ", " << c4.dirObj << ", " << c4.indObj << ", " << c4.direction << ", " << c4.status;

    Command c5;
    parseIt("give taco to alice", &c5);
    cout << c5.verb << ", " << c5.dirObj << ", " << c5.indObj << ", " << c5.direction << ", " << c5.status;

    Command c6;
    parseIt("north door", &c6);
    cout << c6.verb << ", " << c6.dirObj << ", " << c6.indObj << ", " << c6.direction << ", " << c6.status;

    Command c7;
    parseIt("open north door", &c7);
    cout << c7.verb << ", " << c7.dirObj << ", " << c7.indObj << ", " << c7.direction << ", " << c7.status;

    Command c8;
    parseIt("open north door with key", &c8);
    cout << c8.verb << ", " << c8.dirObj << ", " << c8.indObj << ", " << c8.direction << ", " << c8.status;

    Command c9;
    parseIt("go north", &c9);
    cout << c9.verb << ", " << c9.dirObj << ", " << c9.indObj << ", " << c9.direction << ", " << c9.status;

    return 0;
}
