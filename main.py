import pygame
from settings.states import Game

game = Game()

if __name__ == '__main__':
    print('START GAME')
    game.startGame()
pygame.quit()

