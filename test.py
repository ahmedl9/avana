import pygame
from time import sleep
pygame.init()

pygame.mixer.pre_init(4410,16,2,4096)
#MUSIC


def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped


def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)




screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

pygame.mixer.music.load("Assets/Quirky-Puzzle-Game-Menu.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)




#clock = pygame.time.Clock()

def writtenText(screen, xpoint, ypoint, length, width, text, textsize, backgroundrgbvalues, textrgbvalues, font = None):

    ypoint = ypoint - textsize
    ypoint = ypoint + 5
    xpoint = xpoint + 5

    
    done = False
    font = pygame.font.Font(font, textsize)
    mynewlist = wrapline(text, font, width)

#myrealtext = 'Hello World hdhjg skdjfhs kdjfhksdj fksj dhf kjsdhf ksdj fhjfkgh ksdjfhgks djhf gksjdhf gksj dhfgkjsdhf gksjdhfg ksjdhfg ksjdhfg ksjdh gskdjfhg sdjfgh sdfgj khsdf gjkh sdfgk jhsd fgjkh'
#text = font.render(myrealtext, True, (0, 128, 0))

    #spacer = 0
    j = 0

    #screen.fill((255, 255, 255)) MAY NEED??
    for thenextbigstring in mynewlist:

        #spacer += (2*textsize)
        i = 0
        j += (textsize)
    
        while not done: 

            if i < len(thenextbigstring):
              i = i + 1
            else:
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True

            blittext = font.render(thenextbigstring[0:i], True, textrgbvalues)
            sleep(0.04)
            #pygame.draw.rect(screen, backgroundrgbvalues, (xpoint, ypoint + j ,width, textsize), 0)
            pygame.draw.rect(screen, backgroundrgbvalues, (xpoint, ypoint + j, width, textsize), 0)
            #screen.blit(blittext,(xpoint, ypoint + spacer))
            screen.blit(blittext,(xpoint, ypoint + j))
            pygame.display.flip()
            #clock.tick(60)


#pygame.draw.rect(screen, (100,100,100), (100, 100, 10, 10))
#writtenText(screen, 100, 100, 200, 200, "Hello, my name is Nishant Iyengar and I like to eat pie! I also like to hoola hoop and watch video games", 16, (255,255,255), (0,128,0))
