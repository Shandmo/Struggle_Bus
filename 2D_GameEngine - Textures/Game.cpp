#include "Game.hpp"
#include "SDL_image.h"

SDL_Texture* playerTex;
SDL_Rect srcR, dstR;

//Sorry future me for the comments - its the first time for me using cpp

Game::Game() : window(nullptr), renderer(nullptr), isRunning(false) {};
Game::~Game() {}

//Initilize SDL and check everything works, then set is_running var.
void Game::init(const char* title, int xpos, int ypos, int width, int height, bool fullscreen) {
	int flags = 0;
	if (fullscreen) {
		flags = SDL_WINDOW_FULLSCREEN;
	}
	if (SDL_Init(SDL_INIT_EVERYTHING) == 0) {
		std::cout << "Subsystems Initialized!..." << std::endl;
		window = SDL_CreateWindow(title, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, flags);
		if (window) {
			std::cout << "Window created!" << std::endl;
		}
		renderer = SDL_CreateRenderer(window, -1, 0);
		if (renderer) {
			SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
			std::cout << "Renderer created!" << std::endl;
		}
		isRunning = true;
	}
	SDL_Surface* tmpSurface = IMG_Load("C:\\Users\\shay\\Documents\\Dev\\source\\repos\\2D_GameEngine - Textures\\player_one.png");
	playerTex = SDL_CreateTextureFromSurface(renderer, tmpSurface);
	SDL_FreeSurface(tmpSurface);

};

void Game::handle_events() {
	SDL_Event event;
	SDL_PollEvent(&event);
	switch (event.type) {
	case SDL_QUIT:
		isRunning = false;
		break;
	default:
		break;
	}
}

void Game::update() {
	//cnt++;
	dstR.h = 64;
	dstR.w = 64;
	//dstR.x = cnt;
	//std::cout << cnt << std::endl;
};

void Game::render() {
	SDL_RenderClear(renderer);
		//this is where we would add stuff to render
	SDL_RenderCopy(renderer, playerTex, NULL, NULL);
	SDL_RenderPresent(renderer);
};

void Game::clean() {
	SDL_DestroyWindow(window);
	SDL_DestroyRenderer(renderer);
	SDL_Quit();
	std::cout << "Game Cleaned" << std::endl;
};
