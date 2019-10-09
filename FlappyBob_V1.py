# Title - Bird with Flapping feature
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

# Player declaration of images
flappy1 = pygame.image.load('flappy1.png')
flappy1 = pygame.transform.scale(flappy1, (100, 100))
flappy2 = pygame.image.load('flappy2.png')
flappy2 = pygame.transform.scale(flappy2, (100, 100))

# Sound files
swing = pygame.mixer.Sound('sfx_wing.wav')
gotPoint = pygame.mixer.Sound('sfx_point.wav')
gotHit = pygame.mixer.Sound('sfx_hit.wav')



# Flapping effects function
def flap(playerX, playerY, state1):
        displayBird1 = flappy1
        displayBird2 = flappy2
        if state1 == True:
            gameDisplay.blit(displayBird1, (playerX, playerY))
        elif state1 == False:
            gameDisplay.blit(displayBird2, (playerX, playerY))


def mainLoop():

    gravity = 10
    speed = -10


    playerX = (displayWidth * 0.4)
    playerY = (displayHeight * 0.4)
    y_change = 0



    gameExit = False
    state1 = True

    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state1 = False
                    y_change = -3
                    pygame.mixer.Sound.play(swing)



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    state1 = True
                    y_change = gravity

        playerY += y_change
        gameDisplay.blit(background_image, [0,0])
        if playerY <= 0:
            playerY = 0
        if playerY >= displayHeight-20:
            playerY = displayHeight-30


        flap(playerX, playerY, state1)
        pygame.display.update()

mainLoop()
pygame.quit()
quit()
