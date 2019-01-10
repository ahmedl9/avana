#This is our main file 
import pygame

def main():   
    pygame.init()
    screen = pygame.display.set_mode((300, 300), 0,32)
    clock = pygame.time.Clock()

    isRunning = True
    
    while isRunning:
        time_passed = clock.tick(50)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                isRunning = False

if __name__=="__main__":
    main()
                
