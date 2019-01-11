#This is our main file 
import pygame
import serial
from MainFrame import mainFrame
from HUD import hud
from pySerialTest import myRead as read

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
    screen.blit(buttonImg, (275, 325-25))
    screen.blit(textButton, (330, 343-25))

    pygame.display.update()



def title(screen, clock):
    bCount = 0
    
    buttonClicked = False

    while (not buttonClicked):
        renderTitle(screen, bCount)
        bCount = bCount + 1
        if (bCount == 30):
            bCount = 0
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False;
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (pygame.Rect((275, 325-25), (250, 50)).collidepoint(pos)):
                    buttonClicked = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (pygame.Rect((275, 325-25), (250, 50)).collidepoint(pos)):
                    buttonClicked = True

    return True;





def main():   
    pygame.init()
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
    
    while isRunning :
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

        mFrame.render(screen)
        ourHUD.render(screen)
        
        pygame.display.update()

if __name__=="__main__":
    main()
    pygame.quit()
                
