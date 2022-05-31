import time

from settings.buttons import *
from objects.bulletHole import Hole
from objects.chickHole import ChickHole


def mainMenuLoop(screen, sounds, cursor, cursorGroup, mainButtons, buttons, chickenHole, holes):
    processing = True

    pygame.mouse.set_visible(False)

    sounds.mainTheme.play(-1)
    back = pygame.image.load("images/mainMenuBackground/main_menu.png")
    backRect = back.get_rect()
    morhuhn = pygame.image.load("images/mainMenuBackground/moorhuhn.png")
    morhuhnRect = morhuhn.get_rect(center=(400, 66))

    newHolesMaxTime = 15
    newHolesCurrentTime = 0
    index = 0
    finish = False

    while processing:
        screen.fill((0, 100, 0))
        screen.blit(back, backRect)
        screen.blit(morhuhn, morhuhnRect)

        mainButtons.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.mainTheme.stop()
                processing = False

            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                if cursor.changeMainButton(cursor, x, y, mainButtons, 'start'):
                    break
                elif cursor.changeMainButton(cursor, x, y, mainButtons, 'score'):
                    break
                elif cursor.changeMainButton(cursor, x, y, mainButtons, 'menu'):
                    break
                elif cursor.changeMainButton(cursor, x, y, mainButtons, 'exit'):
                    break


            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if cursor.checkMainButtons(cursor, x, y, mainButtons, 'start'):
                    if event.button == 1:

                        sounds.buttonClick.play()
                        sounds.mainTheme.stop()
                        for hole in holes:
                            hole.shot()
                        processing = False

                        sounds.readyAfterUserName.play()
                        return 1

                elif cursor.checkMainButtons(cursor, x, y, mainButtons, 'score'):
                    if event.button == 1:

                        sounds.buttonClick.play()
                        sounds.mainTheme.stop()
                        processing = False
                        for hole in holes:
                            hole.shot()
                        return 2

                elif cursor.checkMainButtons(cursor, x, y, mainButtons, 'menu'):
                    if event.button == 1:
                        sounds.buttonClick.play()
                        sounds.mainTheme.stop()
                        for hole in holes:
                            hole.shot()
                        processing = False

                        return 3

                elif cursor.checkMainButtons(cursor, x, y, mainButtons, 'exit'):
                    if event.button == 1:
                        sounds.buttonClick.play()
                        sounds.mainTheme.stop()
                        for hole in holes:
                            hole.shot()
                        processing = False
                        return 4

        newHolesCurrentTime += 1
        if newHolesCurrentTime == newHolesMaxTime:
            index += 1
            newHolesCurrentTime = 0
            if index < 4:
                holes.add(Hole(screen, index))
            if index == 4:
                holes.add(Hole(screen, index))
                finish = True

        holes.update(sounds)

        chickenHole.update()

        cursorGroup.draw(screen)
        cursorGroup.update()

        pygame.display.flip()
