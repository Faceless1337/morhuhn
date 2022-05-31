import pygame


class Boss(pygame.sprite.Sprite):

    def __init__(self, screen, position):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.position = position

        self.alive = True

        self.show = True
        self.showCycle = False
        self.maxShowTime = 3
        self.maxCycleShowTime = 5

        self.waitBeforeDis = 0
        self.disappear = False
        self.currentTime = 0
        self.index = 0

        self.blinkPause = 6
        self.currentBlinkTime = 0

        self.currentDeathTime = 0
        self.deathTime = 2
        self.deathIndex = -1
        self.stopDeath = False

        self.waitTime = 20
        self.currentWaitTime = 0

        self.path = 'images/boss/boss' + str(self.index) + '.png'
        self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))
        self.rect = self.image.get_rect(center=self.position)

    def update(self, move):
        if self.alive:
            if move == 'move_r':
                self.rect.x -= 40
            elif move == 'move_l':
                self.rect.x += 40
            else:

                if self.show:
                    self.currentTime += 1
                    self.screen.blit(self.image, self.rect)

                    if self.currentTime == self.maxShowTime:
                        self.index += 1
                        self.currentTime = 0

                        if self.index <= 17:
                            self.path = 'images/boss/boss' + str(self.index) + '.png'
                            self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))

                        elif self.index == 18:
                            self.path = 'images/boss/boss' + str(self.index) + '.png'
                            self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))
                            self.show = False
                            self.showCycle = True
                            self.currentTime = 0
                            self.index = 8

                if self.showCycle:
                    self.currentTime += 1
                    self.screen.blit(self.image, self.rect)
                    self.waitBeforeDis += 1

                    if self.waitBeforeDis == 70:
                        self.showCycle = False
                        self.disappear = True
                        self.currentTime = 0
                        self.index = 5
                    else:
                        if self.currentTime == self.maxShowTime:
                            self.currentTime = 0

                            if self.index == 8:
                                self.path = 'images/boss/boss' + str(self.index) + '.png'
                                self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))
                                self.index += 1
                                self.currentBlinkTime += 1

                            elif self.index == 9:
                                if self.currentBlinkTime == self.blinkPause:
                                    self.path = 'images/boss/boss' + str(self.index) + '.png'
                                    self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))
                                    self.index += 1
                                    self.currentBlinkTime = 0
                                else:
                                    self.index -= 1

                            elif self.index > 9 and self.index <= 17:
                                self.path = 'images/boss/boss' + str(self.index) + '.png'
                                self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))
                                self.index += 1

                            elif self.index == 18:
                                self.path = 'images/boss/boss' + str(self.index) + '.png'
                                self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))
                                self.index = 8

                if self.disappear:
                    self.currentTime += 1
                    self.screen.blit(self.image, self.rect)
                    if self.currentTime == self.maxShowTime:
                        self.index -= 1
                        self.currentTime = 0
                        if self.index == 0:
                            self.path = 'images/boss/boss' + str(self.index) + '.png'
                            self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))
                            self.disappear = False
                            self.kill()
                        else:
                            self.path = 'images/boss/boss' + str(self.index) + '.png'
                            self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))

        if not self.alive:
            self.screen.blit(self.image, self.rect)
            self.currentDeathTime += 1
            if self.currentDeathTime == 3:
                self.currentDeathTime = 0
                self.deathIndex += 1

                if self.deathIndex == 6:

                    self.kill()

                elif self.deathIndex <= 5:
                    self.path = 'images/boss/bossDead' + str(self.deathIndex) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(self.path), (300, 300))
