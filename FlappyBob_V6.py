# Title - Starting Screen or Adding logo
#
# Credited to
# Hein Khant Zaw | ID - 6118157 | VMS Student | Assumption University

import random
import pygame
import datetime

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

# Ghost bird
ghostBird1 = pygame.image.load('ghostBird1.png')
ghostBird1 = pygame.transform.scale(ghostBird1, (100, 100))
ghostBird2 = pygame.image.load('ghostBird2.png')
ghostBird2 = pygame.transform.scale(ghostBird2, (100, 100))

# Pipes declaration of images
obsImg = pygame.image.load('PIPE001.png')
obsImg = pygame.transform.scale(obsImg, (100, 600))
obsImg2 = pygame.image.load('PIPE002.png')
obsImg2 = pygame.transform.scale(obsImg2, (100, 600))

# Power Ups
powerBall = pygame.image.load('electricSign1.png')
powerBall = pygame.transform.scale(powerBall, (50, 50))

# Sound files
swing = pygame.mixer.Sound('sfx_wing.wav')
gotPoint = pygame.mixer.Sound('sfx_point.wav')
gotHit = pygame.mixer.Sound('sfx_hit.wav')


# For Starting screen and Pause screen
logo = pygame.image.load('flappyBOB.png')
logo = pygame.transform.scale(logo, (350, 150))
logo = pygame.transform.scale(logo, (350, 150))
pauseScreen = pygame.image.load("pauseScreen.png")
pauseScreen = pygame.transform.scale(pauseScreen, (500, 700))
crashScreen = pygame.image.load("crashScreen.png")
crashScreen = pygame.transform.scale(crashScreen, (500, 700))


# Colors
WHITE = (255, 255, 255, 255)


# Flapping effects function
def flap(playerX, playerY, state1, isEaten):
    if isEaten == False:
        displayBird1 = flappy1
        displayBird2 = flappy2
        if state1 == True:
            gameDisplay.blit(displayBird1, (playerX, playerY))
        elif state1 == False:
            gameDisplay.blit(displayBird2, (playerX, playerY))
    elif isEaten == True:
        displayBird1 = ghostBird1
        displayBird2 = ghostBird2
        if state1 == True:
            gameDisplay.blit(displayBird1, (playerX, playerY))
        elif state1 == False:
            gameDisplay.blit(displayBird2, (playerX, playerY))


# Two pipes for up and down (A pair of pipes)
def pipes1(playerX, playerY, x1, y1, speed, score, isEaten):
    gameExit = False
    x1 += speed

    # Condition for Collision between bird and pipe
    # Add if player ate powerball or not
    if isEaten == False:
        if (((x1 + 35 < playerX + 110 < x1 + 100) and (y1 - 70 < playerY < y1 + 793)) or
                ((x1 + 35 < playerX + 20 < x1 + 100) and (y1 - 70 < playerY < y1 + 793))):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(gotHit)
            gameExit = True

    # Collision of player and ground
    if playerY == displayHeight - 30:
        pygame.mixer.Sound.play(gotHit)
        gameExit = True

    # Condition to check if bird has passed the pipe
    if x1 + 40 < playerX < x1 + 45:
        # Add sound every time bird passes the pipe
        pygame.mixer.Sound.play(gotPoint)
        # Add score to one
        score += 1

    gameDisplay.blit(obsImg, (x1, y1))
    return x1, y1, score, gameExit


def pipes2(playerX, playerY, x10, y10, speed, isEaten):
    gameExit = False

    pipeHeight = 321 + y10 - 39
    x10 += speed
    if isEaten == False:
        if (((x10 + 35 < playerX + 110 < x10 + 90) and (y10 - 70 < playerY < y10 + 572)) or
                ((x10 + 35 < playerX + 20 < x10 + 90) and (y10 - 70 < playerY < y10 + 572))):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(gotHit)
            gameExit = True
    gameDisplay.blit(obsImg2, (x10, y10))
    return x10, y10, gameExit


def powerComing(playerX, playerY, powerBallX, powerBallY, powerSpeed, gameStarted, farFromEdge, isEaten, lastingPower):
    if isEaten == False:
        if ((powerBallX + 30 < playerX + 100 < powerBallX + 60) and (powerBallY + 30 < playerY + 90 < powerBallY + 60)
                or
                (powerBallX + 30 < playerX + 100 < powerBallX + 60) and (
                        powerBallY + 30 < playerY + 20 < powerBallY + 60)
                or
                (powerBallX + 30 < playerX + 20 < powerBallX + 60) and (
                        powerBallY + 30 < playerY + 90 < powerBallY + 60)
                or
                (powerBallX + 30 < playerX + 20 < powerBallX + 60) and (
                        powerBallY + 30 < playerY + 20 < powerBallY + 60)):
            isEaten = True
            lastingPower = datetime.datetime.utcnow() + datetime.timedelta(seconds=3)

    if gameStarted == True and isEaten == False:
        powerBallX += powerSpeed
        gameDisplay.blit(powerBall, (powerBallX, powerBallY))

    if powerBallX == -100 or isEaten == True:
        powerBallX = displayWidth + farFromEdge

    return powerBallX, powerBallY, farFromEdge, isEaten, lastingPower


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)  # Define fonts color
    return textSurface, textSurface.get_rect()


# A Function to display text on the screen
# message_display function needs 5 or 6 parameters
# font can be null and valid
# If function is called with null value of font, "freesansbold.ttf" will be the default font
def message_display(text, font_size, fontX, fontY, color, font = None):
    # Default font
    if font == None:
        largeText = pygame.font.Font('freesansbold.ttf', font_size)  # Define font type and size
        TextSurf, TextRect = text_objects(text, largeText, color)  # Create text as object
        TextRect.center = (fontX, fontY)  # Define where texts will appear
        gameDisplay.blit(TextSurf, TextRect)  # Display text
        pygame.display.update()
    # Specified font
    elif font != None:
        largeText = pygame.font.Font(font, font_size)  # Define font type and size
        TextSurf, TextRect = text_objects(text, largeText, color)  # Create text as object
        TextRect.center = (fontX, fontY)  # Define where texts will appear
        gameDisplay.blit(TextSurf, TextRect)  # Display text
        pygame.display.update()


def scoreCount(score):
    # Display score with specified font (flappy bird font)
    message_display(str(score), 100, displayWidth / 2, 70, WHITE, "slkscr.ttf")
    pygame.display.update()


# Function to display Logo in Starting screen
def logoDisplay(logoX, logoY, gameStarted):
    if gameStarted == False:
        gameDisplay.blit(logo, (logoX, logoY))


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

    # x10, y10 are for first above pipe
    x10 = displayWidth + 250
    y10 = -400
    # x102, y102 are for second above pipe
    x102 = x10 + 300
    y102 = -400

    # farFromEdge variable is to set the distance of powerball from the edge
    farFromEdge = displayWidth + 500
    # isEaten is to determine whether Bob ate the powerball or not
    isEaten = False

    # These are the initial values of coordinates of powerball
    powerBallX = displayWidth + farFromEdge
    powerBallY = displayHeight * 0.5
    powerSpeed = -4
    # lastingPower is to determine how long powerball will last after eaten
    lastingPower = None

    # gameStarted is to make sure to start a game or not
    # (Otherwise pipes will be going through since the games is started running)
    gameStarted = False

    # gameExit is to make sure whether game is exited or not
    gameExit = False

    # State 1 means the initial state or freely falling state (Not flapping state)
    state1 = True

    # Score to count every time bird has passed each pipes
    score = 0

    # X and Y coordinates for logo
    # This can be done by putting the exact value directly to the parentheses
    # But to be clean, I created two variables as can be seen below
    logoX = (displayWidth * 0.16)
    logoY = 30

    while not gameExit:
        # Random the distance of powerball from the edge every loop
        farFromEdge = random.randint(1000, 2000)

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
        gameDisplay.blit(background_image, [0, 0])
        if playerY <= 0:
            playerY = 0
        if playerY >= displayHeight - 20:
            playerY = displayHeight - 30

        # To repeat the same pipe back to the screen
        # For below pipe
        if x1 < -80:
            x1 = displayWidth
        if x2 < -80:
            x2 = displayWidth

        if x10 < -80:
            x10 = displayWidth
        if x102 < -80:
            x102 = displayWidth
        flap(playerX, playerY, state1, isEaten)

        # To display Logo when game hasn't been started yet
        logoDisplay(logoX, logoY, gameStarted)



        powerBallX, powerBallY, farFromEdge, isEaten, lastingPower = powerComing(playerX, playerY, powerBallX,
                                                                                 powerBallY, powerSpeed,
                                                                                 gameStarted, farFromEdge,
                                                                                 isEaten, lastingPower)


        # Condition to check whether if time is up for powerball lasting
        # If time has run out, turn isEaten to False
        if isEaten == True and datetime.datetime.utcnow() > lastingPower:
            isEaten = False


        # Calling pipe function for two pipes for now (both on the ground)
        # For below pipe
        # Add score variable to pipe function as argument
        # Return the score as it has to be updated
        # (Reminder: You can just add to under function since it is no need)
        if not gameExit and gameStarted == True:
            x1, y1, score, gameExit = pipes1(playerX, playerY, x1, y1, speed, score, isEaten)
        if not gameExit and gameStarted == True:
            x2, y2, score, gameExit = pipes1(playerX, playerY, x2, y2, speed, score, isEaten)
        # For above pipe
        if not gameExit and gameStarted == True:
            x10, y10, gameExit = pipes2(playerX, playerY, x10, y10, speed, isEaten)
        if not gameExit and gameStarted == True:
            x102, y102, gameExit = pipes2(playerX, playerY, x102, y102, speed, isEaten)

        # scoreCount function should be called after every functions since it should be on above all (bird, pipes, background)
        # Otherwise, pipes will be glitched in every loop ( if it is called just before pipes)
        #
        # scoreCount() function is called if game is started (Otherwise 0 will be displayed on the screen though game hasn't started yet)
        if gameStarted == True:
            scoreCount(score)
        pygame.display.update()


mainLoop()
pygame.quit()
quit()

