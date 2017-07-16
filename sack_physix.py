__author__ = 'chinmay'
import  pygame
from pygame.locals import *
from pygame.font import *
import time
import random

BLACK = (0, 0, 0)
DARKGRAY = (50, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LBLUE = (0, 0, 180)
ORANGE = (255, 160, 0)
YELLOW = (255, 255, 0)

pygame.init()
pygame.font.init

# Set the width and height of the screen [width, height]
width = 750
height = 750

screen_dim = [width,height]
screen = pygame.display.set_mode(screen_dim)

pygame.display.set_caption("Sack Simulator")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


gravity = -9.8
radius = 50
x_resistance = 0.9
xpos = -200
ypos = 500
xvel = 50
yvel = 50


while True:
    screen.fill(WHITE)

    xvel = xvel * x_resistance
    xpos += xvel

    if (ypos>radius):
        yvel+=gravity
        ypos+=yvel
        print ypos
    else:
        yvel = (yvel * -1) - 3
        ypos+=yvel
        if ypos < radius:
            ypos = radius
            yvel = 0
    #print ypos
    pygame.draw.ellipse(screen, RED, [xpos+(width/2), height-ypos, radius, radius])

    pygame.display.flip()
    #loop through the events
    for event in pygame.event.get():
        #check if the event is the X button
        if (event.type==pygame.QUIT):
            #if it is quit the game
            pygame.quit()
            exit(0)