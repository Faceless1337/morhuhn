from menus.playingProcess import *
from settings.states import *

pygame.init()


class Camera:

    def __init__(self, x, y, max):
        self.max = max
        self.rect = pygame.Rect(x, y, 800, 600)

    def move(self, x):
        if self.rect[0] >= self.max:
            if x < 0:
                self.rect[0] += x
                return True
            else:
                self.rect[0] += 0
                return False
        elif self.rect[0] == 0:
            if x > 0:
                self.rect[0] += x
                return True
            else:
                self.rect[0] += 0
                return False
        else:
            self.rect[0] += x
            return True


sky = pygame.transform.scale(pygame.image.load('images/world/sky.png'), (4000, 500))
hills = pygame.transform.scale(pygame.image.load('images/world/backgroundHills.gif'), (2000, 500))

castle = pygame.transform.scale(pygame.image.load('images/world/background1.png'), (2120, 500))

green = pygame.image.load('images/world/background2.png')
