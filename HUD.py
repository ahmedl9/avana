import pygame

class HUD:
    #Store person image displayed
    #Store current text displayed
    #Store current decisions
    happiness = 0
    creditScore = 0
    balance = 0
    
    def __init__(self):

    def getHapiness(self):
        return happiness

    def getCreditScore(self):
        return creditScore

    def getBalance(self):
        return balance

    def setHapiness(self, val):
        hapiness = val

    def render(self, screen):
        #clean up all previous texts and images
        pygame.draw.rect(screen, (105, 105, 105), (200,200,400,400))

        
        
        #render image
        #render text on button
        #render options



