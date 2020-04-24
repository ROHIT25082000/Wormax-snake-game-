import pygame 
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
skyblue = (135,206,250)
green = (0,155,0)
darkgreen = (0,70,0)
violet = (238,130,238)
cream = (255,253,208)

disp_width = 800
disp_height = 600
block_size = 20


font = pygame.font.SysFont(None , 50)

def snake(block_size, snakelist):
    pygame.draw.rect(gameDisplay,darkgreen,[snakelist[-1][0],snakelist[-1][1],block_size,block_size])
    for xy in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [xy[0],xy[1],block_size,block_size])
def textobj(text ,color):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()

def message(msg, color):
    textSurf, text_rect = textobj(msg,color)
    text_rect.center = (disp_width/2),((disp_height)/2)
    gameDisplay.blit(textSurf, text_rect)

def message1(msg, color):
    textSurf, text_rect = textobj(msg,color)
    text_rect.center = (disp_width/2),(50)
    gameDisplay.blit(textSurf, text_rect)

gameDisplay  = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption('Wormax.io')
pygame.display.update()

clock = pygame.time.Clock()
def gameloop():
    gameExit = False
    gameOver = False 
    lead_x = (disp_width)/2
    lead_y = (disp_height)/2 
    lead_x_change = 0
    lead_y_change = 0
    speed = 10
    snakelist = []
    count = 1
    
    random_apple_x = round(random.randrange(0,disp_width - block_size)/block_size)*block_size
    random_apple_y = round(random.randrange(0,disp_height - block_size )/block_size)*block_size
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(skyblue)
            message("Game Over! press c to continue and q to quit",red)
            message1("Score : " + str((count-1)*10),black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change  = 0
        lead_x += lead_x_change
        lead_y += lead_y_change 
        
        gameDisplay.fill(cream)
        pygame.draw.rect(gameDisplay, red, [random_apple_x, random_apple_y,block_size,block_size])
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)

        if len(snakelist) > count:
            del snakelist[0]
        snake(block_size,snakelist)
        message1("Score : " + str((count-1)*10),violet)
        pygame.display.update()

        for i in snakelist[:-1]:
            if i == snakeHead:
                gameOver = True

        if lead_x >= disp_width   or lead_x < 0 or lead_y >= (disp_height) or lead_y < 0 :
            gameOver = True
        
        if lead_x == random_apple_x and lead_y == random_apple_y:
            random_apple_x = round(random.randrange(0,disp_width - block_size)/block_size)*block_size
            random_apple_y = round(random.randrange(0,disp_height - block_size)/block_size)*block_size 
            count +=1
            speed +=1
        clock.tick(speed)
    pygame.quit() 
    quit()
gameloop()

