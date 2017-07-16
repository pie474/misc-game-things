__author__ = 'chinmay'
import pygame
from pygame.locals import *
import random

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
b = 0.0
n = 10
m = 0.0
temp1 = 0.0
temp2 = 0.0
temp3 = 0.0
temp4 = 0.0
coords = []
ORANGE = (255, 160, 0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)

#screen.fill(WHITE)

for i in range(0, n):
    px = random.randrange(1, width)
    py = height - random.randrange(1, height/2)
    #pygame.draw.rect(screen, ORANGE, px - 1, height - (py - 1), 2, 2)
    pygame.draw.rect(screen,ORANGE,[px - 3, py - 3, 6, 6])
    tup = (px, py)
    #coords[tup] = 1
    coords.append(tup)

for w in range(0, n):
    temp1 += coords[w][0] * coords[w][1]

for y in range(0, n):
    temp2 += coords[y][0]

for z in range(0, n):
    temp3 += coords[z][1]

for a in range(0, n):
    temp4 += coords[a][0] * coords[a][0]

m = ((n * temp1) - (temp2 * temp3)) / ((n * temp4) - (temp2 * temp2 ))
b = (temp3 - (m * temp2)) / n

print "slope is " + str(m)
print "intercept is " + str(b)

for x in range (1, width):
    pygame.draw.circle(screen, BLUE, (x, int(0 +( m * x + b))), 2, 0)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        # check if the event is the X button
        if (event.type == pygame.QUIT):
            # if it is quit the game
            quit()