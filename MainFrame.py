import pygame
import serial
from pySerialTest import myRead as read

class mainFrame:
    #Store person image displayed
    #Store current text displayed
    #Store current decisions
    #Store decision aftermath
    image = ""
    text = ""
    decisions = {}
    aftermath = {}

    black = [0, 0, 0]
    
    
    def __init__(self):
        image = ""
        self.xpos = 195
        #self.ser = serial.Serial('/dev/cu.usbmodem1411', 115200)

    def pullScenario(self):
        """
        pull all the info
        self.image = ...
        """
    
    def render(self, screen):
        #clean up all previous texts and images
        grayBG = pygame.Surface((600, 400))
        grayBG.set_alpha(8)
        grayBG.fill((105, 105, 105))
        screen.blit(grayBG, (100, 125))
        #pygame.draw.rect(screen, (105, 105, 105), (100,200,600,500))
        joystickInput = ""#read(self.ser)
        if joystickInput == "Left":
            self.xpos -= 20
        elif joystickInput == "Right":
            self.xpos += 20
        #screen.fill(black)
        pygame.draw.rect(screen, (0,0,255), (200 + self.xpos,325,10,10))

        buttonImg = pygame.image.load('Assets/button.png')

        screen.blit(buttonImg, (130, 425))
        screen.blit(buttonImg, (420, 425))
        
        
        #render image
        #render text on button
        #render options



