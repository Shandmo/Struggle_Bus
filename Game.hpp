#ifndef Game_hpp
#define Game_hpp

#include "SDL.h"
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
	void render();
	void clean();

	bool running() { return is_running; }

private:
	bool is_running;
	SDL_Window* window;
	SDL_Renderer* renderer;

};

#endif /* Game_hpp */