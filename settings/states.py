import pygame.sprite
from random import randint
import shelve
from menusImports import *
from menus.playingProcess import playingProcess
from objectsImports import *
from settingsImports import *

pygame.init()
HEIGHT = 600
WIDTH = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.time.set_timer(pygame.USEREVENT, 4000)

buttons = Button(screen)

mainButtons = pygame.sprite.Group()
for i in range(0, 4):
    mainButtons.add(MainMenuButtons(screen, i))

sounds = Sound()

chickenHole = ChickHole(screen)

holes = pygame.sprite.Group()
holes.add(Hole(screen, 0))

cursor = Crosshair(screen, 'images/crosshair/crosshair.png')
cursorGroup = pygame.sprite.Group()
cursorGroup.add(cursor)

clock = pygame.time.Clock()


def setUserName(name):
    USER_NAME = name


class State:
    def backToIntroMode(self):
        raise NotImplementedError

    def enterNewScreen(self):
        raise NotImplementedError

    def playGameMode(self):
        raise NotImplementedError

    def bestGameMode(self):
        raise NotImplementedError

    def helpGameMode(self):
        raise NotImplementedError

    def exitGameMode(self):
        raise NotImplementedError


class Game:
    def __init__(self):
        self.gameState = MainMenuState(game=self)
        self.save = Save()
        self.scores = 0
        self.username = ''

        self.highscore = HighscoreTable(self.save.get('hs'))

    def startGame(self):
        self.gameState.enterNewScreen()

    def changeGameState(self, new_state: State):
        if self.gameState == None:
            pass
        self.gameState = new_state
        self.gameState.enterNewScreen()

    def playGameMode(self):
        self.gameState.playGameMode()

    def bestGameMode(self):
        self.gameState.bestGameMode()

    def helpGameMode(self):
        self.gameState.helpGameMode()

    def exitGameMode(self):
        self.gameState.exitGameMode()


class MainMenuState(State):
    def __init__(self, game):
        self.game = game

    def enterNewScreen(self):
        pygame.display.set_caption("MAIN MENU")

        chosenScreen = mainMenuLoop(screen, sounds, cursor, cursorGroup, mainButtons, buttons, chickenHole, holes)
        if chosenScreen == 1:
            self.game.playGameMode()
        elif chosenScreen == 2:
            self.game.bestGameMode()
        elif chosenScreen == 3:
            self.game.helpGameMode()
        elif chosenScreen == 4:
            self.game.exitGameMode()

    def backToIntroMode(self):
        pygame.display.set_caption("MAIN MENU")
        chosenScreen = mainMenuLoop(screen, sounds, cursorGroup, buttons)
        if chosenScreen == 1:
            self.game.playGameMode()
        elif chosenScreen == 2:
            self.game.bestGameMode()
        elif chosenScreen == 3:
            self.game.helpGameMode()

    def playGameMode(self):
        self.game.changeGameState(PlayState(self.game))

    def usernameGameMode(self):
        self.game.changeGameState(UserNameState(self.game))

    def bestGameMode(self):
        self.game.changeGameState(BestScoreState(self.game))

    def helpGameMode(self):
        self.game.changeGameState(HelpState(self.game))

    def exitGameMode(self):
        self.game.changeGameState(ExitState(self.game))


class PlayState(State):
    def __init__(self, game):
        self.game = game
        self.scores = 0

    def backToIntroMode(self):
        self.game.changeGameState(MainMenuState(game=self.game))

    def enterNewScreen(self):
        pygame.display.set_caption('PLAY')

        mill = pygame.sprite.Group()
        for i in range(0, 4):
            mill.add(MillChicken(screen, i))

        ammo = Ammunition(sounds)
        ammoGroup = pygame.sprite.Group()
        for i in range(0, 8):
            ammoGroup.add(Ammo(screen, i))

        pumpkin = Pumpkin(screen)

        roadSign = RoadSign(screen)
        smallChickenGroup = pygame.sprite.Group()
        smallChickenGroup.add(SmallChicken(screen, randint(100, 200)))
        midChickenGroup = pygame.sprite.Group()
        midChickenGroup.add(MiddleChicken(screen, randint(100, 300)))
        bigChickenGroup = pygame.sprite.Group()
        bigChickenGroup.add(BigChicken(screen, randint(100, 500)))
        scoresGroup = pygame.sprite.Group()
        scoreManager = ScoreManager(screen)
        scoresGroup.add(ScoreImgManager(screen, scoreManager))

        bossGroup = pygame.sprite.Group()

        check, score = playingProcess(clock, screen, sounds, buttons, cursor, cursorGroup, smallChickenGroup,
                                      midChickenGroup, bigChickenGroup, ammo, ammoGroup, scoreManager, scoresGroup,
                                      pumpkin, roadSign, bossGroup, mill)

        self.game.scores = score
        if check == 1:
            self.game.changeGameState(PauseState(self.game))
        elif check == 2:
            self.game.changeGameState(UserNameState(self.game))

    def playGameMode(self):
        pass

    def bestGameMode(self):
        self.game.changeGameState(BestScoreState(self.game))

    def helpGameMode(self):
        self.game.changeGameState(HelpState(self.game))

    def exitGameMode(self):
        self.game.changeGameState(ExitState(self.game))


class UserNameState(State):
    def __init__(self, game):
        self.game = game

    def enterNewScreen(self):
        check, userName = nameManuLoop(screen, sounds)
        self.game.username = userName

        if check:
            print('user name: ', userName)
            self.game.highscore.update(self.game.username, self.game.scores)
            self.game.save.add('hs', self.game.highscore.hsTable)
            self.game.changeGameState(BestScoreState(self.game))

    def backToIntroMode(self):
        pass

    def playGameMode(self):
        pass

    def bestGameMode(self):
        pass

    def helpGameMode(self):
        pass

    def exitGameMode(self):
        pass


class PauseState(State):
    def __init__(self, game):
        self.game = game

    def backToIntroMode(self):
        self.game.changeGameState(MainMenuState(game=self.game))

    def enterNewScreen(self):
        pygame.display.set_caption('PAUSE')
        check = pauseMenu(screen, sounds, buttons, cursorGroup)
        if check == 1:

            self.game.changeGameState(MainMenuState(self.game))
        elif check == 2:

            self.game.changeGameState(ExitState(self.game))

    def playGameMode(self):
        pass

    def bestGameMode(self):
        self.game.changeGameState(BestScoreState(self.game))

    def helpGameMode(self):
        self.game.changeGameState(HelpState(self.game))

    def exitGameMode(self):
        self.game.changeGameState(ExitState(self.game))


class BestScoreState(State):
    def __init__(self, game):
        self.game = game

    def backToIntroMode(self):
        self.game.changeGameState(MainMenuState(self.game))

    def enterNewScreen(self):
        pygame.display.set_caption('BEST SCORE TABLE')
        newState = recordMenu(screen, sounds, cursorGroup, buttons, self.game.username, self.game.scores,
                              self.game)

        if newState:
            self.game.changeGameState(MainMenuState(self.game))

    def playGameMode(self):
        self.game.changeGameState(PlayState(self.game))

    def bestGameMode(self):
        pass

    def helpGameMode(self):
        self.game.changeGameState(HelpState(self.game))

    def exitGameMode(self):
        self.game.changeGameState(ExitState(self.game))


class HelpState(State):
    def __init__(self, game):
        self.game = game

    def backToIntroMode(self):
        self.game.changeGameState(MainMenuState(self.game))

    def enterNewScreen(self):
        pygame.display.set_caption('HELP INFORMATION')
        check = helpMenu(screen, sounds, cursorGroup, buttons)

        if check:
            self.game.changeGameState(MainMenuState(self.game))

    def playGameMode(self):
        self.game.changeGameState(PlayState(self.game))

    def bestGameMode(self):
        self.game.changeGameState(BestScoreState(self.game))

    def helpGameMode(self):
        pass

    def exitGameMode(self):
        self.game.changeGameState(ExitState(self.game))


class Save:
    def __init__(self):
        self.file = shelve.open('highscore')

    def save(self, table):
        self.file['score'] = table

    def add(self, name, value):
        self.file[name] = value

    def get(self, name):
        return self.file[name]

    def __del__(self):
        self.file.close()


class HighscoreTable:
    def __init__(self, table):
        self.hsTable = table

    def update(self, name, score):
        self.hsTable[name] = score

    def print(self, x, y):
        stepX = 300
        stepY = 30
        self.sortedHsTable = {}

        sortedKeys = sorted(self.hsTable, key=self.hsTable.get)
        for i in sortedKeys:
            self.sortedHsTable[i] = self.hsTable[i]
        for name, score in reversed(self.sortedHsTable.items()):
            buttons.drawText(name, 30, x, y)
            x += stepX
            buttons.drawText(str(score), 30, x, y)
            x -= stepX
            y += stepY


class ExitState(State):
    def __init__(self, game):
        self.game = game

    def backToIntroMode(self):
        self.game.changeGameState(MainMenuState(self.game))

    def enterNewScreen(self):
        pygame.display.set_caption('EXIT')
        check = exitMenu(screen, sounds, cursorGroup, buttons)
        if check == 1:
            pygame.quit()
        elif check == 2:
            self.game.changeGameState(MainMenuState(self.game))
        elif check == 0:
            self.game.changeGameState(MainMenuState(self.game))

    def playGameMode(self):
        pass

    def bestGameMode(self):
        pass

    def helpGameMode(self):
        pass

    def exitGameMode(self):
        pass
