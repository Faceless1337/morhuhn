import pygame
import random

from settings.scoreManager import ScoreImgManager

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, screen, imgPath):
        super().__init__()
        self.screen = screen
        self.simple = 'images/crosshair/crosshair.png'
        self.target = 'images/crosshair/crosshair.png'
        self.image = pygame.image.load(self.simple)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shootChicken(self, sounds, chickensGroup, checkShot, scoreManager, scoresGroup):
        for chicken in chickensGroup:
            if self.rect.colliderect(chicken.rect) and chicken.alive:
                if checkShot:
                    index = random.randint(0, 2)
                    sounds.returnChickHits(index).play()

                    score1 = ScoreImgManager(self.screen, scoreManager)
                    score1.show = True
                    scoresGroup.add(score1)
                    for score in scoresGroup:
                        if score.shot:
                            score.shot(chicken)
                    chicken.alive = False
                    return True

    def shootPumpkin(self, sounds, pumpkin, checkShot, scoreManager, scoresGroup):
        if self.rect.colliderect(pumpkin.rect) and pumpkin.alive:
            if checkShot:
                sounds.pumpkinShotSound.play()

                score1 = ScoreImgManager(self.screen, scoreManager)
                scoresGroup.add(score1)
                score1.show = True
                for score in scoresGroup:
                    if score.show:
                        score.shot(pumpkin)
                pumpkin.alive = False
                return True
    def shootSignPost(self, sounds, signPost, checkShot, scoreManager, scoresGroup):
        if self.rect.colliderect(signPost.rect):
            if checkShot:
                sounds.signPostSound.play()
                score1 = ScoreImgManager(self.screen, scoreManager)
                scoresGroup.add(score1)
                score1.show = True
                for score in scoresGroup:
                    if score.show:
                        score.shot(signPost)

                if signPost.shot:
                    signPost.shot = False
                else:
                    signPost.shot = True

                return True

    def shootBoss(self, sounds, cursor, bossGroup, checkShot, scoreManager, scoresGroup):
        for boss in bossGroup:
            if self.rect.colliderect(boss.rect):
                if checkShot:
                    index = random.randint(0, 2)
                    sounds.returnChickHits(index).play()
                    score1 = ScoreImgManager(self.screen, scoreManager)
                    scoresGroup.add(score1)
                    score1.show = True
                    for score in scoresGroup:
                        if score.show:
                            score.shot(boss)
                    if boss.alive:
                        boss.alive = False
                        boss.currentTime = 0
                return True

    def shootMill(self, cursor, x, y, sounds, mill, checkShot, scoreManager, scoresGroup):
        for chicken in mill:
            k = chicken.check_shot(cursor, x, y)
            if k:
                if checkShot:
                    index = random.randint(0, 2)
                    sounds.returnChickHits(index).play()
                    score1 = ScoreImgManager(self.screen, scoreManager)
                    scoresGroup.add(score1)
                    score1.show = True
                    for score in scoresGroup:
                        if score.show:
                            score.shot(chicken)
                    if chicken.alive:
                        chicken.alive = False
                        chicken.currentTime = 0

                return True

    def shootTree(self, sounds, trees, checkShot):
        for tree in trees:
            if self.rect.colliderect(tree.rect):
                if checkShot:
                    sounds.tree_hit_sound.play()
                return True
        return False

    def checkMainButtons(self, cursor, x, y, mainButtons, name):
        for button in mainButtons:
            if button.check(cursor, x, y) and button.name == name:
                return True
        return False

    def changeMainButton(self, cursor, x, y, main_buttons, name):
        for button in main_buttons:
            if button.check(cursor, x, y) and button.name == name:
                newButton = 'images/mainMenuBackground/' + name + '_h.png'
                button.change(newButton)
                return True
            else:
                if button.name == name:
                    newButton = 'images/mainMenuBackground/' + name + '_normal.png'
                    button.change(newButton)
        return False

    def changePressedButton(self, cursor, x, y, mainButtons, name):
        for button in mainButtons:
            if button.check(cursor, x, y) and button.name == name:
                newButton = 'images/mainMenuBackground/' + name + '_pressed.png'

                button.change(newButton)
                print('it is', newButton)
                return True
            else:
                if button.name == name:
                    newButton = 'images/mainMenuBackground/' + name + '_normal.png'
                    button.change(newButton)
        return False
