#This is our main file 
import pygame
import serial
from MainFrame import mainFrame
from HUD import hud
from pySerialTest import myRead as read
import random
from storyboard2 import StoryBoard

arr = [1,2,3,4,5]
myStory = StoryBoard()
ser = serial.Serial('/dev/cu.usbmodem14501', 115200)
blinktimer = 1

def renderTitle(screen, bCount):

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
            """if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (pygame.Rect((275, 325-25), (250, 50)).collidepoint(pos)):
                    buttonClicked = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (pygame.Rect((275, 325-25), (250, 50)).collidepoint(pos)):
                    buttonClicked = True"""
        
    return True





def main():
    
    pygame.init()
    pygame.mixer.pre_init(4410,16,2,4096)
    pygame.mixer.music.load("Assets/Quirky-Puzzle-Game-Menu.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Avana")
    clock = pygame.time.Clock()
    #BG_COLOR = 128, 128, 128 #Light gray RGB
    #screen.fill(BG_COLOR)

    #Entering main game loop
    
    mFrame = mainFrame()
    ourHUD = hud()

    #Entering title screen loop
    isRunning = title(screen, clock)
    backgroundImg = pygame.image.load('Assets/background_image.png')

    screen.blit(backgroundImg, (0, 0))
    bCount = 0
    doesTextWritten = False
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
        
        buttonPressed = mFrame.render(screen)
        ourHUD.render(screen)
        if not doesTextWritten:
            randNum = random.randint(1,5)
            questionText = myStory.question(randNum)
            answerList = myStory.option(randNum)
            reasonsWhy = myStory.aftermath(randNum)
            mFrame.textcool(screen, 120, 260, 120, 560 - 5, questionText, 30, (85,85,85), (255,255,255),"Assets/Minecraft.ttf")
            doesTextWritten = True
        else:
            mFrame.textnotcool(screen, 120, 260, 120, 560 - 5, questionText, 30, (85,85,85), (255,255,255), "Assets/Minecraft.ttf")
            mFrame.textnotcool(screen, 420, 425, 150, 560 - 5, answerList[1], 20 , (85,85,85), (0,0,0), "Assets/Minecraft.ttf")
            mFrame.textnotcool(screen, 130, 425, 150, 560 - 5, answerList[0], 20, (85,85,85), (0,0,0),"Assets/Minecraft.ttf")
        
        
        if buttonPressed:
            theAnswer = ""
            print('ANKUR IS GOD')
            if buttonPressed == "Left":
                theAnswer = answerList[0]
            elif buttonPressed == "Right":
                theAnswer = answerList[1]

            doesText = False
            


        
        

        

       
    

            
        
        pygame.display.update()

if __name__=="__main__":
    main()
    pygame.quit()
                
