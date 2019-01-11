import pygame

class hud:    
    def __init__(self):
        self.happiness = 0
        self.creditScore = 0
        self.balance = 0

    def getHapiness(self):
        return self.happiness

    def getCreditScore(self):
        return self.creditScore

    def getBalance(self):
        return self.balance

    def changeHapiness(self, val):
        self.hapiness = self.hapiness + val

    def changeCreditScore(self, val):
        self.creditScore = self.creditScore + val

    def changeBalance(self, val):
        self.balance = self.balance + val

    def render(self, screen):
        creditScoreImg = pygame.image.load('Assets/creditscore_bar.png')
        balanceImg = pygame.image.load('Assets/balance_bar.png')
        happinessImg = pygame.image.load('Assets/happiness1.png')

        screen.blit(creditScoreImg, (50, 50))
        screen.blit(happinessImg, (384, 59))
        screen.blit(balanceImg, (500, 50))

        font = pygame.font.Font("Assets/Minecraft.ttf", 24)
        text = font.render("0", True, (0, 0, 0))
        screen.blit(text, (60, 63))

        text2 = font.render("0", True, (0, 0, 0))
        screen.blit(text2, (510, 63))
        
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

