import pygame


# EXIT
def exitMenu(screen, sounds, cursorGroup, buttons):
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.mainTheme.stop()
                    processing = False
                    return 0


            elif event.type == pygame.MOUSEBUTTONDOWN:

                if buttons.exitButtons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.mainTheme.stop()
                        sounds.buttonClick.play()
                        processing = False
                        return 1
                # back to Main Menu
                elif buttons.exitButtons[1].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.mainTheme.stop()
                        sounds.buttonClick.play()
                        processing = False
                        return 2

        font = pygame.font.Font(None, 60)
        top = font.render('Are you sure?', True, '#FFE80E')
        topRect = top.get_rect(center=(540, 200))
        screen.blit(top, topRect)

        font2 = pygame.font.Font(None, 60)
        top1 = font2.render('Yes', True, '#FFE80E')
        top1Rect = top1.get_rect(center=(530, 280))
        buttons.exitButtons.append(top1Rect)
        screen.blit(top1, top1Rect)

        font3 = pygame.font.Font(None, 60)
        top2 = font3.render('No', True, '#FFE80E')
        top2Rect = top2.get_rect(center=(530, 350))
        buttons.exitButtons.append(top2Rect)
        screen.blit(top2, top2Rect)

        cursorGroup.draw(screen)
        cursorGroup.update()

        pygame.display.flip()
