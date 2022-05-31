from settings.buttons import *


def recordMenu(screen, sounds, cursorGroup, buttons, userName, score, game):
    processing = True

    sounds.mainTheme.play(-1)

    backGround = pygame.transform.scale(pygame.image.load('images/helpBackground/helpBack.png'), (800, 600))
    backGroundRect = backGround.get_rect()

    while processing:
        screen.fill((90, 22, 45))
        screen.blit(backGround, backGroundRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.mainTheme.stop()
                processing = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.bestScoreButtons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.mainTheme.stop()
                        sounds.buttonClick.play()
                        processing = False
                        return True

        buttons.drawText('Best Score Table', 50, 530, 100)
        buttons.drawText(f'Name:', 30, 350, 200)
        buttons.drawText(f'Score:', 30, 650, 200)
        game.highscore.print(350, 230)
        buttons.drawBestScore('Main Menu', 40, 140, 550)

        cursorGroup.draw(screen)
        cursorGroup.update()

        pygame.display.flip()
