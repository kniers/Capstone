/**************************************************
 * Name: parser.hpp
 * Author: Collin Zurbrugg
 * Description: The header file for the text parser
**************************************************/

#ifndef PARSER_HPP
#define PARSER_HPP

#include <string>
#include <cstring>
#include <iostream>
#include <bits/stdc++.h>
#include <Python.h>

#include "Command.hpp"

Command* parseIt(std::string, Command*);

std::string isItem(std::string);
std::string isVerb(std::string);

#endif
