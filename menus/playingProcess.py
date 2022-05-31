import sys
import time

import pygame.event

from settings.timer import Timer
from objectsImports import *
from objects.background import *
from objects.trees import *

from random import randint
from objects.background import *


def playingProcess(clock, screen, sounds, buttons, cursor, cursorGroup, chickensSmallGroup, chickensMidGroup,
                   chickensBigGroup, ammo, ammoGroup, scoreManager, scoresGroup, pumpkin, signPost,
                   bigChickenGroup,
                   mill):
    sounds.backgroundTheme.play(-1)

    processing = True

    timer = Timer()

    pygame.mouse.set_visible(False)

    initTime = 0

    bigChickenTimer = 0

    ammoCount = -1

    tree1 = Tree(screen, 'images/tree/trunkBig1.png', 300, 200)
    tree2 = Tree(screen, 'images/tree/trunkSmall1.png', 1900, 100)
    trees = pygame.sprite.Group()
    trees.add(tree1)
    trees.add(tree2)

    camera1 = Camera(0, 0, 96)
    camera2 = Camera(0, 80, 1900)
    camera3 = Camera(0, 130, 890)
    camera4 = Camera(0, 160, 1900)

    processing = True
    while processing:

        dt = clock.tick(60)

        cursorX = cursor.rect.x
        if cursorX >= 750 and cursorX <= 800:
            if camera1.move(2) and camera2.move(5) and camera3.move(15) and camera4.move(40):
                chickensSmallGroup.update(dt, 'move_r')
                chickensMidGroup.update(dt, 'move_r')
                chickensBigGroup.update(dt, 'move_r')
                bigChickenGroup.update('move_r')

                mill.update('move_r')
                pumpkin.update('move_r')
                signPost.update('move_r')
                trees.update('move_r')

        elif cursorX <= 20 and cursorX >= -20:
            if camera1.move(-2) and camera2.move(-5) and camera3.move(-15) and camera4.move(-40):
                chickensSmallGroup.update(dt, 'move_l')
                chickensMidGroup.update(dt, 'move_l')
                chickensBigGroup.update(dt, 'move_l')
                bigChickenGroup.update('move_l')

                mill.update('move_l')
                pumpkin.update('move_l')
                signPost.update('move_l')
                trees.update('move_l')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.backgroundTheme.stop()
                processing = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.backgroundTheme.stop()
                    processing = False
                    return 1, 0

                elif event.key == pygame.K_SPACE:
                    if ammo.count < 8:
                        ammoCount = ammo.update(screen, ammoGroup)


            elif event.type == pygame.USEREVENT:
                chickensSmallGroup.add(SmallChicken(screen, randint(100, 200)))
                chickensMidGroup.add(MiddleChicken(screen, randint(100, 300)))
                chickensBigGroup.add(BigChicken(screen, randint(100, 500)))



            elif event.type == pygame.MOUSEBUTTONDOWN:

                check_shot, ammoCount = ammo.shot()
                x, y = event.pos

                if cursor.shootBoss(sounds, cursor, bigChickenGroup, check_shot, scoreManager, scoresGroup):
                    continue

                elif cursor.shootTree(sounds, trees, check_shot):
                    continue


                elif cursor.shootChicken(sounds, chickensBigGroup, check_shot, scoreManager, scoresGroup):
                    continue
                elif cursor.shootChicken(sounds, chickensMidGroup, check_shot, scoreManager, scoresGroup):
                    continue
                elif cursor.shootChicken(sounds, chickensSmallGroup, check_shot, scoreManager, scoresGroup):
                    continue


                elif cursor.shootMill(cursor, x, y, sounds, mill, check_shot, scoreManager, scoresGroup):
                    continue

                elif cursor.shootSignPost(sounds, signPost, check_shot, scoreManager, scoresGroup):
                    continue

                elif cursor.shootPumpkin(sounds, pumpkin, check_shot, scoreManager, scoresGroup):
                    continue

        bigChickenTimer += 1
        if bigChickenTimer == 40:
            sounds.bigChickenPopsUpSound.play()
            x = randint(100, 1700)
            bigChickenGroup.add(Boss(screen, (x, 450)))
            bigChickenTimer = -300

        initTime += 1
        if initTime == 1:
            startTime = time.time()
        playTime = round(time.time() - startTime)

        playTimeCheck = timer.timeCheck(sounds, playTime)
        if playTimeCheck == 1:
            sounds.backgroundTheme.stop()
            sounds.gameOverSound.play()
            processing = False

            return 2, scoreManager.returnScore()

        screen.fill((90, 100, 45))
        screen.blit(sky, (-camera1.rect[0], camera1.rect[1]))
        screen.blit(hills, (-camera2.rect[0], camera2.rect[1]))

        chickensSmallGroup.draw(screen)
        chickensSmallGroup.update(dt, 'no')
        screen.blit(castle, (-camera3.rect[0], camera3.rect[1]))

        chickensMidGroup.draw(screen)
        chickensMidGroup.update(dt, 'no')
        screen.blit(green, (-camera4.rect[0], camera4.rect[1]))

        pumpkin.update('no')

        mill.update('no')

        chickensBigGroup.draw(screen)
        chickensBigGroup.update(dt, 'no')

        signPost.update('no')

        scoresGroup.update()

        trees.update('no')

        buttons.drawText(f'Time: {90 - playTime}', 30, 70, 20)

        buttons.drawText(f'Score: {scoreManager.returnScore()}', 30, 710, 20)

        bigChickenGroup.update('no')

        ammoGroup.update(dt, ammoCount)

        cursorGroup.draw(screen)
        cursorGroup.update()

        pygame.display.flip()
