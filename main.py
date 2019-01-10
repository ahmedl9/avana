#This is our main file 
import pygame
import serial
from pySerialTest import myRead as read

ser = serial.Serial('/dev/cu.usbmodem1411', 115200)


def main():   
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Avana")
    clock = pygame.time.Clock()
    BG_COLOR = 128, 128, 128 #Light gray RGB
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, (105, 105, 105), (200,200,400,400))


    isRunning = True
    xpos = 350
    black = [0, 0, 0]

    while isRunning :
        print(read(ser))
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                isRunning = False
        joystickInput = read(ser)
        if joystickInput == "Left":
            xpos -= 20
        elif joystickInput == "Right":
            xpos += 20
        screen.fill(black)
        pygame.draw.rect(screen, (0,0,255), (xpos,10,10,10))


        pygame.display.update()

if __name__=="__main__":
    main()
    pygame.quit()
                
