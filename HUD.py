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
        
        
        #render image
        #render text on button
        #render options



