import pygame
import time
import random


# -- Color Setup
WHITE = (230,230,230)
BLACK = (0,0,0)
GREEN = (0,255,0)

# -- Screen Setup
WIDTH = 720
HEIGHT = 520
size = (WIDTH+20, HEIGHT+20)
game_speed = 0.065 

speed = 20
snake_size = 20
head = [WIDTH/2, HEIGHT/2]
body = [[WIDTH/2,speed+HEIGHT/2],[WIDTH/2,speed*2+HEIGHT/2], [WIDTH/2,speed*3+HEIGHT/2]]
fruit = [random.randint(0,WIDTH/20)*20,random.randint(0,HEIGHT/20)*20]
direction = 0
eating = False


def updateBody(head, body, eating):
    new = [0,0]
    new[0] = head[0]
    new[1] = head[1]
    body.insert(0,new)
    if eating == False:
        body.pop()
    else:
        eating = False
    return body

def updateHead(head, direction, speed):
    if direction == 0:
        head[1]-=speed
    elif direction == 1:
        head[0] += speed
    elif direction == 2:
        head[1] += speed
    elif direction == 3:
        head[0] -= speed
    return head

def moveFruit():
    new_location = [0,0]
    new_location[0] = random.randint(0,WIDTH/20)*20
    new_location[1] = random.randint(0,HEIGHT/20)*20
    return new_location

def eatFruit(head,f):
    if head == f:
        return True
    return False

def die():
    if head in body:
        return True
    if head[0] > WIDTH or head[0] < 0 or head[1] < 0 or head[1] > HEIGHT:
        return True 
    return False


pygame.init()


# -- Pygame display Setup
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

done = False

# -- Functions

def draw(body, head):
    # -- Reset Display
    screen.fill(WHITE)
    
    # -- Draw Snake
    pygame.draw.rect(screen,BLACK,pygame.Rect(head[0],head[1],snake_size,snake_size))
    
    for square in body:
        pygame.draw.rect(screen,BLACK,pygame.Rect(square[0],square[1],snake_size,snake_size))

    pygame.draw.rect(screen,GREEN,pygame.Rect(fruit[0],fruit[1],snake_size,snake_size))

             
# -- Main Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 2:
                    direction = 0
            if event.key == pygame.K_RIGHT:
                if direction != 3:
                    direction = 1
            if event.key == pygame.K_DOWN:
                if direction != 0:
                    direction = 2
            if event.key == pygame.K_LEFT:
                if direction != 1:
                    direction = 3


    eating = eatFruit(head, fruit)
    if eating:
        fruit = moveFruit()
    body = updateBody(head, body, eating)
    head = updateHead(head, direction, speed)
    done = die()
     
    time.sleep(game_speed)
    
    
    # -- Draw Logic
    draw(body, head)
    pygame.display.flip()