/****************************************
 * A program for testing the text parser
****************************************/

#include <iostream>
#include "parser.hpp"

using std::cout;

int main(){
    Command comm;

    std::string parseMe = "bffergsig taco";
    parseIt(parseMe, &comm);
    cout << comm.verb << " " << comm.dirObj << " " << comm.indObj << "\n";

    return 0;
}
