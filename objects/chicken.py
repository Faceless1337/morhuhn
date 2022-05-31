import time

import pygame
import random


class SmallChicken(pygame.sprite.Sprite):
    def __init__(self, screen, posY):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        self.alive = True

        self.deadIndex = 0
        self.max_dead_time = 2
        self.deadTime = 0

        self.flyIndex = 0
        self.maxFlyTime = 2
        self.flyTime = 0
        self.size = (40, 40)
        self.speed = 0.095

        self.direction = 0
        self.imgPath = None
        r = random.choice([0, 800])
        if r == 0:
            self.direction = 1
            self.imgPath = 'images/chickenFlight/chicken1.png'
        else:
            self.direction = -1
            self.imgPath = 'images/chickenFlight/chicken1.png'

        self.image = pygame.transform.scale(pygame.image.load(self.imgPath).convert_alpha(), self.size)
        self.rect = self.image.get_rect(center=(r, posY))

    def update(self, dt, move):

        if self.alive:
            self.flyTime += 1
            self.screen.blit(self.image, self.rect)

            if self.direction == 1:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed * dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed * dt))
                else:
                    self.rect.x += float(self.speed * dt)

                if self.flyTime == self.maxFlyTime:
                    self.flyTime = 0
                    self.flyIndex += 1
                    if self.flyIndex == 13:
                        self.flyIndex = 0
                    elif self.flyIndex <= 12:
                        path = 'images/chickenFlight/chicken' + str(self.flyIndex) + '.png'
                        self.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size), True, False)






            else:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed * dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed * dt))
                else:
                    self.rect.x -= float(self.speed * dt)

                if self.flyTime == self.maxFlyTime:
                    self.flyTime = 0
                    self.flyIndex += 1
                    if self.flyIndex == 13:
                        self.flyIndex = 0
                    elif self.flyIndex <= 12:
                        path = 'images/chickenFlight/chicken' + str(self.flyIndex) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)

            if self.rect.y >= 540:
                self.kill()
            elif self.rect.x >= 4000:
                self.kill()
            if self.rect.x == -4000:
                self.kill()

        if not self.alive:
            self.deadTime += 1
            self.rect.y += float(self.speed * dt)

            if self.deadTime == self.max_dead_time:
                self.deadTime = 0
                self.deadIndex += 1
                if self.deadIndex == 9:
                    self.kill()
                elif self.deadIndex <= 8:
                    path = 'images/chickenFlightDeath/chickendead' + str(self.deadIndex) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)


class MiddleChicken(pygame.sprite.Sprite):
    def __init__(self, screen, posY):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        self.alive = True

        self.deadIndex = 0
        self.maxDeadTime = 2
        self.deadTime = 0

        self.flyIndex = 0
        self.maxFlyTime = 2
        self.flyTime = 0

        self.size = (60, 60)
        self.speed = 0.1

        self.direction = 0
        self.imgPath = None
        r = random.choice([0, 800])
        if r == 0:
            self.direction = 1
            self.imgPath = 'images/chickenFlight/chicken1.png'
        else:
            self.direction = -1
            self.imgPath = 'images/chickenFlight/chicken1.png'

        self.image = pygame.transform.scale(pygame.image.load(self.imgPath).convert_alpha(), self.size)
        self.rect = self.image.get_rect(center=(r, posY))

    def update(self, dt, move):

        if self.alive:
            self.flyTime += 1

            self.screen.blit(self.image, self.rect)

            if self.direction == 1:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed * dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed * dt))
                else:
                    self.rect.x += float(self.speed * dt)

                if self.flyTime == self.maxFlyTime:
                    self.flyTime = 0
                    self.flyIndex += 1
                    if self.flyIndex == 13:
                        self.flyIndex = 0
                    elif self.flyIndex <= 12:
                        path = 'images/chickenFlight/chicken' + str(self.flyIndex) + '.png'
                        self.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size), True, False)





            else:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed * dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed * dt))
                else:
                    self.rect.x -= float(self.speed * dt)

                if self.flyTime == self.maxFlyTime:
                    self.flyTime = 0
                    self.flyIndex += 1
                    if self.flyIndex == 13:
                        self.flyIndex = 0
                    elif self.flyIndex <= 12:
                        path = 'images/chickenFlight/chicken' + str(self.flyIndex) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)

            if self.rect.y >= 540:
                self.kill()
            elif self.rect.x >= 4000:
                self.kill()
            if self.rect.x == -4000:
                self.kill()

        if not self.alive:
            self.deadTime += 1
            self.rect.y += float(self.speed * dt)

            if self.deadTime == self.maxDeadTime:
                self.deadTime = 0
                self.deadIndex += 1
                if self.deadIndex == 9:
                    self.kill()
                elif self.deadIndex <= 8:
                    path = 'images/chickenFlightDeath/chickendead' + str(self.deadIndex) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)
                    # self.rect.y += 2


class BigChicken(pygame.sprite.Sprite):
    def __init__(self, screen, posY):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        self.alive = True

        self.deadIndex = 0
        self.maxDeadTime = 2
        self.deadTime = 0

        self.flyIndex = 0
        self.maxFlyTime = 2
        self.flyTime = 0

        self.size = (80, 80)
        self.speed = 0.15

        self.direction = 0
        self.imgPath = None
        r = random.choice([0, 800])
        if r == 0:
            self.direction = 1
            self.imgPath = 'images/chickenFlight/chicken1.png'
        else:
            self.direction = -1
            self.imgPath = 'images/chickenFlight/chicken1.png'

        self.image = pygame.transform.scale(pygame.image.load(self.imgPath).convert_alpha(), self.size)
        self.rect = self.image.get_rect(center=(r, posY))

    def update(self, dt, move):

        if self.alive:
            self.flyTime += 1

            self.screen.blit(self.image, self.rect)

            if self.direction == 1:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed * dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed * dt))
                else:
                    self.rect.x += float(self.speed * dt)

                if self.flyTime == self.maxFlyTime:
                    self.flyTime = 0
                    self.flyIndex += 1
                    if self.flyIndex == 13:
                        self.flyIndex = 0
                    elif self.flyIndex <= 12:
                        path = 'images/chickenFlight/chicken' + str(self.flyIndex) + '.png'
                        self.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size), True, False)





            else:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed * dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed * dt))
                else:
                    self.rect.x -= float(self.speed * dt)

                if self.flyTime == self.maxFlyTime:
                    self.flyTime = 0
                    self.flyIndex += 1
                    if self.flyIndex == 13:
                        self.flyIndex = 0
                    elif self.flyIndex <= 12:
                        path = 'images/chickenFlight/chicken' + str(self.flyIndex) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)

            if self.rect.y >= 540:
                self.kill()
            elif self.rect.x >= 4000:
                self.kill()
            if self.rect.x == -4000:
                self.kill()

        if not self.alive:
            self.deadTime += 1
            self.rect.y += float(self.speed * dt)

            if self.deadTime == self.maxDeadTime:
                self.deadTime = 0
                self.deadIndex += 1
                if self.deadIndex == 9:
                    self.kill()
                elif self.deadIndex <= 8:
                    path = 'images/chickenFlightDeath/chickendead' + str(self.deadIndex) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)
