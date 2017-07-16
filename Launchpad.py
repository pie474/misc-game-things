__author__ = 'chinmay'
import  pygame
from pygame.locals import *
from pygame.font import *
import time
import random

# Define some colors


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

grid_h = 4
grid_w = 4

marginx = 15
marginy = 15
spacex = (width - 2*marginx)/grid_w
spacey = (height - 2*marginy)/grid_h
square_w = (width - 2*marginx)/grid_w - 10
square_h = (height - 2*marginy)/grid_h - 10

screen_dim = [width,height]
screen = pygame.display.set_mode(screen_dim)

pygame.display.set_caption("Launchpad")
pygame.mixer.init
pygame.mixer.pre_init

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#sound = pygame.mixer.Sound("resources/audio/Launchpad_Clips/Fur Elise Dub 1.wav")
#sound.play(loops = 0)

sound_clips = [[pygame.mixer.Sound("foo") for i in range(grid_w)] for j in range(grid_h)]

for i in range(0,grid_w):
    for j in range(0,grid_h):
        filename = "resources/audio/Launchpad_Clips/Clip_" + str(i) + str(j) + ".wav"
        sound = pygame.mixer.Sound(filename)
        #sound.play(loops = 0)
        sound_clips[i][j] = sound


Colors = [[DARKGRAY for i in range(grid_w)] for j in range(grid_h)]

def genRandColor(hue):
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    if (hue==0):
        return (r,g,0)
    elif(hue==1):
        return (r,0,b)
    elif (hue==2):
        return (0,g,b)
    else:
        return (r,g,b)

#sound_clips[1][1].play(loops = 0)
#sound = pygame.mixer.Sound("resources/audio/Launchpad_Clips/Clip_11.wav")
#sound.play(loops = 0)
while True:
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()

    if keys[K_1]:
        pygame.mixer.stop()
        sound_clips[0][0].play(loops=0)
        Colors[0][0] = genRandColor(0)
    else: Colors[0][0] = DARKGRAY
    if keys[K_2]:
        pygame.mixer.stop()
        sound_clips[1][0].play(loops=0)
        Colors[1][0] = genRandColor(1)
    else: Colors[1][0] = DARKGRAY
    if keys[K_3]:
        pygame.mixer.stop()
        sound_clips[2][0].play(loops=0)
        Colors[2][0] = genRandColor(2)
    else: Colors[2][0] = DARKGRAY
    if keys[K_4]:
        pygame.mixer.stop()
        sound_clips[3][0].play(loops=0)
        Colors[3][0] = genRandColor(2)
    else: Colors[3][0] = DARKGRAY
    if keys[K_q]:
        pygame.mixer.stop()
        sound_clips[0][1].play(loops=0)
        Colors[0][1] = genRandColor(0)
    else: Colors[0][1] = DARKGRAY
    if keys[K_w]:
        pygame.mixer.stop()
        sound_clips[1][1].play(loops=0)
        Colors[1][1] = genRandColor(3)
    else: Colors[1][1] = DARKGRAY
    if keys[K_e]:
        pygame.mixer.stop()
        sound_clips[2][1].play(loops=0)
        Colors[2][1] = genRandColor(1)
    else: Colors[2][1] = DARKGRAY
    if keys[K_r]:
        pygame.mixer.stop()
        sound_clips[3][1].play(loops=0)
        Colors[3][1] = genRandColor(2)
    else: Colors[3][1] = DARKGRAY
    if keys[K_a]:
        pygame.mixer.stop()
        sound_clips[0][2].play(loops=0)
        Colors[0][2] = genRandColor(0)
    else: Colors[0][2] = DARKGRAY
    if keys[K_s]:
        pygame.mixer.stop()
        sound_clips[1][2].play(loops=0)
        Colors[1][2] = genRandColor(1)
    else: Colors[1][2] = DARKGRAY
    if keys[K_d]:
        pygame.mixer.stop()
        sound_clips[2][2].play(loops=0)
        Colors[2][2] = genRandColor(2)
    else: Colors[2][2] = DARKGRAY
    if keys[K_f]:
        pygame.mixer.stop()
        sound_clips[3][2].play(loops=0)
        Colors[3][2] = genRandColor(2)
    else: Colors[3][2] = DARKGRAY
    if keys[K_z]:
        pygame.mixer.stop()
        sound_clips[0][3].play(loops=0)
        Colors[0][3] = genRandColor(2)
    else: Colors[0][3] = DARKGRAY
    if keys[K_x]:
        pygame.mixer.stop()
        sound_clips[1][3].play(loops=0)
        Colors[1][3] = genRandColor(2)
    else: Colors[1][3] = DARKGRAY
    if keys[K_c]:
        pygame.mixer.stop()
        sound_clips[2][3].play(loops=0)
        Colors[2][3] = genRandColor(2)
    else: Colors[2][3] = DARKGRAY
    if keys[K_v]:
        pygame.mixer.stop()
        sound_clips[3][3].play(loops=0)
        Colors[3][3] = genRandColor(2)
    else: Colors[3][3] = DARKGRAY


    for i in range(0,grid_w):
        for j in range(0,grid_h):
            pygame.draw.rect(screen,Colors[i][j],[marginx+i*spacex,marginy+j*spacey,square_w,square_h])

    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if (event.type==pygame.QUIT):
            # if it is quit the game
            pygame.quit()
            exit(0)