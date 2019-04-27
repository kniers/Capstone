/****************************************
 * A program for testing the text parser
****************************************/

#include <iostream>
#include "parser.hpp"

using std::cout;

int main(){

    Command c1;
    parseIt("north", &c1);
    printf("%s %s %s %d\n", c1->verb, c1->dirObj, c1->indObj, c1->status);

    Command c2;
    parseIt("taco", &c2);
    printf("%s %s %s %d\n", c1->verb, c1->dirObj, c1->indObj, c1->status);

    Command c3;
    parseIt("eat taco", &c3);
    printf("%s %s %s %d\n", c1->verb, c1->dirObj, c1->indObj, c1->status);

    Command c4;
    parseIt("give alice taco", &c4);
    printf("%s %s %s %d\n", c1->verb, c1->dirObj, c1->indObj, c1->status);


    Command c5;
    parseIt("give taco to alice", &c5);
    printf("%s %s %s %d\n", c1->verb, c1->dirObj, c1->indObj, c1->status);


    Command c6;
    parseIt("north door", &c6);
    printf("%s %s %s %d\n", c1->verb, c1->dirObj, c1->indObj, c1->status);

    Command c7;
    parseIt("open north door", &c7);
    printf("%s %s %s %d\n", c1->verb, c1->dirObj, c1->indObj, c1->status);

    Command c8;
    parseIt("open north door with key", &c8);
    printf("%s %s %s %d\n", c1->verb, c1->dirObj, c1->indObj, c1->status);

    Command c9;
    parseIt("go north", &c9);
    printf("%s %s %s %d\n", c1->verb, c1->dirObj, c1->indObj, c1->status);

    return 0;
}
