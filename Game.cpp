#include "Game.hpp"

//Sorry future me for the comments - its the first time for me using cpp
Game::Game() {

}
Game::~Game() {

}

//Initilize SDL and check everything works, then set is_running var.
void Game::init(const char* title, int xpos, int ypos, int width, int height, bool fullscreen) {
	int flags = 0;
	//Set Fullscreen if enabled
	if (fullscreen) {
		flags = SDL_WINDOW_FULLSCREEN;
	}
	//Check to make sure initilization is good.
	if (SDL_Init(SDL_INIT_EVERYTHING) == 0) {
		std::cout << "Subsystems Initialized!..." << std::endl;
	
	//Create Window - take window created in header file and pass in all vars
		window = SDL_CreateWindow(title, xpos, ypos, width, height, flags);
	//Check if window is good to go.
		if (window) {
			std::cout << "Window created!" << std::endl;
		}
	//Create Renderer
		renderer = SDL_CreateRenderer(window, -1, 0);
		if (renderer) {
			SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
			std::cout << "Renderer cretaed!" << std::endl;
		}

		is_running = true;
	} else {
		is_running = false;
	}

};
void Game::handle_events() {
	SDL_Event event;
	SDL_PollEvent(&event);
	switch (event.type) {
		case SDL_QUIT:
			is_running = false;
			break;
		default:
			break;
	}
}

void Game::update() {

};

void Game::render() {
	SDL_RenderClear(renderer);
		//this is where we would add stuff to render
	SDL_RenderPresent(renderer);
};

void Game::clean() {
	SDL_DestroyWindow(window);
	SDL_DestroyRenderer(renderer);
	SDL_Quit();
	std::cout << "Game Cleaned" << std::endl;
};
