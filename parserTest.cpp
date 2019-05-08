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
    cout << c1.verb << ", " << c1.dirObj << ", " << c1.indObj << ", " << c1.direction << ", " << c1.status << "\n" << c1.errMessage << "\n";

    Command c2;
    parseIt("closet", &c2);
    cout << "closet\n";
    cout << c2.verb << ", " << c2.dirObj << ", " << c2.indObj << ", " << c2.direction << ", " << c2.status << "\n" << c2.errMessage << "\n";

    Command c3;
    parseIt("eat nightstand", &c3);
    cout << "eat nightstand\n";
    cout << c3.verb << ", " << c3.dirObj << ", " << c3.indObj << ", " << c3.direction << ", " << c3.status << "\n" << c3.errMessage << "\n";

    Command c4;
    parseIt("feel closet nightstand", &c4);
    cout << "feel closet nightstand\n";
    cout << c4.verb << ", " << c4.dirObj << ", " << c4.indObj << ", " << c4.direction << ", " << c4.status << "\n" << c4.errMessage << "\n";

    Command c5;
    parseIt("touch closet with nightstand", &c5);
    cout << "touch closet with nightstand\n";
    cout << c5.verb << ", " << c5.dirObj << ", " << c5.indObj << ", " << c5.direction << ", " << c5.status << "\n" << c5.errMessage << "\n";

    Command c6;
    parseIt("north masterBathDoor", &c6);
    cout << "north masterBathDoor\n";
    cout << c6.verb << ", " << c6.dirObj << ", " << c6.indObj << ", " << c6.direction << ", " << c6.status << "\n" << c6.errMessage << "\n";

    Command c7;
    parseIt("open north masterBathDoor", &c7);
    cout << "open north masterBathDoor\n";
    cout << c7.verb << ", " << c7.dirObj << ", " << c7.indObj << ", " << c7.direction << ", " << c7.status << "\n" << c7.errMessage << "\n";

    Command c8;
    parseIt("open north masterBathDoor with closet", &c8);
    cout << "open north masterBathDoor with closet\n";
    cout << c8.verb << ", " << c8.dirObj << ", " << c8.indObj << ", " << c8.direction << ", " << c8.status << "\n" << c8.errMessage << "\n";

    Command c9;
    parseIt("go north", &c9);
    cout << "go north\n";
    cout << c9.verb << ", " << c9.dirObj << ", " << c9.indObj << ", " << c9.direction << ", " << c9.status << "\n" << c9.errMessage << "\n";

    return 0;
}
