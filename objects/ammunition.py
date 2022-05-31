import pygame


class Ammunition(pygame.sprite.Sprite):

    def __init__(self, sounds):
        pygame.sprite.Sprite.__init__(self)
        self.sounds = sounds
        self.count = 8

    def update(self, screen, ammo_group):
        self.sounds.updateAmmo.play()
        self.count = 8
        for ammo in ammo_group:
            ammo.animation = False
            ammo.end()
        for i in range(0, 8):
            ammo_group.add(Ammo(screen, i))
        return 8

    def shot(self):
        if self.count == 0:

            self.sounds.emptyShotSound.play()

            return False, 9
        else:
            self.count -= 1

            self.sounds.shotSound.play()
            return True, self.count


class Ammo(pygame.sprite.Sprite):

    def __init__(self, screen, index):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.index = index

        self.count = 8
        self.show = True
        self.animation = False
        self.currentTime = 0
        self.maxTime = 1
        self.animationIndex = 0

        self.imgIndex = 1
        self.path = 'images/ammo/Ammo' + str(self.imgIndex) + '.png'
        self.image = pygame.transform.scale(pygame.image.load(self.path), (50, 80))
        self.rect = self.image.get_rect(center=(500 + self.index * 35, 550))

    def update(self, dt, index):
        if index == 8:
            self.show = True

        elif index == 9:
            self.show = False

        elif 7 - self.index == index:
            self.show = False
            self.animation = True

        if self.show:
            self.image = pygame.transform.scale(pygame.image.load(self.path).convert_alpha(), (50, 80))
            self.screen.blit(self.image, self.rect)

        elif self.animation:
            self.screen.blit(self.image, self.rect)
            self.currentTime += 1
            if self.currentTime == 1:
                self.currentTime = 0
                self.animationIndex += 1

                if self.animationIndex == 18:
                    self.animation = False
                    self.kill()


                elif self.animationIndex <= 17:
                    path = 'images/ammo/Ammo' + str(self.animationIndex) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), (50, 80))
                    self.rect.x += float(0.1 * dt)
                    self.rect.y -= float(0.05 * dt)
    def end(self):
        self.animation = False
        self.index = -1
        self.kill()
