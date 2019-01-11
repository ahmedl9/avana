import pygame

class hud:    
    def __init__(self):
        self.happiness = 2
        self.creditScore = 400
        self.balance = 1000

    def getHapiness(self):
        return self.happiness

    def getCreditScore(self):
        return self.creditScore

    def getBalance(self):
        return self.balance

    def changeHapiness(self, val):
        self.happiness = self.happiness + val
        if self.happiness < 0:
            self.happiness = 0
        elif self.happiness > 2:
            self.happiness = 2



    def changeCreditScore(self, val):
        self.creditScore = self.creditScore + val
        if self.creditScore > 800:
            self.creditScore = 800
        elif self.creditScore < 0:
            self.creditScore = 0

    def changeBalance(self, val):
        self.balance = self.balance + val

    def render(self, screen):
        creditScoreImg = pygame.image.load('Assets/creditscore_bar.png')
        balanceImg = pygame.image.load('Assets/balance_bar.png')
        happinessImg = pygame.image.load('Assets/happiness-1.png')
        happinessImg2 = pygame.image.load('Assets/happiness-2.png')
        happinessImg3 = pygame.image.load('Assets/happiness-3.png')

        screen.blit(creditScoreImg, (50, 50))
        screen.blit(balanceImg, (500, 50))

        if (self.happiness == 0):
            screen.blit(happinessImg3, (384, 59))
        elif (self.happiness == 1):
            screen.blit(happinessImg2, (384, 59))
        elif (self.happiness == 2):
            screen.blit(happinessImg1, (384, 59))




        font = pygame.font.Font("Assets/Minecraft.ttf", 24)
        text = font.render("Credit Score: " + str(self.creditScore), True, (0, 0, 0))
        screen.blit(text, (60, 68))

        text2 = font.render("Balance: " + str(self.balance), True, (0, 0, 0))
        screen.blit(text2, (510, 68))
        
        #render image
        #render text on button
        #render options

"""
#This is our main file 
import pygame
import serial
from MainFrame import mainFrame
from HUD import hud
from pySerialTest import myRead as read

#ser = serial.Serial('/dev/cu.usbmodem1411', 115200)


def main():   
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Avana")
    clock = pygame.time.Clock()
    BG_COLOR = 128, 128, 128 #Light gray RGB
    screen.fill(BG_COLOR)
    
    mFrame = mainFrame()

    ourHUD = hud()

    isRunning = True
    xpos = 350
    black = [0, 0, 0]

    while isRunning :
        #print(read(ser))
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                isRunning = False
        joystickInput = ""#read(ser)
        if joystickInput == "Left":
            xpos -= 20
        elif joystickInput == "Right":
            xpos += 20
        screen.fill(black)
        pygame.draw.rect(screen, (0,0,255), (xpos,10,10,10))
        mFrame.render(screen)
        ourHUD.render(screen)
        
        pygame.display.update()

if __name__=="__main__":
    main()
    pygame.quit()
                


"""

