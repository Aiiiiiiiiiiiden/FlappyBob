# Title - Below Pipes
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

# Player Identities
flappy1 = pygame.image.load('flappy1.png')
flappy1 = pygame.transform.scale(flappy1, (100, 100))
flappy2 = pygame.image.load('flappy2.png')
flappy2 = pygame.transform.scale(flappy2, (100, 100))

# Pipes
obsImg = pygame.image.load('PIPE001.png')
obsImg = pygame.transform.scale(obsImg, (100, 600))

# Sound files
swing = pygame.mixer.Sound('sfx_wing.wav')
gotPoint = pygame.mixer.Sound('sfx_point.wav')
gotHit = pygame.mixer.Sound('sfx_hit.wav')



# Flapping effects function
def flap(playerX, playerY, state1):

        # displayBird1 is a bird with no flapping
        # displayBird2 is a bird with flapping state
        # ( Reason why displayBird1 & 2 variables are created is to change it to Ghost bird later on)
        #
        displayBird1 = flappy1
        displayBird2 = flappy2
        if state1 == True:
            gameDisplay.blit(displayBird1, (playerX, playerY))
        elif state1 == False:
            gameDisplay.blit(displayBird2, (playerX, playerY))


# Two pipes for up and down (A pair of pipes)
def pipes1(playerX, playerY, x1, y1, speed):
    gameExit = False
    x1 += speed

    # Condition for Collision between bird and pipe
    if (((x1 + 35 < playerX + 110 < x1 + 100) and (y1 - 70 < playerY < y1 + 793)) or
            ((x1 + 35 < playerX + 20 < x1 + 100) and (y1 - 70 < playerY < y1 + 793))):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(gotHit)
        gameExit = True


    # Collision of player and ground
    if playerY == displayHeight - 30:
        pygame.mixer.Sound.play(gotHit)
        gameExit = True


    gameDisplay.blit(obsImg, (x1, y1))
    return x1, y1, gameExit

# Main loop to run a game
def mainLoop():

 # You know what this is....Right! Newton's first baby
    gravity = 3

 # Speed of every pipes in a game
    speed = -4

 # Player's coordinates
    playerX = (displayWidth * 0.4)
    playerY = (displayHeight * 0.4)
    y_change = 0


 # Pipes' coordinates
    # x1, y1 are for first below pipe
    x1 = displayWidth + 250
    y1 = 400
    # x2, y2 are for second below pipe
    x2 = x1 + 300
    y2 = 400



  # gameStarted is to make sure to start a game or not
  # (Otherwise pipes will be going through since the games is started running)
    gameStarted = False

  # gameExit is to make sure whether game is exited or not
    gameExit = False

  # State 1 means the initial state or freely falling state (Not flapping state)
    state1 = True

    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state1 = False
                    gameStarted = True
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

        # To repeat the same pipe back to the screen
        if x1 < -80:
            x1 = displayWidth
        if x2 < -80:
            x2 = displayWidth


        flap(playerX, playerY, state1)



     # Calling pipe function for two pipes for now (both on the ground)
        if not gameExit and gameStarted == True:
            x1, y1, gameExit = pipes1(playerX, playerY, x1, y1, speed)
        if not gameExit and gameStarted == True:
            x2, y2, gameExit = pipes1(playerX, playerY, x2, y2, speed)


        pygame.display.update()

mainLoop()
pygame.quit()
quit()

