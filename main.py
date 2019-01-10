#This is our main file 
import pygame
import serial
from MainFrame import mainFrame
from HUD import hud
from pySerialTest import myRead as read



def main():   
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Avana")
    clock = pygame.time.Clock()
    #BG_COLOR = 128, 128, 128 #Light gray RGB
    backgroundImg = pygame.image.load('Assets/background_image.png')

    screen.blit(backgroundImg, (0, 0))
    #screen.fill(BG_COLOR)
    
    mFrame = mainFrame()

    ourHUD = hud()

    isRunning = True

    while isRunning :
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                isRunning = False
        
        mFrame.render(screen)
        ourHUD.render(screen)
        
        pygame.display.update()

if __name__=="__main__":
    main()
    pygame.quit()
                
