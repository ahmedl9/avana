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
        self.xpos = 200
        #self.ser = serial.Serial('/dev/cu.usbmodem1411', 115200)

    def pullScenario(self):
        """
        pull all the info
        self.image = ...
        """
    
    def render(self, screen):
        #clean up all previous texts and images
        pygame.draw.rect(screen, (105, 105, 105), (200,200,400,400))
        joystickInput = ""#read(self.ser)
        if joystickInput == "Left":
            self.xpos -= 20
        elif joystickInput == "Right":
            self.xpos += 20
        #screen.fill(black)
        pygame.draw.rect(screen, (0,0,255), (200 + self.xpos,400,10,10))

        
        
        #render image
        #render text on button
        #render options



