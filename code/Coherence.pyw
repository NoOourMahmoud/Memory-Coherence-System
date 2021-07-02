import pygame
from threading import Thread

pygame.init()

#colors
white = (255,255,255)
green = (0,155,0)
black = (0,0,0)

#Main screen
display_height = 497
display_width = 724
gameDisplay = pygame.display.set_mode((display_width,display_height))

#button borders
press_xStart = 588
press_width = 110
press_yStart = 432
press_height = 32

#shared variables
b1 = 0
b2 = 0
b3 = 0

#arrows list
arrows = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#images
image = {'back_ground':pygame.image.load('Background.png'),
         'next_button':pygame.image.load('Button.PNG'),
         'gray_arrow':pygame.image.load('Gray Arrow.png'),
         'green_arrow':pygame.image.load('Green Arrow.png'),
         'purple_arrow':pygame.image.load('Purple Arrow.png'),
         'red_arrow':pygame.image.load('Red Arrow.png'),
         'white_arrow':pygame.image.load('White Arrow.png'),
         'yellow_arrow':pygame.image.load('Yellow Arrow.png')
    }

#fonts
smallfont = pygame.font.SysFont("Arial" , 18)
medfont = pygame.font.SysFont("Arial" , 25)

#'light_arrow':pygame.image.load('light.png'),
#'thick_arrow':pygame.image.load('thick.png')

def init():
    #music
    pygame.mixer.music.load("Ta Da-SoundBible.com-1884170640.wav")                  
    pygame.mixer.music.play(1)
    #Back screen
    pygame.display.set_caption('Memory')
    gameDisplay.blit(image['back_ground'] , (0 ,0))
    gameDisplay.blit(image['next_button'] , (588,425))

    pygame.display.update()


def th1():
    global arrows , b1, b2, b3 
    b2 = b1 + 1
    

def th2():
    global arrows , b1, b2, b3 
    b3 = b1 + 1


def th3():
    global arrows , b1, b2, b3
    b1 = b2 + 1


def th4():
    global arrows , b1, b2, b3
    b3 = b1 + 1
    

def th5():
    global arrows , b1, b2, b3
    b2 += 1


def th6():
    global arrows , b1, b2, b3
    b3 += 1
    

def message_to_screen(msg,color,x_displace,y_displace,size):
    if size == "small": 
        textSurface = smallfont.render(msg, True , color)
    if size == "med":   
        textSurface = medfont.render(msg, True , color)
    if size == "large": 
        textSurface = largefont.render(msg, True , color)
    if size == "semimed":                               
        textSurface = semimedfont.render(msg, True , color)
    textRect = textSurface.get_rect()
    textRect.center = x_displace, y_displace
    gameDisplay.blit(textSurface , textRect)


def main():
    init()
    global arrows
    flagT1 = 1
    flagT2 = 0
    flagT3 = 0

    inst1 = ''
    inst2 = ''
    inst3 = ''
    
    b1c1 = 'Invalid'
    b1c2 = 'Invalid'
    b1c3 = 'Invalid'
    
    b2c2 = 'Invalid'
    b2c1 = 'Invalid'
    b2c3 = 'Invalid'
    
    b3c3 = 'Invalid'
    b3c2 = 'Invalid'
    b3c1 = 'Invalid'
    
    
    t1 = Thread(target=th1, args=())
    t2 = Thread(target=th2, args=())
    t3 = Thread(target=th3, args=())
    t4 = Thread(target=th4, args=())
    t5 = Thread(target=th5, args=())
    t6 = Thread(target=th6, args=())

    while 1:
        gameDisplay.blit(image['back_ground'] , (0 ,0))
        gameDisplay.blit(image['next_button'] , (588,425))
        
        cur = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if press_xStart < cur[0] < press_xStart+press_width and press_yStart < cur[1] < press_yStart+press_height:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if flagT1:
                            t1.start()
                            t1.join()
                            arrows[2] = 1
                            arrows[3] = 1
                            b1c1 = 'Shared'
                            b2c1 = 'Exclusive'
                            inst1 = "W -> B2, R -> B1"
                            
                            t2.start()
                            t2.join()
                            arrows[7] = 1
                            arrows[8] = 1
                            b1c2 = 'Shared'
                            b3c2 = 'Exclusive'
                            inst2 = 'W -> B3, R -> B1'

                            flagT1 = 0
                            flagT2 = 1

                        elif flagT2:
                            arrows = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                            inst1 = ''
                            inst2 = ''
                            inst3 = ''
                            
                            t3.start()
                            t3.join()
                            arrows[11] = 1  #c3
                            arrows[12] = 1
                            arrows[13] = 1
                            b1c3 = 'Modified'
                            b2c3 = 'Shared'
                            b3c3 = 'Inavlid'
                            inst3 = 'W -> B1, R -> B2'
                            
                            
                            arrows[4] = 1  #c1
                            b1c1 = 'Inavlid'
                            b2c1 = 'Shared'
                            b3c1 = 'Inavlid'
                            
                            t6.start()
                            t6.join()
                            arrows[5] = 1   #c2
                            b1c2 = 'Inavlid'
                            b2c2 = 'Inavlid'
                            b3c2 = 'Exclusive'
                            inst2 = 'W -> B3, R -> B3'

                            flagT2 = 0
                            flagT3 = 1

                        elif flagT3:
                            arrows = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                            inst1 = ''
                            inst2 = ''
                            inst3 = ''
                            
                            t4.start()  #c1
                            t4.join()
                            arrows[3] = 1
                            arrows[2] = 1
                            arrows[1] = 1
                            b1c1 = 'Shared'
                            b2c1 = 'Inavlid'
                            b3c1 = 'Modified'
                            inst1 = 'W -> B3, R -> B1'
                            
                            t5.start()  #c3
                            t5.join()
                            arrows[10] = 1
                            arrows[11] = 1
                            arrows[14] = 1
                            b1c3 = 'Shared'
                            b2c3 = 'Modified'
                            b3c3 = 'Inavlid'
                            inst3 = 'W -> B2, R -> B2'

                            #c2
                            b1c2 = 'Inavlid'
                            b2c2 = 'Inavlid'
                            b3c2 = 'Inavlid'
                            arrows[9] = 1
                            
                            flagT3 = 0
                    

        #first inst
        message_to_screen(inst1,black,165,200,'small')

        message_to_screen("B1: " + b1c1,black,165,240,'small')
        message_to_screen("B2: " + b2c1,black,165,260,'small')
        message_to_screen("B3 : " + b3c1,black,165,280,'small')
        
        
        #mid instruction
        message_to_screen(inst2,black,365,200,'small')

        message_to_screen("B1: " + b1c2,black,365,240,'small')
        message_to_screen("B2: " + b2c2,black,365,260,'small')
        message_to_screen("B3: " + b3c2,black,365,280,'small')

        #third instruction
        message_to_screen(inst3,black,575,200,'small')

        message_to_screen("B1: " + b1c3,black,575,240,'small')
        message_to_screen("B2: " + b2c3,black,575,260,'small')
        message_to_screen("B3: " + b3c3,black,575,280,'small')

        


        #first block arrows
        if arrows[0]:
            gameDisplay.blit(image['yellow_arrow'] , (90,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (90,290))
        if arrows[1]:
            gameDisplay.blit(image['red_arrow'] , (120,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (120,290))
        if arrows[2]:
            gameDisplay.blit(image['green_arrow'] , (150,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (150,290))
        if arrows[3]:
            gameDisplay.blit(image['purple_arrow'] , (180,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (180,290))
        if arrows[4]:
            gameDisplay.blit(image['white_arrow'] , (210,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (210,290))

        
        #second block arrows
        
        if arrows[5]:
            gameDisplay.blit(image['yellow_arrow'] , (295,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (295,290))
        if arrows[6]:
            gameDisplay.blit(image['red_arrow'] , (325,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (325,290))
        if arrows[7]:
            gameDisplay.blit(image['green_arrow'] , (355,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (355,290))
        if arrows[8]:
            gameDisplay.blit(image['purple_arrow'] , (385,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (385,290))
        if arrows[9]:
            gameDisplay.blit(image['white_arrow'] , (415,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (415,290))

        #third block arrows
       
        if arrows[10]:
            gameDisplay.blit(image['yellow_arrow'] , (503,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (503,290))
        if arrows[11]:
            gameDisplay.blit(image['red_arrow'] , (533,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (533,290))
        if arrows[12]:
            gameDisplay.blit(image['green_arrow'] , (563,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (563,290))
        if arrows[13]:
            gameDisplay.blit(image['purple_arrow'] , (593,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (593,290))
        if arrows[14]:
            gameDisplay.blit(image['white_arrow'] , (623,290))
        else:
            gameDisplay.blit(image['gray_arrow'] , (623,290))

        pygame.display.update()

if __name__ == "__main__":
    main()

    
