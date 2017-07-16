__author__ = 'chinmay'
import  pygame
from pygame.locals import *
import time
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 160, 0)

pygame.init()
pygame.font.init

# Set the width and height of the screen [width, height]
width = 700
height = 500
screen_dim = [700,500]
screen = pygame.display.set_mode(screen_dim)

pygame.display.set_caption("AGAR.IO")


# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

player_mass = 15
max_cell_spawn = 1
player_x = 0.0
player_y = 0.0
max_speed = 11
current_food = 0
food_mass = 4
max_food = 35
old_time = time.time()
player_speed = 0.0
playerdead = 0

food = {}
cells = []



def random_food(count,food):
    current_food = 0
    for i in range(0,count):
        fx = random.randrange(1,width)
        fy = random.randrange(1,height)
        tup = (fx,fy)
        food[tup] = 1
        current_food += 1
    return current_food

def spawncells(count,cells):

    for i in range(0, count):
        x = random.randrange(1,width)
        y = random.randrange(1,height)
        size = random.randrange(player_mass,player_mass + 20)
        speed = max_speed * pow (0.999, -(size / 13))
        celllist = [x,y,size,speed]
        cells.append(celllist)

def quit():
    pygame.quit()
    pygame.font.quit
    exit()

random_food(max_food,food)
spawncells(3,cells)


while True:
    foodtups = food.keys()

    player_speed = max_speed * pow (1.1, -(player_mass / 15))
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player_y -= player_speed
    if keys[K_DOWN]:
        player_y += player_speed
    if keys[K_RIGHT]:
        player_x += player_speed
    if keys[K_LEFT]:
        player_x -= player_speed

    if (food == {}):
        food = {}
        current_food = random_food(max_food,food)
        old_time = time.time()

    for x in range(int(player_x),int(player_x) + player_mass):
        for y in range(int(player_y),int(player_y) + player_mass):
            ptup = (x,y)
            if (ptup in food):
                del food[ptup]
                current_food -= 1
                player_mass += 1

    for n in range(0,len(cells)):

        xdist = cells[n][0] + cells[n][2]/2 - player_x - player_mass/2
        ydist = cells[n][1] + cells[n][2]/2 - player_y - player_mass/2
        centerdist = (xdist*xdist + ydist*ydist)
        sumradii = (cells[n][2] / 2) + (player_mass / 2)

        if (centerdist < 200 * 200):
            #print centerdist
            if (cells[n][2] < player_mass):
                if (player_x > cells[n][0] and player_y > cells[n][1]):
                    cells[n][0] -= cells[n][3]
                    cells[n][1] -= ((cells[n][1] - player_y) / (cells[n][0] - player_x)) * cells[n][3]
                else:
                    if (player_x > cells[n][0] and player_y < cells[n][1]):
                        cells[n][0] -= cells[n][3]
                        cells[n][1] -= ((cells[n][1] - player_y) / (cells[n][0] - player_x)) * cells[n][3]
                    else:
                        cells[n][0] += cells[n][3]
                        cells[n][1] += ((cells[n][1] - player_y) / (cells[n][0] - player_x)) * cells[n][3]
            if (cells[n][2] > player_mass):
                if (player_x > cells[n][0] and player_y > cells[n][1]):
                    cells[n][0] += cells[n][3]
                    cells[n][1] += ((cells[n][1] - player_y) / (cells[n][0] - player_x)) * cells[n][3]
                else:
                    if (player_x > cells[n][0] and player_y < cells[n][1]):
                        cells[n][0] += cells[n][3]
                        cells[n][1] += ((cells[n][1] - player_y) / (cells[n][0] - player_x)) * cells[n][3]
                    else:
                        cells[n][0] -= cells[n][3]
                        cells[n][1] -= ((cells[n][1] - player_y) / (cells[n][0] - player_x)) * cells[n][3]

        if ( centerdist < sumradii*sumradii):
            if (cells[n][2] < player_mass):
                player_mass += cells[n][2]
                #del cells[cells[n]]
                cells.pop(n)
            else:
                player_mass = 0
                quit()


    screen.fill(WHITE)
    pygame.draw.ellipse(screen,GREEN,[player_x,player_y,player_mass,player_mass])

    for n in range(0,len(foodtups)):
        pygame.draw.rect(screen,BLUE,[foodtups[n][0],foodtups[n][1],food_mass,food_mass])


    for i in range(0, len(cells)):
        pygame.draw.ellipse(screen,ORANGE,[cells[i][0],cells[i][1],cells[i][2],cells[i][2]])

    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if (event.type == pygame.QUIT):
            # if it is quit the game
            quit()