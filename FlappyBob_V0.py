# Title - Background
#
# Credited to
# Hein Khant Zaw | ID - 6118157 | VMS Student | Assumption University

import pygame


pygame.init()


# Width and Height of the game window
displayWidth = 500
displayHeight = 600

# Setting up environment
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Flappy Bob")
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (500, 700))


def mainLoop():

    gameExit = False


    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True


        gameDisplay.blit(background_image, [0,0])
        pygame.display.update()

mainLoop()
pygame.quit()
quit()