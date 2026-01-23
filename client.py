import pygame
import math

pygame.init()

#creates a window
screen = pygame.display.set_mode((800, 600))

#hover effect for the chess board
def onHover():
    x,y = pygame.mouse.get_pos()
    x,y = math.floor(x/50), math.floor(y/50)
    if 1 <= x <= 8 and 1 <= y <= 8:
        pygame.draw.rect(screen,(153, 255, 153),(50*x,50*y,50,50))
    #print(f"{x} and {y}")

#renders the chess board
def drawboard():
    for k in range(1,9):
        temp =k
        for i in range (1,9):
            if temp%2 == 0:
                colour = (51,25,0)
            else:
                colour = (243,238,170)
            pygame.draw.rect(screen,colour,(50*i,50*k,50,50))

            temp +=1

open =True
while open:
    for event in pygame.event.get():
        #checks if the user tries to close the window
        if event.type == pygame.QUIT:
            open = False
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            x,y = math.floor(x/50), math.floor(y/50)
            if 1 <= x <= 8 and 1 <= y <= 8:
                print(f"The user clicked on {x} and {9-y}")

    
    #changes the background colour
    screen.fill((255,255,255))
    
    drawboard()
    onHover()

    pygame.display.flip()