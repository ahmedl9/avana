#This is our main file 
import pygame
import serial
from MainFrame import mainFrame
from HUD import hud
from pySerialTest import myRead as read
import db
import random
from storyboard2 import StoryBoard
import time

arr = [1,2,3,4,5]
changes = {"1) Give number": [-1,-200,-900], "2) Heck No!": [1,100,-450], "1) Piggy Bank": [1,100,500], "2) Actual Bank": [-1,-200,-500], "1) Ofc Fortnite": [1, 0, -200], "2) Calculator": [-1,150,-200], "1) Capital One": [2,100,1000], "2) Irrelevant Bank": [-2,-200,-2000], "1) Electricity Bill": [-1,100,-500], "2) Pay taxes": [1,50,-500]}
myStory = StoryBoard()
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

blinktimer = 1

def renderTitle(screen, bCount):
    """
    Called in a loop, renders title page and start menu. Animates background with clouds.
    """
    if (bCount >= 0 and bCount < 10): 
        backgroundImg = pygame.image.load('Assets/background_image.png')
        screen.blit(backgroundImg, (0, 0))
    if (bCount >= 10 and bCount < 20):
        backgroundImg = pygame.image.load('Assets/background_image_1.png')
        screen.blit(backgroundImg, (0, 0))
    if (bCount >= 20 and bCount < 30):
        backgroundImg = pygame.image.load('Assets/background_image_2.png')
        screen.blit(backgroundImg, (0, 0))

    grayBG = pygame.Surface((600, 400))
    grayBG.set_alpha(128)
    grayBG.fill((105, 105, 105))
    screen.blit(grayBG, (100, 125))
    
    fontTitle = pygame.font.Font("Assets/Minecraft.ttf", 64)
    textTitle = fontTitle.render("AVANA", True, (0, 0, 0))
    screen.blit(textTitle, (300, 200))

    fontTitle = pygame.font.Font("Assets/Minecraft.ttf", 18)
    textTitle = fontTitle.render("Powered by", True, (0, 0, 0))
    screen.blit(textTitle, (350, 395))

    logoImg = pygame.image.load('Assets/capital_one_logo.png')
    screen.blit(logoImg, (320, 425))


    fontButton = pygame.font.Font("Assets/Minecraft.ttf", 24)
    textButton = fontButton.render("Start Game", True, (0, 0, 0))

    buttonImg = pygame.image.load('Assets/button.png')
    screen.blit(buttonImg, (275, 300))
    screen.blit(textButton, (330, 318))

    selectionBorder = pygame.image.load('Assets/selection.png')

    global blinktimer
    if blinktimer < 0:
        blinktimer = 8
    elif blinktimer < 4:
        blinktimer -= 1
        screen.blit(selectionBorder, (270, 295))
    else:
        blinktimer -= 1

    pygame.display.update()

def title(screen, clock):
    """
    Game manager for title animation. Calls renderTitle(). This function is called in main().
    """
    bCount = 0
    
    buttonClicked = False

    while (not buttonClicked):
        renderTitle(screen, bCount)

        joystickInput = read(ser)
        if joystickInput == "Button":

            buttonClicked = True

        bCount = bCount + 1
        if (bCount == 30):
            bCount = 0
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False
        
def pickAvatar(screen, clock):
    """
    Allows user to pick avatar using joystick. Saves choice and displays appropriate selection.
    """
    bCount = 0
    
    avatarPicked = False
    currAvatar = 1
    avatarBlinkTimer = 1

    while (not avatarPicked):
        if (bCount >= 0 and bCount < 10): 
            backgroundImg = pygame.image.load('Assets/background_image.png')
            screen.blit(backgroundImg, (0, 0))
        if (bCount >= 10 and bCount < 20):
            backgroundImg = pygame.image.load('Assets/background_image_1.png')
            screen.blit(backgroundImg, (0, 0))
        if (bCount >= 20 and bCount < 30):
            backgroundImg = pygame.image.load('Assets/background_image_2.png')
            screen.blit(backgroundImg, (0, 0))

        grayBG = pygame.Surface((600, 400))
        grayBG.set_alpha(128)
        grayBG.fill((105, 105, 105))
        screen.blit(grayBG, (100, 125))

        fontTitle = pygame.font.Font("Assets/Minecraft.ttf", 32)
        textTitle = fontTitle.render("Pick an Avatar", True, (255, 255, 255))
        screen.blit(textTitle, (275, 200))

        person1 = pygame.image.load('Assets/person1.png')
        person2 = pygame.image.load('Assets/person2.png')
        person3 = pygame.image.load('Assets/person3.png')
        person4 = pygame.image.load('Assets/person4.png')

        screen.blit(person1, (125, 275))
        screen.blit(person2, (275, 275))
        screen.blit(person3, (425, 275))
        screen.blit(person4, (575, 275))

        avatarBorder = pygame.image.load('Assets/character_selection.png')

        if avatarBlinkTimer < 0:
            avatarBlinkTimer = 8
        elif avatarBlinkTimer < 4:
            avatarBlinkTimer -= 1
            if currAvatar == 1:
                screen.blit(avatarBorder, (120, 270))
            elif currAvatar == 2:
                screen.blit(avatarBorder, (270, 270))
            elif currAvatar == 3:
                screen.blit(avatarBorder, (420, 270))
            else:
                screen.blit(avatarBorder, (570, 270))
        else:
            avatarBlinkTimer -= 1

        joystickInput = read(ser)
        if joystickInput == "Left" and currAvatar > 1:
            currAvatar -= 1
        elif joystickInput == "Right" and currAvatar < 4:
            currAvatar += 1
        elif joystickInput == "Button":
            avatarPicked = True

        bCount = bCount + 1
        if (bCount == 30):
            bCount = 0
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False

        pygame.display.update()
    return int(currAvatar)

def displayEndGame(screen, clock, avatarNum, bCount, ourHUD):
    """
    Final end game screen, connects to SQL database hosted with AWS and displays recent games.
    """
    nameSwitch = {1: "Jason", 2: "Kunal", 3: "Wes", 4: "Heidi"} 
    db.addEntry(nameSwitch[avatarNum], ourHUD.getCreditScore(), ourHUD.getBalance(), ourHUD.getHapiness())

    while (True):
        if (bCount >= 0 and bCount < 10): 
            backgroundImg = pygame.image.load('Assets/background_image.png')
            screen.blit(backgroundImg, (0, 0))
        if (bCount >= 10 and bCount < 20):
            backgroundImg = pygame.image.load('Assets/background_image_1.png')
            screen.blit(backgroundImg, (0, 0))
        if (bCount >= 20 and bCount < 30):
            backgroundImg = pygame.image.load('Assets/background_image_2.png')
            screen.blit(backgroundImg, (0, 0))

        grayBG = pygame.Surface((600, 400))
        grayBG.set_alpha(128)
        grayBG.fill((105, 105, 105))
        screen.blit(grayBG, (100, 125))

        leaders = db.getEntries()
        numSwitch = {"Jason" : 1, "Kunal" : 2, "Wes" : 3, "Heidi" : 4} 
        person1 = pygame.image.load('Assets/person' + str(numSwitch[leaders[0]['name']]) +'.png')
        person2 = pygame.image.load('Assets/person' + str(numSwitch[leaders[1]['name']]) +'.png')
        person3 = pygame.image.load('Assets/person' + str(numSwitch[leaders[2]['name']]) +'.png')

        screen.blit(person1, (175, 150))
        screen.blit(person2, (175, 275))
        screen.blit(person3, (175, 400))

        fontTitlerecent = pygame.font.Font("Assets/Minecraft.ttf", 48)
        textTitlerecent = fontTitlerecent.render("Recent Games", True, (0, 0, 0))
        screen.blit(textTitlerecent, (225, 75))

        fontTitle1name = pygame.font.Font("Assets/Minecraft.ttf", 32)
        textTitle1name = fontTitle1name.render(leaders[0]['name'], True, (0, 0, 0))
        screen.blit(textTitle1name, (325, 175))

        fontTitle1 = pygame.font.Font("Assets/Minecraft.ttf", 32)
        textTitle1 = fontTitle1.render("$ %s" % leaders[0]['balance'], True, (0, 0, 0))
        screen.blit(textTitle1, (500, 175))

        fontTitle2name = pygame.font.Font("Assets/Minecraft.ttf", 32)
        textTitle2name = fontTitle2name.render(leaders[1]['name'], True, (0, 0, 0))
        screen.blit(textTitle2name, (325, 300))

        fontTitle2 = pygame.font.Font("Assets/Minecraft.ttf", 32)
        textTitle2 = fontTitle2.render("$ %s" % leaders[1]['balance'], True, (0, 0, 0))
        screen.blit(textTitle2, (500, 300))

        fontTitle3name = pygame.font.Font("Assets/Minecraft.ttf", 32)
        textTitle3name = fontTitle3name.render(leaders[2]['name'], True, (0, 0, 0))
        screen.blit(textTitle3name, (325, 425))

        fontTitle3 = pygame.font.Font("Assets/Minecraft.ttf", 32)
        textTitle3 = fontTitle3.render("$ %s" % leaders[2]['balance'], True, (0, 0, 0))
        screen.blit(textTitle3, (500, 425))

        bCount = bCount + 1
        if (bCount == 30):
            bCount = 0
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False
        pygame.display.update()


def main():
    """
    Main game function, interfaces with mainframe, HUD, and storyboard.
    """
    pygame.init()
    pygame.mixer.pre_init(4410,16,2,4096)
    pygame.mixer.music.load("Assets/Quirky-Puzzle-Game-Menu.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Avana")
    clock = pygame.time.Clock()

    #Entering main game loop
    
    mFrame = mainFrame()
    ourHUD = hud()

    #Entering title screen loop
    title(screen, clock)
    avatarNum = pickAvatar(screen, clock)
    backgroundImg = pygame.image.load('Assets/background_image.png')

    screen.blit(backgroundImg, (0, 0))
    bCount = 0
    
    isRunning = True
    doesTextWritten = False
    questionNum = 0
    randPerson = 1

    # Main game loop, continues running until game end parameters.
    while isRunning:
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                isRunning = False

        if (bCount >= 0 and bCount < 10): 
            backgroundImg = pygame.image.load('Assets/background_image.png')
            screen.blit(backgroundImg, (0, 0))
        if (bCount >= 10 and bCount < 20):
            backgroundImg = pygame.image.load('Assets/background_image_1.png')
            screen.blit(backgroundImg, (0, 0))
        if (bCount >= 20 and bCount < 30):
            backgroundImg = pygame.image.load('Assets/background_image_2.png')
            screen.blit(backgroundImg, (0, 0))
        bCount = bCount + 1
        if (bCount == 30):
            bCount = 0

        buttonPressed = ""

        if questionNum == 5 or ourHUD.getBalance() <= 0 or ourHUD.getCreditScore() <= 0:
            isRunning = displayEndGame(screen, clock, avatarNum, bCount, ourHUD)
            break
        else:
            buttonPressed = mFrame.render(screen, avatarNum, randPerson)

        ourHUD.render(screen)
        if not doesTextWritten:
            randNum = random.randint(1,5)
            questionText = myStory.question(randNum)
            answerList = myStory.option(randNum)
            reasonsWhy = myStory.aftermath(randNum)
            mFrame.textcool(screen, 120, 260, 120, 560 - 5, questionText, 25, (85,85,85), (255,255,255),"Assets/Minecraft.ttf")
            doesTextWritten = True
        else:
            mFrame.textnotcool(screen, 120, 260, 120, 560 - 5, questionText, 25, (85,85,85), (255,255,255), "Assets/Minecraft.ttf")
            mFrame.textnotcool(screen, 420, 425, 150, 560 - 5, answerList[1], 20 , (85,85,85), (0,0,0), "Assets/Minecraft.ttf")
            mFrame.textnotcool(screen, 130, 425, 150, 560 - 5, answerList[0], 20, (85,85,85), (0,0,0),"Assets/Minecraft.ttf")
        
        
        if buttonPressed == "Left" or buttonPressed == "Right":
            randPerson = random.randint(1, 4)
            questionNum += 1
            theAnswer = ""
            if buttonPressed == "Left":
                theAnswer = answerList[0]
            elif buttonPressed == "Right":
                theAnswer = answerList[1]
            
            myChanges = changes[theAnswer]

            ourHUD.changeHapiness(myChanges[0])
            ourHUD.changeCreditScore(myChanges[1])
            ourHUD.changeBalance(myChanges[2])

            grayBG = pygame.Surface((560, 120))
            grayBG.fill((85, 85, 85))
            screen.blit(grayBG, (120, 260))

            mFrame.textcool(screen, 120, 260, 120, 560 - 5, reasonsWhy, 25, (85,85,85), (44,183,123),"Assets/Minecraft.ttf")
            time.sleep(2)
            doesTextWritten = False
        
        pygame.display.update()

if __name__=="__main__":
    main()
    pygame.quit()
                
