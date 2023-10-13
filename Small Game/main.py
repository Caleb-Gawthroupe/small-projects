import pygame
import random
import ai
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 700
HEIGHT = 500

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False

#Debug
Debug = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#Object Set Up
class Player:
    def __init__(self, speed, x, y, w, h):
        self.speed = speed
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sprite = pygame.Rect(x,y,w,h)
        self.score = 0

class Ball:
    def __init__(self, speed, pos, r, c):
        self.speed = [speed,speed]
        self.pos = pos
        self.r = r
        self.c = c
        self.dir = dir

class Coin:
    def __init__(self, pos,max_worth, r, c):
        self.pos = pos
        self.max_worth = max_worth
        self.worth = max_worth
        self.r = r
        self.c = c

player = Player(5, WIDTH/2, HEIGHT/2, 32, 32)
ball = Ball(8, [25,25],32, RED)
coin = Coin([50,100],100,16,GREEN)

def playerMove():
    keys = pygame.key.get_pressed()
     # -- Player Move
    if keys[pygame.K_LEFT]:
        player.x -= player.speed

    if keys[pygame.K_RIGHT]:
        player.x += player.speed

    if keys[pygame.K_UP]:
        player.y -= player.speed

    if keys[pygame.K_DOWN]:
        player.y += player.speed
    
    player.sprite = pygame.Rect(player.x,player.y,player.w,player.h)   
    
def screenBorder(x,y):
    if x > WIDTH or x < 0-player.w or y < 0-player.h or y > HEIGHT:
        return True
    return False

def draw():
    # --- Reset Screen
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, BLACK, player.sprite)
    pygame.draw.circle(screen,ball.c,[ball.pos[0],ball.pos[1]],ball.r) 
    pygame.draw.circle(screen,coin.c,coin.pos,coin.r*(coin.worth/100))  

def ballEdge(pos,speed):
    if pos[0]+speed[0] <= 0 or pos[0]+speed[0] >= WIDTH:
        speed[0]=speed[0]*-1
    if pos[1]+speed[1] <= 0 or pos[1]+speed[1] >= HEIGHT:
        speed[1]=speed[1]*-1
    return speed

def ballMove(pos, speed):
    pos[0]+=speed[0]
    pos[1]+=speed[1]
    return pos

def coinWorth(worth):
    if worth > 0:
        worth -= 0.25
    else:
        worth = coin.max_worth
    if coinCollision():
        worth = coin.max_worth
    return worth

def coinCollision():
    #Get the are the player is covering
    pL = player.x
    pR = player.x+player.w
    cL = coin.pos[0]-coin.r
    cR = coin.pos[0]+coin.r
    
    pT = player.y
    pB = player.y+player.h
    cT = coin.pos[1]-coin.r
    cB = coin.pos[1]+coin.r
    
    
    x_col = False
    y_col = False
    
    if cL > pL and cL < pR:
        x_col = True
    elif cR > pL and cR < pR:
        x_col = True
    else:
        x_col = False

    if cT > pT and cT < pB:
        y_col = True
    elif cB > pT and cB < pB:
        y_col = True
    else:
        y_col = False

    
    if y_col == True and x_col == True:
        player.score+=coin.worth/10
        return True
    return False

def coinMove(worth, pos):
    if worth == 0 or coinCollision():
        pos = [random.randint(10,WIDTH-10),random.randint(10,HEIGHT-10)]
    return pos

def ballCollision():
    pL = player.x
    pR = player.x+player.w
    cL = ball.pos[0]-ball.r
    cR = ball.pos[0]+ball.r
    
    pT = player.y
    pB = player.y+player.h
    cT = ball.pos[1]-ball.r
    cB = ball.pos[1]+ball.r
    
    
    x_col = False
    y_col = False
    
    if cL > pL and cL < pR:
        x_col = True
    elif cR > pL and cR < pR:
        x_col = True
    else:
        x_col = False

    if cT > pT and cT < pB:
        y_col = True
    elif cB > pT and cB < pB:
        y_col = True
    else:
        y_col = False

    
    if y_col == True and x_col == True:
        return True
    return False    

def debug():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                print(player.score)
    
    


# -------- Main Program Loop -----------
while not done:
    done = screenBorder(player.x,player.y)
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                print(player.score)
 
    # --- Game logic should go here
    
    playerMove()
    ball.dir = ballEdge(ball.pos,ball.speed)
    ball.pos = ballMove(ball.pos, ball.speed)
    coin.worth = coinWorth(coin.worth)
    coin.pos = coinMove(coin.worth,coin.pos)
    if ballCollision():
        player.score -= 15
    if Debug:
        debug()
    
    player.score = round(player.score)





    # -- AI LOGIC
    #print(ai.inputs(player.x,player.y,ball.pos,ball.speed,coin.pos))






    # --- Screen-clearing code goes here
    
    draw()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
# Close the window and quit.
pygame.quit()
