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
        self.currentSelection = "None"
        self.ser = serial.Serial('/dev/cu.usbmodem1411', 115200)
        self.blinktimer = 1

    def pullScenario(self):
        """
        pull all the info
        self.image = ...
        """
    
    def render(self, screen):
        #clean up all previous texts and images
        grayBG = pygame.Surface((600, 400))
        grayBG.set_alpha(128)
        grayBG.fill((105, 105, 105))
        screen.blit(grayBG, (100, 125))
        #pygame.draw.rect(screen, (105, 105, 105), (100,200,600,500))
        joystickInput = read(self.ser)
        if joystickInput == "Left" or joystickInput == "Right":
            self.currentSelection = joystickInput
        #if joystickInput == "Left":
        #    self.xpos -= 20
        #elif joystickInput == "Right":
        #    self.xpos += 20
        #screen.fill(black)

        buttonImg = pygame.image.load('Assets/button.png')
        selectionBorder = pygame.image.load('Assets/selection.png')

        if self.blinktimer < 0:
            self.blinktimer = 8
        elif self.blinktimer < 4:
            self.blinktimer -= 1
            if self.currentSelection == "Left":
                screen.blit(selectionBorder, (125, 420))
            elif self.currentSelection == "Right":
                screen.blit(selectionBorder, (415, 420))
        else:
            self.blinktimer -= 1

        screen.blit(buttonImg, (130, 425))
        screen.blit(buttonImg, (420, 425))
        
        
        #render image
        #render text on button
        #render options



