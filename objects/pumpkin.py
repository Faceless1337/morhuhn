import pygame


class Pumpkin(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        self.alive = True
        self.stop = False

        self.image = pygame.transform.scale(pygame.image.load('images/pumpkin/pumpkin1.png'), (100, 100))
        self.rect = self.image.get_rect(center=(2110, 410))
        self.deIndex = 0
        self.maxTime = 2
        self.deTime = 0
    def update(self, move):
        if self.alive:
            if move == 'move_r':
                self.rect.x -= 40
            elif move == 'move_l':
                self.rect.x += 40
            self.screen.blit(self.image, self.rect)

        else:
            if not self.stop:
                if move == 'move_r':
                    self.rect.x -= 40
                elif move == 'move_l':
                    self.rect.x += 40
                self.deTime += 1
                if self.deTime == self.maxTime:
                    self.deTime = 0
                    self.deIndex += 1
                    if self.deIndex <= 8:
                        path = 'images/pumpkin/pumpkin' + str(self.deIndex) + '.png'
                        self.image = pygame.image.load(path)
                    elif self.deIndex == 9:
                        self.stop = True
                        path = 'images/pumpkin/pumpkin9.png'
                        self.image = pygame.image.load(path)

            else:
                if move == 'move_r':
                    self.rect.x -= 40
                elif move == 'move_l':
                    self.rect.x += 40
                path = 'images/pumpkin/pumpkin9.png'
                self.image = pygame.image.load(path)
            self.screen.blit(self.image, self.rect)
