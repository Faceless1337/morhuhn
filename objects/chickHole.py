import pygame


class ChickHole(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.show = False
        self.showCycle = False
        self.maxShowTime = 7
        self.maxShowCycleTime = 9
        self.blinkPause = 6
        self.currentBlinkTime = 0
        self.currentTime = 0
        self.index = 0
        self.path = 'images/mainMenuBackground/chickenhole1.png'
        self.image = pygame.transform.scale(pygame.image.load(self.path), (50, 55))
        self.rect = self.image.get_rect(center=(380, 200))
        self.start = 0

    def start(self):
        self.rect = self.image.get_rect(center=(500, 200))

    def update(self):
        if self.rect != None:
            if self.show:
                self.currentTime += 1
                self.screen.blit(self.image, self.rect)
                if self.currentTime == self.maxShowTime:
                    self.index += 1
                    if self.index <= 14:
                        self.currentTime = 0
                        self.path = 'images/mainMenuBackground/chickenhole' + str(self.index) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(self.path), (65, 85))

                    elif self.index == 15:
                        self.currentTime = 0
                        self.index = 6
                        self.path = 'images/mainMenuBackground/chickenhole' + str(self.index) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(self.path), (65, 85))
                        self.show = False
                        self.showCycle = True

            elif self.showCycle:
                self.currentTime += 1
                self.screen.blit(self.image, self.rect)

                if self.currentTime == self.maxShowCycleTime:

                    if self.index == 6:
                        self.currentTime = 0
                        self.path = 'images/mainMenuBackground/chickenhole' + str(self.index) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(self.path), (65, 85))
                        self.currentBlinkTime += 1
                        self.index += 1

                    elif self.index == 7:
                        self.currentTime = 0
                        if self.currentBlinkTime == self.blinkPause:
                            self.path = 'images/mainMenuBackground/chickenhole' + str(self.index) + '.png'
                            self.image = pygame.transform.scale(pygame.image.load(self.path), (65, 85))
                            self.index += 1
                        else:
                            self.index -= 1

                    elif self.index == 8:
                        self.currentTime = 0
                        self.path = 'images/mainMenuBackground/chickenhole' + str(self.index) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(self.path), (65, 85))
                        self.currentBlinkTime = 0
                        self.index = 6
            else:
                self.show = True
