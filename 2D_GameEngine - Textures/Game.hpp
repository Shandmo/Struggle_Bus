#ifndef Game_hpp
#define Game_hpp
#pragma once

#include "SDL.h"
#include "SDL_image.h"
#include <stdio.h>
#include <iostream>


class Game {
	//Available to other parts of the class
public:
	//Constructor
	Game();
	//Deconstructor
	~Game();

	//Method for Initializing
	void init(const char* title, int xpos, int ypos, int width, int height, bool fullscreen);
	
	void handle_events();
	void update();
	bool running() { return isRunning; }
	void render();
	void clean();



private:
	bool isRunning = false;
	int cnt = 0;
	SDL_Window* window;
	SDL_Renderer* renderer;

};

#endif /* Game_hpp */