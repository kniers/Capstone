/*********************************************************************
* File: interface.hpp
* Author: Adam Deaton
* Date: 2019.05.26
* Description: Header for user interface.cpp details in cpp file
*********************************************************************/
#ifndef INTERFACE_HPP
#define INTERFACE_HPP

#include <ncurses.h>
#include <unistd.h>
#include <cstring>
#include <string>
#include <iostream>

#define MAXITEM 32
#define MAXDOORS 6
#define MAXSTR 1024

void printInWin(WINDOW , char, int,int);	

WINDOW *createNewWin(int, int, int, int);

WINDOW *createNewOutput(int, int ,int, int);

void introWindow();

void graphicWin();

WINDOW *graphicOutput();

void descriptionWin();

WINDOW *descriptionOutput();

void itemsWin();

WINDOW *itemsOutput();

void doorsWin();

WINDOW *doorsOutput();

void gameStateWin();

WINDOW *extraOutput();

WINDOW *scoreOutput();

void inputWin();

WINDOW *inputScr();

void printMap(WINDOW, char);

void printItems(WINDOW, char, int, int, int);

std::string gameUI(bool, int, std::string, std::string, std::string*, int, std::string*, int, std::string*, int, int);

#endif
