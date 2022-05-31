import pygame


def helpMenu(screen, sounds, cursorGroup, buttons):
    processing = True

    sounds.mainTheme.play(-1)
    backGround = pygame.transform.scale(pygame.image.load('images/helpBackground/helpBack.png'), (800, 600))
    backGroundRect = backGround.get_rect()

    mouse1 = pygame.transform.flip(
        pygame.transform.scale(pygame.image.load('images/helpBackground/mouse-right-click.png').convert_alpha(),
                               (150, 100)), True, False)
    mouse1Rect = mouse1.get_rect(center=(370, 150))

    space = pygame.transform.scale(pygame.image.load('images/helpBackground/space.png').convert_alpha(), (150, 160))
    spaceRect = space.get_rect(center=(370, 330))

    esc = pygame.transform.scale(pygame.image.load('images/helpBackground/6.jpg').convert_alpha(), (90, 90))
    escRect = esc.get_rect(center=(370, 500))

    while processing:
        screen.fill((90, 15, 45))
        screen.blit(backGround, backGroundRect)
        screen.blit(mouse1, mouse1Rect)
        screen.blit(space, spaceRect)
        screen.blit(esc, escRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.mainTheme.stop()
                processing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.mainTheme.stop()
                    processing = False
                    return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.helpButtons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.mainTheme.stop()
                        sounds.buttonClick.play()
                        processing = False
                        return True

        pygame.font.init()
        font1 = pygame.font.Font(None, 50)
        ier = font1.render(' - SHOOT', True, '#FFE80E')
        ierRect = ier.get_rect(center=(520, 150))
        screen.blit(ier, ierRect)

        font2 = pygame.font.Font(None, 50)
        crr = font2.render(' - RECHARGE', True, '#FFE80E')
        crrRect = crr.get_rect(center=(580, 330))
        screen.blit(crr, crrRect)

        font3 = pygame.font.Font(None, 50)
        pp = font3.render(' - MAIN MENU', True, '#FFE80E')
        ppRect = pp.get_rect(center=(580, 500))
        screen.blit(pp, ppRect)

        cursorGroup.draw(screen)
        cursorGroup.update()

        pygame.display.flip()
