import pygame

from settings.buttons import *


def nameManuLoop(screen, sounds):
    processing = True
    userName = '|'
    userTick = 30
    boxWidth = True
    backGround4 = pygame.transform.scale(pygame.image.load('images/helpBackground/helpBack.png'), (800, 600))
    backGroundRect = backGround4.get_rect()

    pygame.mouse.set_visible(False)
    while processing:
        screen.fill((90, 22, 45))
        screen.blit(backGround4, backGroundRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                processing = False


            elif event.type == pygame.KEYDOWN:
                userName = userName.replace('|', '')
                userTick = 150
                if event.key == pygame.K_RETURN:
                    processing = False

                    if len(userName) == 0:
                        userName = 'NO NAME'
                    return True, userName
                elif event.key == pygame.K_ESCAPE:
                    processing = False
                    if len(userName) == 0:
                        userName = 'NO NAME'
                    return False, userName
                elif event.key == pygame.K_BACKSPACE:

                    userName = userName[0:-1]
                else:

                    if boxWidth:

                        sounds.typeSound.play()
                        if len(userName) != 12:
                            userName += event.unicode
                userName += '|'

        b = Button(screen)
        font2 = pygame.font.Font(None, 30)
        bD = font2.render('ENTER USER NAME', True, '#FFE80E')
        bSurfRect = bD.get_rect(center=(540, 250))
        screen.blit(bD, bSurfRect)

        userTick -= 1
        if userTick == 0:
            userName = userName[: - 1]
        if userTick == -150:
            userName += '|'
            userTick = 150

        pygame.font.init()
        font = pygame.font.Font(None, 40)
        userNameSurf = font.render(userName, True, '#FFE80E')
        userNameRect = pygame.Rect(440, 294, 400, 50)

        screen.blit(userNameSurf, (userNameRect.x + 10, userNameRect.y + 10))

        font1 = pygame.font.Font(None, 30)
        bSurf = font1.render('Press ENTER to continue', True, '#FFE80E')
        bSurfRect = bSurf.get_rect(center=(140, 550))
        screen.blit(bSurf, bSurfRect)
        pygame.display.flip()
