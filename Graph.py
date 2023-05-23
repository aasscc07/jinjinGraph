import pygame
import sys


pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Graph")

# Lines = pygame.Rect()
x = 0
# y1 = x ** 2 + 2 * x + 1

# y2 = x + 1

def F_Y2(x):
    return x + 1

C_BLACK = (0,0,0)
C_RED = (255,0,0)
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

    for i in range(600):
        pygame.draw.circle(screen,C_RED,[x + 300,F_Y2(x) + 300],1,1)
        x += 0.1

        

    


    


    pygame.display.update()

