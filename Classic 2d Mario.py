__author__ = 'chinmay'
import pygame
from timeit import default_timer as timer
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
player_x = 320
player_y = 63
cph = 0
chw = 0
goomba_x = 20
goomba_y = 63
goomba_direction = 1
goomba_walk = 1
goomba_stomped = 0
stomp_timer = 0
goomba_dead = 0
player_costume = 1
y_velocity = 0
gravity = 1
onground = 1
itembox1_alive = 1
itembox1_hit = 0
itembox1_y = 130
itembox1_x = 200
start = timer()
mushroom_y = 130
mushroom_emerged = 0
mushroom_x = 200
mushroom_alive = 1

pygame.display.set_caption('Super Mario')
sound = pygame.mixer.Sound("resources/audio/mario_bros_theme.wav")
sound.play(loops = -1)

# 3 - Load images
player = pygame.image.load("resources/images/Mario Images/m1.png")
player2 = pygame.image.load("resources/images/Mario Images/m2.png")
player3 = pygame.image.load("resources/images/Mario Images/m3.png")
super_player = pygame.image.load("resources/images/Mario Images/smario1.png")
super_player2 = pygame.image.load("resources/images/Mario Images/smario2.png")
super_player3 = pygame.image.load("resources/images/Mario Images/smarioj1.png")
background = pygame.image.load("resources/images/Mario Images/background sky.png")
ground = pygame.image.load("resources/images/Mario Images/ground.png")
goomba1 = pygame.image.load("resources/images/Mario Images/g1.png")
goomba2 = pygame.image.load("resources/images/Mario Images/g2.png")
flatgoomba = pygame.image.load("resources/images/Mario Images/fg.png")
alive_item_box_1 = pygame.image.load("resources/images/Mario Images/itembox1.png")
dead_item_box = pygame.image.load("resources/images/Mario Images/itemboxdead.png")
super_mushroom = pygame.image.load("resources/images/Mario Images/super_mushroom.png")
icon = pygame.image.load("resources/images/Mario Images/a2eea58289b17188a0e5047d045fb14e_icon.png")

pygame.display.set_icon(icon)

player_super = 0
current_player = player

# 4 - keep looping through
while 1:
    cpw = current_player.get_width()
    cph = current_player.get_height()
    keys = pygame.key.get_pressed()
    skp = 0
    if keys[K_UP]:
        skp=1
        if (onground == 1):
            y_velocity = 17
            player_y += y_velocity
            onground = 0
            player_costume = 3
    if keys[K_RIGHT]:
        if (not ((player_x + cpw > itembox1_x) and (player_x < itembox1_x + alive_item_box_1.get_width()) and  (player_y > itembox1_y - alive_item_box_1.get_height()) and (player_y - cph < itembox1_y))):
                player_x += 4
        skp = 1
        if (round(8 * timer()) % 2 == 1):
            player_costume = 1
        else:
            player_costume = 2
    if keys[K_LEFT]:
        player_x -= 4
        skp = 1
        if (round(8*timer()) % 2 == 0):
            player_costume = 1
        else:
            player_costume = 2
    if (skp==0 and onground==1):
        player_costume = 1
    if (player_y > 63):
        onground = 0
        player_costume = 3
    else:
        onground = 1
    if ((player_y < itembox1_y + cph + 10) and (player_y > itembox1_y + cph) and (player_x < itembox1_x + alive_item_box_1.get_width()) and (player_x > itembox1_x - cpw)):
        onground = 1
        player_costume = 1
    if (onground == 0):
        y_velocity = y_velocity - gravity
    else:
        y_velocity = 0
    player_y = player_y + y_velocity
    if (goomba_x < 20):
        goomba_direction = 1
    if (goomba_x > 600):
        goomba_direction = 0
    if (goomba_direction == 1):
        if (goomba_stomped == 0):
            goomba_x += 1
    else:
        if (goomba_stomped == 0):
            goomba_x -= 1
    if (player_y < (goomba_y + 13) and player_y > (goomba_y ) and player_x < (goomba_x + player.get_width()) and player_x > (goomba_x - player.get_width()) and goomba_stomped == 0):
        goomba_stomped = 1
        stomp_timer = timer()
        y_velocity = 5
        onground = 0
    if (round(timer() - stomp_timer) == 1):
        goomba_dead = 1

    if (player_super == 0):
        if (player_y < itembox1_y - alive_item_box_1.get_height() and player_y > itembox1_y - alive_item_box_1.get_height() - 8 and player_x > 200 - player.get_width() and player_x < 200 + player.get_width()):
            y_velocity = -1
            itembox1_hit = 1
            itembox1_alive = 0
    else:
        if (player_y < itembox1_y - alive_item_box_1.get_height() - 8 and player_y > itembox1_y - alive_item_box_1.get_height() - 18 and player_x > 200 - super_player.get_width() and player_x < 200 + super_player.get_width()):
            y_velocity = -1
            itembox1_hit = 1
            itembox1_alive = 0

    if (player_x > 625):
        player_x = 15
    elif (player_x < 15):
        player_x = 625

    if (itembox1_hit == 1 and mushroom_emerged == 0):
        if (mushroom_y < 129 + super_mushroom.get_width()):
            mushroom_y += 1
        else:
            mushroom_emerged = 1

    if (mushroom_emerged == 1 and player_x > mushroom_x - player.get_width() and player_x < mushroom_x + player.get_width() and player_y > mushroom_y - player.get_height() and player_y < mushroom_y + player.get_height()):
        player_super = 1
        mushroom_alive = 0

    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background, (-50, -100))
    screen.blit(ground, (0, 447))
    screen.blit(ground, (477, 447))
    if (itembox1_hit == 1 and mushroom_alive == 1):
        screen.blit(super_mushroom, (200, height - mushroom_y))
    if (itembox1_alive == 1):
        screen.blit(alive_item_box_1, (itembox1_x, height - itembox1_y))
    else:
        screen.blit(dead_item_box, (itembox1_x, height - itembox1_y))
    if (goomba_dead == 0):
        if (goomba_stomped == 1):
            screen.blit(flatgoomba, (goomba_x, height - goomba_y + 15))
        else:
            screen.blit(goomba1, (goomba_x, height - goomba_y))
    if (player_costume == 3):
        if (player_super == 0):
            screen.blit(player3, (player_x, (height - player_y)))
            current_player = player3
        else:
            screen.blit(super_player3, (player_x, (height - player_y - (super_player3.get_height() - player3.get_height()))))
            current_player = super_player3
    else:
        if (player_costume == 1):
            if (player_super == 0):
                screen.blit(player, (player_x, (height - player_y)))
                current_player = player
            else:
                screen.blit(super_player, (player_x, (height - player_y - (super_player.get_height() - player.get_height()))))
                current_player = super_player
        else:
            if (player_costume == 2):
                if(player_super == 0):
                    screen.blit(player2, (player_x - 4, (height - player_y)))
                    current_player = player2
                else:
                    screen.blit(super_player2, (player_x, (height - player_y - (super_player2.get_height() - player2.get_height()))))
                    current_player = super_player2
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if (event.type == pygame.QUIT):
            # if it is quit the game
            pygame.quit()
            exit(0)