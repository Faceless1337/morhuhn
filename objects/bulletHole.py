import pygame


class Hole(pygame.sprite.Sprite):
    def __init__(self, screen, count):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.currentTime = 0
        self.maxTime = 40
        self.show = True

        self.image = pygame.transform.scale(pygame.image.load('images/mainMenuBackground/hole.png'), (40, 40))
        self.rect = None
        self.count = count

    def update(self, sounds):
        self.currentTime += 1
        if self.rect == None:
            pass
        else:
            self.screen.blit(self.image, self.rect)

        if self.currentTime == self.maxTime:
            if self.count == 1:
                self.rect = self.image.get_rect(center=(500, 200))
                sounds.shotSound.play()

            elif self.count == 2:
                self.rect = self.image.get_rect(center=(450, 300))
                sounds.shotSound.play()

            elif self.count == 3:
                self.rect = self.image.get_rect(center=(290, 320))
                sounds.shotSound.play()

            elif self.count == 4:
                self.rect = self.image.get_rect(center=(300, 220))
                sounds.shotSound.play()

    def shot(self):
        self.kill()
