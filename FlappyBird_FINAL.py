import time
import pygame
import datetime
import random


p = pygame
pygame.init()
displayWidth = 500
displayHeight = 600
# Colors
WHITE = (255,255,255,255)
BLACK = (0, 0, 0)
GREEN = (64, 255, 0)
RED = (255, 0, 0)
BRIGHTRED = (255, 179, 179)
BRIGHTGREEN = (102, 255, 51)

clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Sans", 20)
TEXT_COLOR = (0, 0, 0)


# playerWidth = 10
# playerHeight = 10
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Flappy Bob")

logo = p.image.load('flappyBOB.png')
logo = p.transform.scale(logo, (350, 150))
logo = p.transform.scale(logo, (350, 150))
background_image = p.image.load('background.png')
background_image = p.transform.scale(background_image, (500, 700))
pauseScreen = p.image.load("pauseScreen.png")
pauseScreen = p.transform.scale(pauseScreen, (500, 700))
crashScreen = p.image.load("crashScreen.png")
crashScreen = p.transform.scale(crashScreen, (500, 700))


# Normal birdie
flappy1 = p.image.load('flappy1.png')
flappy1 = p.transform.scale(flappy1, (100, 100))
flappy2 = p.image.load('flappy2.png')
flappy2 = p.transform.scale(flappy2, (100, 100))

# Ghost bird
ghostBird1 = p.image.load('ghostBird1.png')
ghostBird1 = p.transform.scale(ghostBird1, (100, 100))
ghostBird2 = p.image.load('ghostBird2.png')
ghostBird2 = p.transform.scale(ghostBird2, (100, 100))

# Pipes
obsImg = p.image.load('PIPE001.png')
obsImg = p.transform.scale(obsImg, (100, 600))
obsImg2 = p.image.load('PIPE002.png')
obsImg2 = p.transform.scale(obsImg2, (100, 600))

# Power Ups
powerBall = p.image.load('electricSign1.png')
powerBall = p.transform.scale(powerBall, (50, 50))

# Sound files
swing = pygame.mixer.Sound('sfx_wing.wav')
gotPoint = pygame.mixer.Sound('sfx_point.wav')
gotHit = pygame.mixer.Sound('sfx_hit.wav')

# Buttons
playBtn1 = pygame.image.load("playButton1.png")
playBtn1 = pygame.transform.scale(playBtn1, (120, 70))
playBtn2 = pygame.image.load("playButton2.png")
playBtn2 = pygame.transform.scale(playBtn2, (120, 70))

quitBtn1 = pygame.image.load("quitButton1.png")
quitBtn1 = pygame.transform.scale(quitBtn1, (120, 70))
quitBtn2 = pygame.image.load("quitButton2.png")
quitBtn2 = pygame.transform.scale(quitBtn2, (120, 70))

quotes = ["Poor Bird", "Pathetic", "I am sorry", "Try Harder", "You best?", "Pfffff"]

# Below code is to reset the high-score every time opening the game
# fileOne = open("HScore.txt", "w")
# fileOne.write("0")
# fileOne.close()
# fileOne = open("HScore.txt", "r")
#
# global high_score

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)  # Define fonts color
    return textSurface, textSurface.get_rect()


def message_display(text, font_size, fontX, fontY, color, font = None):
    if font == None:
        largeText = pygame.font.Font('freesansbold.ttf', font_size)  # Define font type and size
        TextSurf, TextRect = text_objects(text, largeText, color)  # Create text as object
        TextRect.center = (fontX, fontY)  # Define where texts will appear
        gameDisplay.blit(TextSurf, TextRect)  # Display text
        pygame.display.update()
    elif font != None:
        largeText = pygame.font.Font(font, font_size)  # Define font type and size
        TextSurf, TextRect = text_objects(text, largeText, color)  # Create text as object
        TextRect.center = (fontX, fontY)  # Define where texts will appear
        gameDisplay.blit(TextSurf, TextRect)  # Display text
        pygame.display.update()


def playButton(x, y, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+110 > mouse[0] > x and y+70 > mouse[1] > y:
        gameDisplay.blit(playBtn2, (x, y))


        if click[0] == 1 and action != None:
            action()
    else:

        gameDisplay.blit(playBtn1, (x, y))
    # clock.tick(60)
    pygame.display.update()


def quitButton(x, y, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+110 > mouse[0] > x and y+70 > mouse[1] > y:
        # pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        gameDisplay.blit(quitBtn2, (x, y))


        if click[0] == 1 and action != None:
            action()
    else:
        # pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        gameDisplay.blit(quitBtn1, (x, y))
    # clock.tick(60)
    pygame.display.update()


def quitgame():
    pygame.quit()
    quit()


def crash(score):
    # message_display("You are Dead", 75, displayWidth/2, 200, "ShareTechMono-Regular.ttf")
    gameDisplay.blit(crashScreen, [0,0])
    global high_score   # Most important part of calling global variables
    if score > high_score:
        fileTwo = open("HScore.txt", "w")
        fileTwo.write(str(score))
        fileTwo.close()

        fileOne = open("HScore.txt", "r")
        high_score = fileOne.read()
        fileOne.close()

    if len(str(score)) <= 1:
        message_display(" "+str(score), 50, displayWidth / 2 + 105, 275, BLACK, "slkscr.ttf")
        if len(str(high_score)) <= 1:
            message_display(" "+str(high_score), 50, (displayWidth / 2) + 105, 322, BLACK, "slkscr.ttf")
        elif len(str(high_score)) >= 2:
            message_display(str(high_score), 50, (displayWidth / 2) + 100, 322, BLACK, "slkscr.ttf")
    elif len(str(score)) >= 1:
        message_display(" "+str(score), 50, displayWidth / 2 + 90, 275, BLACK, "slkscr.ttf")
        if len(str(high_score)) <= 1:
            message_display(" "+str(high_score), 50, (displayWidth / 2) + 105, 322, BLACK, "slkscr.ttf")
        elif len(str(high_score)) >= 2:
            message_display(str(high_score), 50, (displayWidth / 2) + 100, 322, BLACK, "slkscr.ttf")
    # message_display(" " + str(score), 50, displayWidth / 2 + 105, 275, BLACK, "slkscr.ttf")
    # message_display(" " + str(high_score), 50, (displayWidth / 2) + 105, 322, BLACK, "slkscr.ttf")
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                quit()
        # button("Play Again", 100, 400, 100, 50, GREEN, BRIGHTGREEN, mainLoop)
        playButton(100, 400, mainLoop)
        quitButton(280, 400, quitgame)
        # button("Quit", 300, 400, 100, 50, RED, BRIGHTRED, quitgame)
        pygame.display.update()
        # clock.tick(60)


def paused(score):
    gameDisplay.blit(pauseScreen, [0,0])
    # message_display("Pause", 200, displayWidth/2, 230, WHITE, "FlappyBirdy.ttf")
    message_display(str(score), 50, displayWidth/2+100, 266, BLACK, "slkscr.ttf")
    # message_display(str(high_score), 50, (displayWidth/2)+100, 322, BLACK, "slkscr.ttf")
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pause_quit = True
                pygame.quit()
                quit()
        playButton(100, 400, unpause)
        quitButton(280, 400, quitgame)
        pygame.display.update()


def unpause():
    global pause
    pause = False


def setI(SET, y1, y10, overFrame1, difficulty, easy_generator1, easy_hard_generator23):

    easy_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    easy_list2 = [1, 4, 7]

    hard_list = [3, 6, 9]
    hard_list2 = [2, 5, 8]


    if overFrame1 == True:
        if SET == 1 or SET == 2 or SET == 3:
            y1 = 400
            y10 = -400
            if difficulty == "easy":
                if SET == 1:
                    SET = easy_list[easy_generator1]
                elif SET == 2:
                    SET = easy_list2[easy_hard_generator23]
                elif SET == 3:
                    SET = easy_list2[easy_hard_generator23]
            elif difficulty == "hard":
                if SET == 1:
                    SET = easy_list[easy_generator1]
                elif SET == 2:
                    SET = hard_list[easy_hard_generator23]
                elif SET == 3:
                    SET = easy_list2[easy_hard_generator23]
        elif SET == 4 or SET == 5 or SET == 6:
            y1 = 300
            y10 = -500
            if difficulty == "easy":
                if SET == 4:
                    SET = easy_list[easy_generator1]
                elif SET == 5:
                    SET = easy_list2[easy_hard_generator23]
                elif SET == 6:
                    SET = easy_list2[easy_hard_generator23]
            elif difficulty == "hard":
                if SET == 4:
                    SET = easy_list[easy_generator1]
                elif SET == 5:
                    SET = hard_list[easy_hard_generator23]
                elif SET == 6:
                    SET = hard_list2[easy_hard_generator23]
        elif SET == 7 or SET == 8 or SET == 9:
            y1 = 500
            y10 = -300
            if difficulty == "easy":
                if SET == 7:
                    SET = easy_list[easy_generator1]
                elif SET == 8:
                    SET = easy_list2[easy_hard_generator23]
                elif SET == 9:
                    SET = easy_list2[easy_hard_generator23]
            elif difficulty == "hard":
                if SET == 7:
                    SET = easy_list[easy_generator1]
                elif SET == 8:
                    SET = hard_list[easy_hard_generator23]
                elif SET == 9:
                    SET = hard_list2[easy_hard_generator23]

        # overFrame1 = False
    return y1, y10, SET


def setII(SET2, y2, y102, overFrame2, difficulty, easy_generator1, easy_hard_generator23):
    easy_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    easy_list2 = [1, 4, 7]

    hard_list = [3, 6, 9]
    hard_list2 = [2, 5, 8]

    if overFrame2 == True:
        if SET2 == 1 or SET2 == 4 or SET2 == 7:
            y2 = 400
            y102 = -400
            if difficulty == "easy":
                if SET2 == 1:
                    SET2 = easy_list[easy_generator1]
                elif SET2 == 4:
                    SET2 = easy_list[easy_generator1]
                elif SET2 == 7:
                    SET2 = easy_list[easy_generator1]
            elif difficulty == "hard":
                if SET2 == 1:
                    SET2 = easy_list[easy_generator1]
                elif SET2 == 4:
                    SET2 = easy_list[easy_generator1]
                elif SET2 == 7:
                    SET2 = easy_list[easy_generator1]
        elif SET2 == 2 or SET2 == 5 or SET2 == 8:
            y2 = 300
            y102 = -500
            if difficulty == "easy":
                if SET2 == 2:
                   SET2 = easy_list2[easy_hard_generator23]
                elif SET2 == 5:
                    SET2 = easy_list2[easy_hard_generator23]
                elif SET2 == 8:
                    SET2= easy_list2[easy_hard_generator23]
            if difficulty == "hard":
                if SET2 == 2:
                   SET2 = hard_list[easy_hard_generator23]
                elif SET2 == 5:
                    SET2 = hard_list[easy_hard_generator23]
                elif SET2 == 8:
                    SET2= hard_list[easy_hard_generator23]
        elif SET2 == 3 or SET2 == 6 or SET2 == 9:
            y2 = 500
            y102 = -300
            if difficulty == "easy":
                if SET2 == 3:
                    SET2 = easy_list2[easy_hard_generator23]
                elif SET2 == 6:
                   SET2 = easy_list2[easy_hard_generator23]
                elif SET2 == 9:
                   SET2 = easy_list2[easy_hard_generator23]
            elif difficulty == "hard":
                if SET2 == 3:
                    SET2 = hard_list2[easy_hard_generator23]
                elif SET2 == 6:
                   SET2 = hard_list2[easy_hard_generator23]
                elif SET2 == 9:
                   SET2 = hard_list2[easy_hard_generator23]

    return y2, y102, SET2


def logoDisplay(logoX, logoY, gameStarted):
    if gameStarted == False:
        gameDisplay.blit(logo, (logoX, logoY))


def flap(playerX, playerY, state1, isEaten):
    if isEaten == True:
        displayBird1 = ghostBird1
        displayBird2 = ghostBird2
        if state1 == True:
            gameDisplay.blit(displayBird1, (playerX, playerY))
        elif state1 == False:
            gameDisplay.blit(displayBird2, (playerX, playerY))
    elif isEaten == False:
        displayBird1 = flappy1
        displayBird2 = flappy2
        if state1 == True:
            gameDisplay.blit(displayBird1, (playerX, playerY))
        elif state1 == False:
            gameDisplay.blit(displayBird2, (playerX, playerY))


def powerComing(playerX, playerY, powerBallX, powerBallY, powerSpeed, gameStarted, farFromEdge, isEaten, lastingPower):

    if isEaten == False:
        if ((powerBallX + 30 < playerX + 100 < powerBallX + 60) and (powerBallY + 30 < playerY + 90 < powerBallY + 60)
                                                                or
                (powerBallX + 30 < playerX + 100 < powerBallX + 60) and (powerBallY + 30 < playerY + 20 < powerBallY + 60)
                                                                or
                (powerBallX + 30 < playerX + 20 < powerBallX + 60) and (powerBallY + 30 < playerY + 90 < powerBallY + 60)
                                                                or
                (powerBallX + 30 < playerX + 20 < powerBallX + 60) and (powerBallY + 30 < playerY + 20 < powerBallY + 60)):
            isEaten = True
            lastingPower = datetime.datetime.utcnow() + datetime.timedelta(seconds=3)

    if gameStarted == True and isEaten == False:
        powerBallX += powerSpeed
        gameDisplay.blit(powerBall, (powerBallX, powerBallY))

    if powerBallX == -100 or isEaten == True:
        powerBallX = displayWidth + farFromEdge


    return powerBallX, powerBallY, farFromEdge, isEaten, lastingPower


def scoreCount(score):
    message_display(str(score), 100, displayWidth / 2, 70, WHITE, "slkscr.ttf")
    pygame.display.update()


def pipes1(playerX, playerY, x1, y1, speed, score, isEaten):
    gameExit = False
    x1 += speed

    if isEaten == False:
        if (((x1 + 35 < playerX + 110 < x1 + 100) and (y1 - 70 < playerY < y1+793)) or
            ((x1 + 35 < playerX + 20 < x1 + 100) and (y1 - 70  < playerY < y1+793))):
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(gotHit)

                crash(score)
                gameExit = True

    if playerY == displayHeight - 30:
        pygame.mixer.Sound.play(gotHit)
        crash(score)
        gameExit = True
    if x1 + 40 < playerX < x1 + 45:
        pygame.mixer.Sound.play(gotPoint)
        score += 1
    gameDisplay.blit(obsImg, (x1, y1))
    return x1, y1, gameExit, score


def pipes2(playerX, playerY, x10, y10, speed, score, isEaten):
    gameExit = False

    # pipeHeight = 321 + y10 - 39
    x10 += speed
    if isEaten == False:
        if (((x10 + 35 < playerX + 110 < x10 + 90) and (y10 - 70 < playerY < y10 + 572)) or
            ((x10 + 35 < playerX + 20 < x10 + 90) and (y10 - 70 < playerY < y10 + 572))):
            # pygame.mixer.music.stop()

            pygame.mixer.Sound.play(gotHit)

            crash(score)
            # time.sleep(1)
            gameExit = True


    gameDisplay.blit(obsImg2, (x10, y10))
    return x10, y10, gameExit


def mainLoop():
    global pause
    pause = False
    gravity = 5
    speed = -4
    score = 0
    fileOne = open("HScore.txt", "r")
    global high_score
    high_score = int(fileOne.read())





    playerX = (displayWidth * 0.4)
    playerY = (displayHeight * 0.4)
    y_change = 0


    # Coordinates
    SET = 1
    SET2 = 1
    x1 = displayWidth + 250
    y1 = 400
    x2 = x1 + 250
    y2 = 400


    x10 = displayWidth + 250
    y10 = -400
    x102 = x10 + 250
    y102 = -400

    logoX = (displayWidth * 0.16)
    logoY = 30


    gameExit = False
    state1 = True
    gameStarted = False

    # Below code is for eating powerball
    farFromEdge = random.randint(500, 800)
    isEaten = False
    powerBallX = displayWidth + farFromEdge
    powerBallY = displayHeight * 0.5
    powerSpeed = -4

    lastingPower = None
    overFrame1 = False
    overFrame2 = False

    difficulty = "easy"

    while not gameExit:
        farFromEdge = random.randint(1000, 2000)
        easy_generator1 = random.randint(0, 8)
        easy_hard_generator23 = random.randint(0, 2)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameStarted = True
                    state1 = False
                    pygame.mixer.Sound.play(swing)
                    if score > 20:
                        y_change = -7
                    else:
                        y_change = -5
                if event.key == pygame.K_p:
                    pause = True
                    paused(score)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    state1 = True
                    y_change = gravity

        playerY += y_change
        gameDisplay.blit(background_image, [0,0])
        # gameDisplay.blit(waiting, [0, 100])
        if playerY <= 0:
            playerY = 0
        if playerY >= displayHeight-20:
            playerY = displayHeight-30


        powerBallX, powerBallY, farFromEdge, isEaten, lastingPower = powerComing(playerX, playerY, powerBallX,
                                                                                 powerBallY, powerSpeed,
                                                                                 gameStarted, farFromEdge,
                                                                                 isEaten, lastingPower)
        if isEaten == True and datetime.datetime.utcnow() > lastingPower:
            isEaten = False

        logoDisplay(logoX, logoY, gameStarted)
        flap(playerX, playerY, state1, isEaten)

        if (x1 <= -100 and x10 <= -100) and overFrame1 == False:
            x1 = displayWidth * 0.9
            x10 = displayWidth * 0.9
            overFrame1 = True
        if (x2 <= -100 and x102 <= -100) and overFrame2 == False:
            x2 = displayWidth * 0.9
            x102 = displayWidth * 0.9
            overFrame2 = True
        if overFrame1 == True:
            y1, y10, SET = setI(SET, y1, y10, overFrame1, difficulty, easy_generator1, easy_hard_generator23)
            overFrame1 = False
        if overFrame2 == True:
            y2, y102, SET2 = setII(SET2, y2, y102, overFrame2, difficulty, easy_generator1, easy_hard_generator23)
            overFrame2 = False


        if not gameExit and gameStarted == True:
            x1, y1, gameExit, score = pipes1(playerX, playerY, x1, y1, speed, score, isEaten)
        if not gameExit and gameStarted == True:
            x2, y2, gameExit, score = pipes1(playerX, playerY, x2, y2, speed, score, isEaten)
        if not gameExit and gameStarted == True:
            x10, y10, gameExit = pipes2(playerX, playerY, x10, y10, speed, score, isEaten)
        if not gameExit and gameStarted == True:
            x102, y102, gameExit = pipes2(playerX, playerY, x102, y102, speed, score, isEaten)


        if score > 20:
            speed = -5
            gravity = 4
            powerSpeed = -3
        elif score > 30:
            difficulty = "hard"
            speed = -10
            gravity = 4
            powerSpeed = -5
        elif 10 < score <= 15:
            difficulty = "hard"

        if gameStarted == True and pause == False:
            scoreCount(score)


        pygame.display.update()


mainLoop()
pygame.quit()
quit()