import time

import pygame
from objectsImports import *
from objects.boss import Boss
from objects.chickenMills import MillChicken


class ScoreImgManager(pygame.sprite.Sprite):
    def __init__(self, screen, scoreManager):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.score = 0
        self.scoreManager = scoreManager
        self.font = pygame.font.Font('fonts/AA_Magnum.ttf', 50)

        self.show = False
        self.maxShowY = 25
        self.currentScore = 0

        self.maxShowTime = 3
        self.showTime = 0

        self.image = self.font.render('0', True, (255, 255, 255, 255))
        self.rect = self.image.get_rect()

    def shot(self, shotObject):
        if isinstance(shotObject, SmallChicken) or isinstance(shotObject, MiddleChicken) or isinstance(shotObject,
                                                                                                       BigChicken):
            if shotObject.size == (40, 40):
                self.score += 20
                self.scoreManager.updateScore('+', 20)
                self.show = True
                self.drawScore(str(20), shotObject)


            elif shotObject.size == (60, 60):
                self.score += 15
                self.scoreManager.updateScore('+', 15)
                self.show = True
                self.drawScore(str(15), shotObject)

            elif shotObject.size == (80, 80):
                self.score += 10
                self.scoreManager.updateScore('+', 10)
                self.show = True
                self.drawScore(str(10), shotObject)


        elif isinstance(shotObject, Pumpkin):
            self.scoreManager.updateScore('+', 15)
            self.show = True
            self.drawScore(str(15), shotObject)

        elif isinstance(shotObject, RoadSign):
            self.scoreManager.updateScore('-', 15)
            self.show = True
            self.drawScore(str(-15), shotObject)

        elif isinstance(shotObject, Boss):
            self.scoreManager.updateScore('+', 25)
            self.show = True
            self.drawScore(str(25), shotObject)

        elif isinstance(shotObject, MillChicken):
            self.scoreManager.updateScore('+', 25)
            self.show = True
            self.drawScore(str(25), shotObject)

    def drawScore(self, newScore, shotObject):
        self.image = self.font.render(newScore, True, (255, 255, 255))
        self.rect = self.image.get_rect(center=(shotObject.rect.x, shotObject.rect.y))
        self.currentScore = newScore

    def update(self):

        if self.show:
            self.showTime += 1
            self.screen.blit(self.image, self.rect)
            if self.showTime == self.maxShowTime:
                self.maxShowY -= 5
                self.rect.y -= 5

                if self.maxShowY == 0:
                    self.show = False
                    self.kill()
                else:
                    self.showTime = 0

    def drawText(self, text, size, posX, posY):
        font = pygame.font.SysFont('Comic Sans MS', size)
        buttonText = font.render(text, True, (0, 1, 1))
        buttonRect = buttonText.get_rect()
        buttonRect.center = (posX, posY)

        self.screen.blit(buttonText, buttonRect)


class ScoreManager:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0

    def updateScore(self, sign, newScore):
        if sign == '+':
            self.score += newScore
        elif sign == '-':
            self.score -= newScore

    def returnScore(self):
        return int(self.score)
