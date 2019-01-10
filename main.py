#This is our main file 
import pygame

def myRead():
    return "Still"

def main():   
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Avana")
    clock = pygame.time.Clock()
    BG_COLOR = 128, 128, 128 #Light gray RGB
    screen.fill(BG_COLOR)


    isRunning = True
    
    while isRunning :
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                isRunning = False

        joystickInput = myRead()
        if joystickInput == "Left":
            pygame.draw.rect(screen, (0,0,255), (10,10,10,10))
        if joystickInput == "Right":
            pygame.draw.rect(screen, (0,0,255), (700,10,10,10))
        if joystickInput == "Still":
            pygame.draw.rect(screen, (0,0,255), (350,10,10,10))


        pygame.display.update()

if __name__=="__main__":
    main()
    pygame.quit()
                
