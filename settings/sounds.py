import pygame


class Sound():
    def __init__(self):
        self.buttonClick = pygame.mixer.Sound('sounds/buttonClick.ogg')

        self.mainTheme = pygame.mixer.Sound('sounds/mainTheme.ogg')

        self.typeSound = pygame.mixer.Sound('sounds/typeSound.wav')
        self.readyAfterUserName = pygame.mixer.Sound('sounds/gameStart.ogg')

        self.shotSound = pygame.mixer.Sound('sounds/gunShotSound.ogg')
        self.backgroundTheme = pygame.mixer.Sound('sounds/ambientloop.ogg')
        self.pumpkinShotSound = pygame.mixer.Sound('sounds/pumpkinShotSound.ogg')
        self.timeRunning = pygame.mixer.Sound('sounds/timeRunning.ogg')
        self.gameOverSound = pygame.mixer.Sound('sounds/gameOver.ogg')
        self.bigChickenPopsUpSound = pygame.mixer.Sound('sounds/bossPopsUp.ogg')
        self.signPostSound = pygame.mixer.Sound('sounds/signPostSound.ogg')
        self.millHitSound = pygame.mixer.Sound('sounds/millHitSound.ogg')
        self.tree_hit_sound = pygame.mixer.Sound('sounds/treebranchShot.wav')

        self.chickHit1 = pygame.mixer.Sound('sounds/chickHit1.ogg')
        self.chickHit2 = pygame.mixer.Sound('sounds/chickHit2.ogg')
        self.chickHit3 = pygame.mixer.Sound('sounds/chickHit3.ogg')
        self.chickHits = []
        self.chickHits.append(self.chickHit1)
        self.chickHits.append(self.chickHit2)
        self.chickHits.append(self.chickHit3)

        self.emptyShotSound = pygame.mixer.Sound('sounds/emptyShotSound.ogg')
        self.updateAmmo = pygame.mixer.Sound('sounds/updateAmmo.ogg')

    def returnChickHits(self, sound):
        return self.chickHits[sound]
