import pygame


def pauseMenu(screen, sounds, buttons, cursor):
    running = True
    pygame.mouse.set_visible(False)

    sounds.mainTheme.play(-1)

    backGround = pygame.transform.scale(pygame.image.load('images/pauseBackground/pause.png'), (800, 600))
    backGroundRect = backGround.get_rect()

    while running:
        screen.fill((255, 204, 255))
        screen.blit(backGround, backGroundRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.mainTheme.stop()
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.pauseButtons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.mainTheme.stop()
                        sounds.buttonClick.play()
                        running = False
                        return 1
                elif buttons.pauseButtons[1].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.mainTheme.stop()
                        sounds.buttonClick.play()
                        running = False
                        return 2

        font = pygame.font.Font(None, 60)
        di = font.render('Main Menu', True, '#FFE80E')
        diRect = di.get_rect(center=(400, 270))
        buttons.pauseButtons.append(diRect)
        screen.blit(di, diRect)

        font2 = pygame.font.Font(None, 60)
        di2 = font2.render('Exit', True, '#FFE80E')
        di2Rect = di2.get_rect(center=(400, 370))
        buttons.pauseButtons.append(di2Rect)
        screen.blit(di2, di2Rect)
        cursor.draw(screen)
        cursor.update()
        pygame.display.flip()
