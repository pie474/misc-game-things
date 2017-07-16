__author__ = 'praveen'
import  pygame
from pygame.locals import *
from pygame.font import *
import time
import random

import randMazeGen

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LRED = (180,0,0)
BLUE = (0, 0, 255)
ORANGE = (255, 160, 0)
LORANGE = (192, 120, 0)
pygame.init()
pygame.font.init

# Set the width and height of the screen [width, height]
width = 730
height = 730

maze_h = 39
maze_w = 39


screen_dim = [width,height]
screen = pygame.display.set_mode(screen_dim)

pygame.display.set_caption("aMAZEing Maze Sim")

big = pygame.mixer.Sound("resources/audio/megashroom.wav")

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

#maze = gen_random_maze(maze_w,maze_h)

mazeM = randMazeGen.randMazeGen1(maze_w/2,maze_h/2)

def convert(mazeM):
    num_rows = maze_w/2
    num_cols = maze_h/2
    mx = maze_w; my = maze_h # width and height of the maze
    maze = [[0 for x in range(mx+1)] for y in range(my+1)]
    for row in range(0,num_rows):
        for col in range(0,num_cols):
            cell_data = mazeM[row,col]
            #LEFT,UP,RIGHT,DOWN
            #in maze, we are at 2*row+1, 2*col+1
            if (cell_data[0] == 0):
                #left wall exists
                maze[2*row][2*col] = 1
                maze[2*row+1][2*col] = 1
            if (cell_data[1] == 0):
                #Up wall exists
                maze[2*row][2*col] = 1
                maze[2*row][2*col+1] = 1

            # for right wall, next cell will get it
            # for down wall, next cell will get it
    # now get the right most wall and the bottom most
    for row in range(0,num_rows):
        cell_data = mazeM[row,num_cols-1] # last col
        if (cell_data[2] == 0):
            maze[2*row][2*num_cols] = 1
            maze[2*row+1][2*num_cols] = 1
    for col in range(0,num_cols):
        cell_data = mazeM[num_rows-1,col] # last row
        if (cell_data[3] == 0):
            maze[2*num_rows][2*col] = 1
            maze[2*num_rows][2*col+1] = 1
    # last corner
    cell_data = mazeM[num_rows-1,num_cols-1]
    if (cell_data[3] == 0):
        maze[2*num_rows][2*num_cols] = 1

    return maze


maze = convert(mazeM)

#print maze

def genBotExit():
    exit_y = maze_h-1
    for i in range(0, maze_w+1):
        if (maze[i][exit_y] == 0):
            exit_x = i
            break
    return exit_x,exit_y

def genBotEntry(where):
    ent_y = maze_h-1
    if (where == 0):
        strt = 0
        end = maze_w
        step = 1
    else:
        strt = maze_w-1
        end = 0
        step = -1
    for i in range(strt, end, step):
        if (maze[i][maze_h-1] == 0):
            ent_x = i
            break
    return ent_x,ent_y

pixelcnt = 0;
mazeaslist=[]

def genRandEnt():
    while True:
        ri = random.randrange(0,maze_w)
        rj = random.randrange(0,maze_h)
        if (maze[ri][rj] == 0):
            return ri,rj


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
rect_w = (width-margin_w*2)/(maze_w+1)
rect_h = (height-margin_h*2)/(maze_h+1)

def dispText():
    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (100, 100, 100))
    textpos = text.get_rect()
    textpos.centerx = 100 #background.get_rect().centerx
    textpos.centery = height-20
    screen.blit(text, textpos)

def texts(scoretext,color,x,y):
   font=pygame.font.Font(None,30)
   st=font.render(scoretext, 1,color)
   #screen.blit(scoretext, (20, height-30))
   screen.blit(st,(x,y))

def drawrect(i,j,color):
    pygame.draw.rect(screen,color,[margin_w+rect_w*i,margin_h+rect_h*j,rect_w,rect_h])

def drawfood(i,j):
    pygame.draw.rect(screen,WHITE,[margin_w+rect_w*i+rect_w/2,margin_h+rect_h*j+rect_h/2,2,2])

def drawmazeWithFood():
    screen.fill(BLACK)
    for i in range(0, maze_w+1):
        for j in range(0, maze_h+1):
            if (maze[i][j] > 0):
                #pygame.draw.rect(screen,BLUE,[30+20*i,30+20*j,20*maze[i][j],20*maze[i][j]])
                #pygame.draw.rect(screen,BLUE,[margin_w+rect_w*i,margin_h+rect_h*j,rect_w*maze[i][j],rect_h*maze[i][j]])
                drawrect(i,j,BLUE)
            if (maze[i][j] == 0):
                drawfood(i,j)


def drawmaze():
    screen.fill(BLACK)
    for i in range(0, maze_w+1):
        for j in range(0, maze_h+1):
            if (maze[i][j] > 0):
                #pygame.draw.rect(screen,BLUE,[30+20*i,30+20*j,20*maze[i][j],20*maze[i][j]])
                #pygame.draw.rect(screen,BLUE,[margin_w+rect_w*i,margin_h+rect_h*j,rect_w*maze[i][j],rect_h*maze[i][j]])
                drawrect(i,j,BLUE)


def drawSmoothMove(to_x, to_y, from_x, from_y, color):
    dx = to_x - from_x
    dy = to_y - from_y

    fx = from_x*rect_w
    fy = from_y*rect_h
    sx=0;sy=0
    if (dx > 0):sx = 1
    elif (dx < 0): sx = -1

    if (dy > 0): sy = 1
    elif (dy < 0): sy =-1

    while fx != to_x*rect_w or fy != to_y*rect_h:

        rectb = pygame.draw.rect(screen,BLACK,[margin_w+fx, margin_h+fy, rect_w, rect_h])
        if (fx != to_x*rect_w):
            fx += sx
        else:
            sx = 0
        if (fy != to_y*rect_h):
            fy += sy
        else:
            sy = 0
        #print [fx,fy]
        rect=pygame.draw.rect(screen,color,[margin_w+fx, margin_h+fy, rect_w, rect_h])
        pygame.display.update(rect)



def doTheMove(to_x, to_y, from_x, from_y, predOrPrey,ts):
    #print "Moving " + dir +" from " + str([from_x,from_y]) + " to " + str([to_x,to_y])

    drawrect(exit_x,exit_y,GREEN)

    #drawmaze()

    if (predOrPrey == 0):
        drawrect(to_x,to_y,ORANGE)
        #drawSmoothMove(to_x,to_y,from_x,from_y,ORANGE)
        if (mazeForPrey[to_x][to_y] == 0): #eating food
            texts("Score: " + str(ts),BLACK,20, height-30)
            ts += 100
            texts("Score: " + str(ts),WHITE, 20, height-30)
        mazeForPrey[to_x][to_y] += 1
        drawrect(from_x, from_y,BLACK)
    else:
        drawrect(to_x,to_y,RED)
        mazeForPred[to_x][to_y] += 1
        #drawrect(from_x, from_y,LRED)
        drawrect(from_x, from_y,BLACK)
        if (mazeForPrey[from_x][from_y] == 0): #prey hasn't visited this square
            drawfood(from_x, from_y)
    pygame.display.flip()
    return ts

    #time.sleep(.5)

def random_move_pred(pred_x,pred_y):
    ri = pred_x
    rj = pred_y
    if (ri == exit_x and rj == exit_y): return
    #get open neighbors
    openneighbors=[]
    leastVisited = 100000000
    nxl = -1
    nyl = -1
    numSame = 0
    for i in range (-1,2,1):
        nx = ri + i
        if (nx <0 or nx>maze_w-1): continue
        for j in range (-1,2,1):
            if (j==0 and i==0): continue
            ny = rj + j
            if (ny < 0 or ny > maze_h-1): continue
            if (mazeForPred[nx][ny] != -1):
                openneighbors.append([nx,ny])
                if (leastVisited > mazeForPred[nx][ny]):
                    leastVisited = mazeForPred[nx][ny]
                    nxl = nx
                    nyl = ny
                elif (leastVisited == mazeForPred[nx][ny]):
                    numSame += 1
    l = len(openneighbors)
    if (l>0):

        if (numSame < l-1):
            [ri,rj] = [nxl,nyl]

        elif (numSame == l-1):
            r = random.randrange(0,len(openneighbors))
            #print openneighbors

            [ri,rj] = openneighbors[r]
        doTheMove(ri,rj, pred_x, pred_y, 1,-1)

    return ri, rj

def random_move_prey(prey_x,prey_y):

    if (prey_x==exit_x and prey_y == exit_y): return
    ri = prey_x
    rj = prey_y

    #get open neighbors
    openneighbors=[]
    leastVisited = 10000000
    nxl = -1
    nyl = -1
    numSame = 0
    for i in range (-1,2,1):
        nx = ri + i
        if (nx <0 or nx>maze_w-1): continue
        for j in range (-1,2,1):
            if (j==0 and i==0): continue
            ny = rj + j
            if (ny < 0 or ny > maze_h-1): continue
            if (mazeForPrey[nx][ny] != -1):
                openneighbors.append([nx,ny])
                if (leastVisited > mazeForPrey[nx][ny]):
                    leastVisited = mazeForPrey[nx][ny]
                    nxl = nx
                    nyl = ny
                elif (leastVisited == mazeForPrey[nx][ny]):
                    numSame += 1

    l = len(openneighbors)
    if (l>0):

        if (numSame < l-1):
            [ri,rj] = [nxl,nyl]

        elif (numSame == l-1):
            r = random.randrange(0,len(openneighbors))
            #print openneighbors

            [ri,rj] = openneighbors[r]
        doTheMove(ri,rj, prey_x, prey_y, 0)

    return ri,rj

def checkIfPreyNear(prey_x,prey_y,pred_x,pred_y):
    dx = pred_x - prey_x
    dy = pred_y - prey_y
    if (dx*dx + dy*dy < 64): #less than 8 blocks away
        big.play(loops = 0)
        for i in range(0,30,1):
            pygame.draw.rect(screen,RED,[margin_w+rect_w*pred_x,margin_h+rect_h*pred_y,rect_w+i,rect_h+i])
            pygame.display.flip()
        return True
    return False

def chasePrey(prey_x,prey_y,pred_x,pred_y):
    dx = pred_x - prey_x
    dy = pred_y - prey_y

    if (dx < 0): sx = -1
    elif (dx > 0): sx = 1
    elif (dx == 0): sx = 0

    if (dy < 0): sy = -1
    elif (dy > 0): sy = 1
    elif (dy == 0): sy = 0

    ri = pred_x - 1.5*sx
    rj = pred_y - 1.5*sy

    #print [pred_x,pred_y]
    #print [ri,rj]
    #print "\n"

    if (ri <0): ri = 0
    if (ri >maze_w-1): ri = maze_w-1
    if (rj<0): rj = 0
    if (rj > maze_h-1): rj = maze_h-1

    drawrect(exit_x,exit_y,GREEN)

    drawmaze()

    pygame.draw.rect(screen,RED,[margin_w+rect_w*ri, margin_h+rect_h*rj, rect_w+30, rect_h+30])
    #pygame.draw.rect(screen,BLACK,[margin_w+rect_w*pred_x, margin_h+rect_h*pred_y, rect_w+30, rect_h+30])
    pygame.display.flip()

    #time.sleep(1)
    return ri,rj

mazeForPrey = [[0 for x in range(maze_w+1)] for y in range(maze_h+1)]
mazeForPred = [[0 for x in range(maze_w+1)] for y in range(maze_h+1)]
for i in range(0, maze_w):
    for j in range(0, maze_h):
        #these mazes have -1 for walls and 0 for empty.  0 means not yet visted.
        # they will hold number of times visited during the moves
        mazeForPrey[i][j] = -1*maze[i][j]
        mazeForPred[i][j] = -1*maze[i][j]


def main():
    prey_x,prey_y = genRandEnt() #genBotEntry(0)
    pred_x,pred_y = genRandEnt() #genBotEntry(1)



    totalsteps = 0
    mll = 1
    chase = False
    while True:
        #screen.fill(BLACK)
        #time.sleep(.1)
        totalsteps += 1
        if (mll > 0):
            if (prey_x != exit_x or prey_y != exit_y):
                prey_x,prey_y = random_move_prey(prey_x,prey_y)
            else:
                mll = 0

            if (chase == False):
                if (pred_x != exit_x or pred_y != exit_y):
                    pred_x,pred_y = random_move_pred(pred_x,pred_y)
                else:
                    mll = 0

            if (chase == False and checkIfPreyNear(prey_x,prey_y,pred_x,pred_y) == True):
                chase = True

            if (chase==True):
                pred_x,pred_y=chasePrey(prey_x,prey_y,pred_x,pred_y)

            if (pred_x == prey_x and pred_y == prey_y):
                pygame.mixer.stop()
                print "Pwned"
                mll = 0

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



def main2():
    prey_x,prey_y = genRandEnt() #genBotEntry(0)
    pred_x,pred_y = genRandEnt() #genBotEntry(1)
    dx = 0
    dy = 0
    chase = False
    done = 0
    totalscore = 0
    while True:
        for event in pygame.event.get():
            # check if the event is the X button
            if (event.type == pygame.QUIT):
                # if it is quit the game
                quit()
        if (done==1):
            continue
        if (chase == False):
            if (pred_x != exit_x or pred_y != exit_y):
                pred_x,pred_y = random_move_pred(pred_x,pred_y)
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            dy = -1
            dx = 0
        if keys[K_DOWN]:
            dy = 1
            dx = 0
        if keys[K_LEFT]:
            dx = -1
            dy = 0
        if keys[K_RIGHT]:
            dx = 1
            dy = 0

        if (maze[prey_x+dx][prey_y+dy] == 0):
            totalscore = doTheMove(prey_x+dx,prey_y+dy,prey_x,prey_y,0,totalscore)
            #drawSmoothMove(prey_x+dx, prey_y+dy, prey_x, prey_y, ORANGE)
            prey_x += dx
            prey_y += dy
        if (chase == False and checkIfPreyNear(prey_x,prey_y,pred_x,pred_y) == True):
            chase = True

        if (chase==True):
            pred_x,pred_y=chasePrey(prey_x,prey_y,pred_x,pred_y)

        if (pred_x == prey_x and pred_y == prey_y):
            pygame.mixer.stop()
            texts("Pwned", WHITE, 200, height-30)
            done = 1


drawmazeWithFood()

pygame.display.flip()
exit_x,exit_y = genBotExit()
main2()