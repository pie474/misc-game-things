__author__ = 'chinmay'
import  pygame
from pygame.locals import *
from pygame.font import *
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
width = 730
height = 730

maze_h = 20
maze_w = 20

screen_dim = [width,height]
screen = pygame.display.set_mode(screen_dim)

pygame.display.set_caption("aMAZEing Maze Sim")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#from PIL import Image

def gen_random_maze(mx,my):
    imgx = 500; imgy = 500
    #image = Image.new("RGB", (imgx, imgy))
    #pixels = image.load()
    mx = maze_w; my = maze_h # width and height of the maze
    maze = [[0 for x in range(mx)] for y in range(my)]
    dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
    color = [(0,0, 0), (255, 255, 255)] # RGB colors of the maze
    # start the maze from a random cell
    stack = [(random.randint(0, mx - 1), random.randint(0, my - 1))]

    while len(stack) > 0:
        (cx, cy) = stack[-1]
        maze[cy][cx] = 1
        # find a new cell to add
        nlst = [] # list of available neighbors
        for i in range(4):
            nx = cx + dx[i]; ny = cy + dy[i]
            if nx >= 0 and nx < mx and ny >= 0 and ny < my:
                if maze[ny][nx] == 0:
                    # of occupied neighbors must be 1
                    ctr = 0
                    for j in range(4):
                        ex = nx + dx[j]; ey = ny + dy[j]
                        if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                            if maze[ey][ex] == 1: ctr += 1
                    if ctr == 1: nlst.append(i)
        # if 1 or more neighbors available then randomly select one and move
        if len(nlst) > 0:
            ir = nlst[random.randint(0, len(nlst) - 1)]
            cx += dx[ir]; cy += dy[ir]
            stack.append((cx, cy))
        else: stack.pop()

    # paint the maze
    #for ky in range(imgy):
        #for kx in range(imgx):
            #pixels[kx, ky] = color[maze[my * ky / imgy][mx * kx / imgx]]
    #image.save("Maze_" + str(mx) + "x" + str(my) + ".png", "PNG")

    return maze

maze = gen_random_maze(maze_w,maze_h)

"""exit_x = maze_w-1
for j in range(0, maze_h):
    if (maze[maze_w-1][j] == 0):
        exit_y = j
        break
"""

pixelcnt = 0;
mazeaslist=[]


def genRandExit():
    while True:
        ri = random.randrange(0,maze_w)
        rj = random.randrange(0,maze_h)
        if (maze[ri][rj]==0): break
    exit_x = ri
    exit_y = rj
    return exit_x,exit_y

def mazeList():
    for i in range(0, maze_w):
        for j in range(0, maze_h):
            #print [i,j]
            if (maze[i][j] > 0):
                mazeaslist.append([i,j])

mazeList()


#(width-30)/maze_w==rectangle width
margin_w = 15
margin_h = 15
rect_w = (width-margin_w*2)/maze_w
rect_h = (height-margin_h*2)/maze_h

def dispText():
    # Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("Hello There", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

def drawrect(i,j,color):
    pygame.draw.rect(screen,color,[margin_w+rect_w*i,margin_h+rect_h*j,rect_w,rect_h])

def drawmaze():
    for i in range(0, maze_w):
        for j in range(0, maze_h):
            if (maze[i][j] > 0):
                #pygame.draw.rect(screen,BLUE,[30+20*i,30+20*j,20*maze[i][j],20*maze[i][j]])
                #pygame.draw.rect(screen,BLUE,[margin_w+rect_w*i,margin_h+rect_h*j,rect_w*maze[i][j],rect_h*maze[i][j]])
                drawrect(i,j,BLUE)


def doTheMove(to_x, to_y, from_x, from_y, listIdx, dir, mll):
    #print "Moving " + dir +" from " + str([from_x,from_y]) + " to " + str([to_x,to_y])
    if (to_x==exit_x and to_y==exit_y):
        val=0
        mazeaslist[listIdx] = mazeaslist[mll-1]
        mll -= 1
        #del(mazeaslist[listIdx])
    else:
        val=1
        mazeaslist[listIdx] = [to_x,to_y]

    maze[to_x][to_y] = val
    maze[from_x][from_y] = 0

    drawrect(exit_x,exit_y,GREEN)

    drawmaze()

    pygame.display.flip()

    return mll

    #time.sleep(.5)


def random_move(mll):
    if (mll == 0):
        return
    #r = random.randrange(0,len(mazeaslist))
    r = random.randrange(0,mll)
    [ri,rj] = mazeaslist[r]
    #print r
    #print mazeaslist


    #if (exit_x-ri > 0): snix = 1
    #else: snix = 0  #snix cant be -1
    snix = exit_x - ri
    if (snix > 0): snix = 1
    elif (snix < 0): snix = -1

    sniy = exit_y - rj
    if (sniy > 0): sniy = 1
    elif (sniy < 0): sniy = -1
    """
    if (snix==0):
        coin = random.random()
        if (coin < .1):
            snix=1
        elif (coin < .2):
            snix=-1

    if (sniy==0):
        coin = random.random()
        if (coin < .1):
            sniy = 1
        if (coin < .2):
            sniy = -1
    """
    #print "[ri,rj]= " + str([ri,rj]) + str([snix,sniy])

    if (maze[ri+snix][rj+sniy] == 0): #NE
        # can move
        mll = doTheMove(ri+snix,rj+sniy,ri,rj,r, "NE", mll)

    elif (maze[ri+snix][rj] == 0): #E

        mll = doTheMove(ri+snix,rj,ri,rj,r, "E", mll)

    elif (maze[ri][rj+sniy] == 0): #N

        mll = doTheMove(ri,rj+sniy,ri,rj,r, "N", mll)

    elif (ri>0 and ri < maze_w -1 and maze[ri-snix][rj+sniy] == 0): #NW

        mll = doTheMove(ri-snix,rj+sniy,ri,rj,r, "NW", mll)

    elif (rj<maze_h-1 and rj > 0 and maze[ri+snix][rj-sniy] == 0): #SE

        mll = doTheMove(ri+snix,rj-sniy,ri,rj,r, "SE", mll)

    elif (rj>0 and rj<maze_h-1 and maze[ri][rj-sniy] == 0): #S

        mll = doTheMove(ri,rj-sniy,ri,rj,r, "S", mll)

    elif (ri>0 and ri < maze_w-1 and maze[ri-snix][rj] == 0): #W

        mll = doTheMove(ri-snix,rj,ri,rj,r, "W", mll)

    elif (ri>0 and ri < maze_w-1 and rj<maze_h-1 and rj>0 and maze[ri-snix][rj-sniy] == 0): #SW

        mll = doTheMove(ri-snix,rj-sniy,ri,rj,r, "SW", mll)

    return mll


def main(mll):
    totalsteps = 0
    while True:
        screen.fill(WHITE)

        if (mll>0):
            totalsteps += 1
            mll = random_move(mll)

        #raw_input("Press Enter to continue...")
        if (mll==0):
            print totalsteps
            mll=-1
        #pygame.display.flip()
        # 8 - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button
            if (event.type == pygame.QUIT):
                # if it is quit the game
                quit()

"""
drawmaze()
dispText()
pygame.display.flip()
main(0)
"""
exit_x,exit_y=genRandExit()
main(len(mazeaslist))