import pygame

pygame.font.init()


class Button:
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.mainMenuButtons = []
        self.pauseButtons = []
        self.bestScoreButtons = []
        self.helpButtons = []
        self.exitButtons = []

    def addMainMenu(self, button):
        self.mainMenuButtons.append(button)

    def drawText(self, text, size, posX, posY):
        font = pygame.font.Font('fonts/AA_Magnum.ttf', size)
        buttonText = font.render(text, True, (255, 255, 255))
        buttonRect = buttonText.get_rect()
        buttonRect.center = (posX, posY)

        self.screen.blit(buttonText, buttonRect)

    def drawPause(self, text, size, posX, posY):
        font = pygame.font.SysFont('Comic Sans MS', size)
        buttonText = font.render(text, True, (0, 1, 1))
        buttonRect = buttonText.get_rect()
        buttonRect.center = (posX, posY)

        self.pauseButtons.append(buttonRect)
        self.screen.blit(buttonText, buttonRect)

    def drawBestScore(self, text, size, posX, posY):
        font = pygame.font.SysFont('Comic Sans MS', size)
        buttonText = font.render(text, True, ('#FFE80E'))
        buttonRect = buttonText.get_rect()
        buttonRect.center = (posX, posY)

        self.bestScoreButtons.append(buttonRect)
        self.screen.blit(buttonText, buttonRect)

    def drawHelp(self, text, size, posX, posY):
        font = pygame.font.SysFont('Comic Sans MS', size)
        buttonText = font.render(text, True, (0, 1, 1))
        buttonRect = buttonText.get_rect()
        buttonRect.center = (posX, posY)

        self.helpButtons.append(buttonRect)
        self.screen.blit(buttonText, buttonRect)

    def drawExit(self, text, size, posX, posY):
        font = pygame.font.SysFont('Comic Sans MS', size)
        buttonText = font.render(text, True, (0, 1, 1))
        buttonRect = buttonText.get_rect()
        buttonRect.center = (posX, posY)

        self.exitButtons.append(buttonRect)
        self.screen.blit(buttonText, buttonRect)


class MainMenuButtons(pygame.sprite.Sprite):
    def __init__(self, screen, index):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.positionList = [(100, 550), (330, 550), (560, 550), (710, 550)]
        self.nameList = ['start', 'score', 'menu', 'exit']
        self.pos = self.positionList[index]
        self.name = self.nameList[index]

        self.path = 'images/mainMenuBackground/' + self.name + '_normal.png'
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect(center=self.pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.screen.blit(self.image, self.rect)

    def check(self, cursor, x, y):
        cursorMask = pygame.mask.from_surface(cursor.image)
        offset = (x - self.rect.x, y - self.rect.y)
        result = self.mask.overlap(cursorMask, offset)
        if result:
            return True
        else:
            return False

    def change(self, new_path):
        self.path = new_path
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect(center=self.pos)
        self.screen.blit(self.image, self.rect)
