import random
import pygame
import time
import sys
from audio.media import MediaPlayer

pygame.init()

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width,dis_height),pygame.FULLSCREEN)
pygame.display.update()
pygame.display.set_caption("Snake xenzia")
game_over=False
BLUE = (0,0,255)
RED  = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
SNAKE_SPEED = 10
SNAKE_BLOCK = 10
x1=dis_width/2
y1=dis_height/2

x1_change = 0
y1_chnage = 0


font_style = pygame.font.SysFont(None,25)
score_style = pygame.font.SysFont('comicsansms',35)


def our_snake(SNAKE_BLOCK,SNAKE_LIST:list):
    for x in SNAKE_LIST:
        pygame.draw.rect(dis,BLACK,[x[0],x[1],SNAKE_BLOCK,SNAKE_BLOCK])



def alert(msg,color):

    msg = font_style.render(msg,True,color)
    dis.blit(msg,[dis_width/2,dis_height/2])

clock = pygame.time.Clock()

def main_loop():
    global game_over
    global x1
    global x1_change
    global y1
    global y1_chnage
    game_close = False
    SNAKE_LIST = []
    Lenght_of_snake = 1
    foodx = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)* 10.0
    foody = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)*10.0
    if foody > dis_width and dis_height:
        foody = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)* 10.0
    
    if foodx > dis_width and dis_height:
        foodx = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)* 10.0
    
    


    print(foodx)
    print(foody)
    while not game_over:
        while game_close == True:
            dis.fill(BLUE)
          
            alert('You Lost! Press C to Play again or Q to Quit',RED)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        main_loop()
    




        for event in pygame.event.get():
            # Hello faruq
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit() 
                            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change  = -SNAKE_BLOCK
                    y1_chnage  = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_chnage = 0
                elif event.key == pygame.K_UP:
                    y1_chnage = - SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_chnage = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
            md = MediaPlayer('audio/sound/crash.wav')
            md.load_sound()
            md.play()
            game_close=True
        x1 += x1_change
        y1 += y1_chnage
        dis.fill(WHITE)

        
        #food
        pygame.draw.rect(dis,BLUE,[foodx,foody,SNAKE_BLOCK,SNAKE_BLOCK])
        snake_Head =[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        SNAKE_LIST.append(snake_Head)
        if len(SNAKE_LIST) > Lenght_of_snake:
            del SNAKE_LIST[0]

        for x in SNAKE_LIST[:-1]:
            if x == snake_Head:
                game_close =True

        our_snake(SNAKE_BLOCK,SNAKE_LIST)


        # pygame.draw.rect(dis,BLACK,[x1,y1,SNAKE_BLOCK,SNAKE_BLOCK])

        pygame.display.update()


        #food matching
        if x1 == foodx  and y1 == foody:
            foodx = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)* 10.0
            foody = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)*10.0
            if foody > dis_width and dis_height:
                foody = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)* 10.0
    
            if foodx > dis_width and dis_height:
                foodx = round(random.randrange(0,dis_width - SNAKE_BLOCK)/10.0)* 10.0
            Lenght_of_snake+=1
            md = MediaPlayer('audio/sound/yummy.ogg')
            md.load_sound()
            md.play()
        # print(x1)
        # print(foodx)
        # print(y1)
        # print(foody)
        

        # pygame.draw.rect(dis,BLUE,[200,150,10,10])
        # pygame.display.update()
        clock.tick(SNAKE_SPEED)


# main_loop()