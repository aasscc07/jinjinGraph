
import pygame
import sys
import math


pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Graph")

C_BLACK = (0,0,0)
C_RED = (255,0,0)
n_ = 0

c = int(input("초월함수면 1 다항함수면 2 : "))

if c==1:
    n_ = int(input("sin함수면 1, cos함수면 2, tan함수면 3 : "))
    

xn_ = []

if c==2:
    n = int(input("최고차항 : "))
    xn_ = []
    for i in range(n + 1):
        v1 = int(input(f"x{i} : "))
        xn_.append(v1)


def Functions(x,xn :list):
    x_ = 0
    sum_y = 0
    for i in range(len(xn)):
        
        x_ = xn[i] * pow(x,i) 
        
        sum_y += x_

    return -1 * sum_y






        
            
    

    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    for i in range(31):
        if i == 15:
            pygame.draw.line(screen,C_BLACK, [i * 20,0],[i * 20,WINDOW_WIDTH],3)
        else:
            pygame.draw.line(screen,C_BLACK, [i * 20,0],[i * 20,WINDOW_WIDTH],1)
    for i in range(31):
        if i == 15:
            pygame.draw.line(screen,C_BLACK, [0,i * 20],[WINDOW_HEIGHT,i * 20],3)
        else:
            pygame.draw.line(screen,C_BLACK, [0,i * 20],[WINDOW_HEIGHT,i * 20],1)


   
    
    # a = 함수 그래프
    def draw_fuction1():
        x1 = 0
        x2 = 0
        for i in range(10000):
            pygame.draw.circle(screen,C_RED,[x1 + 300, Functions(x1 / 20,xn_) * 20 + 300],1,1)
            pygame.draw.circle(screen,C_RED,[x2 + 300, Functions(x2 / 20,xn_) * 20 + 300],1,1)
            
            x1 += 0.1
            x2 -= 0.1
    def draw_fuction2():
            if n_==1:
                for i in range(1000):
                    pygame.draw.circle(screen,C_RED, [ i + 300, math.sin(i / 20) * 20 + 300],1,1)
                    pygame.draw.circle(screen,C_RED, [-i + 300, math.sin(-i / 20) * 20 + 300],1,1)
            if n_==2:    
                for i in range(1000):
                    pygame.draw.circle(screen,C_RED, [i + 300, math.cos(i/ 20) * 20 + 300],1,1)
                    pygame.draw.circle(screen,C_RED, [-i + 300, math.cos(-i / 20) * 20 + 300],1,1)
            if n_==3:
                for i in range(1000):
                    pygame.draw.circle(screen,C_RED, [i + 300, math.tan(i / 20) * 20 + 300],1,1)
                    pygame.draw.circle(screen,C_RED, [-i + 300, math.tan(-i / 20) * 20 + 300],1,1)
        
    # draw_fuction

    
    draw_fuction1()
    draw_fuction2()
    


    pygame.display.update()
