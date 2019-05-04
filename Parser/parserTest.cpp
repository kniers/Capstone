/****************************************
 * A program for testing the text parser
****************************************/

#include <iostream>
#include "parser.hpp"

using std::cout;

int main(){

    Command c1;
    parseIt("north", &c1);
    cout << "north\n";
    cout << c1.verb << ", " << c1.dirObj << ", " << c1.indObj << ", " << c1.direction << ", " << c1.status << "\n\n";

    Command c2;
    parseIt("chest", &c2);
    cout << "chest\n";
    cout << c2.verb << ", " << c2.dirObj << ", " << c2.indObj << ", " << c2.direction << ", " << c2.status << "\n\n";

    Command c3;
    parseIt("eat chest", &c3);
    cout << "eat chest\n";
    cout << c3.verb << ", " << c3.dirObj << ", " << c3.indObj << ", " << c3.direction << ", " << c3.status << "\n\n";

    Command c4;
    parseIt("give chest chest", &c4);
    cout << "give chest chest\n";
    cout << c4.verb << ", " << c4.dirObj << ", " << c4.indObj << ", " << c4.direction << ", " << c4.status << "\n\n";

    Command c5;
    parseIt("give chest to chest", &c5);
    cout << "give chest to chest\n";
    cout << c5.verb << ", " << c5.dirObj << ", " << c5.indObj << ", " << c5.direction << ", " << c5.status << "\n\n";

    Command c6;
    parseIt("north bridge", &c6);
    cout << "north bridge\n";
    cout << c6.verb << ", " << c6.dirObj << ", " << c6.indObj << ", " << c6.direction << ", " << c6.status << "\n\n";

    Command c7;
    parseIt("open north bridge", &c7);
    cout << "open north bridge\n";
    cout << c7.verb << ", " << c7.dirObj << ", " << c7.indObj << ", " << c7.direction << ", " << c7.status << "\n\n";

    Command c8;
    parseIt("open north bridge with chest", &c8);
    cout << "open north bridge with chest\n";
    cout << c8.verb << ", " << c8.dirObj << ", " << c8.indObj << ", " << c8.direction << ", " << c8.status << "\n\n";

    Command c9;
    parseIt("go north", &c9);
    cout << "go north\n";
    cout << c9.verb << ", " << c9.dirObj << ", " << c9.indObj << ", " << c9.direction << ", " << c9.status << "\n\n";

    return 0;
}
