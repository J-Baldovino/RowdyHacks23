import pygame
import random

#Color values
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#Pygame set up
pygame.init()

pygame.display.set_caption("Snake Game")

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#Fruit Positioning
fruitPosition = [random.randrange(1, (1280 // 10)) * 10,
                    random.randrange(1, (720 // 10)) * 10]
fruitSpawn = True

#Snake Head Position
snakePosX = 0
snakePosY = 0
orientation = 0 #0 = North, 1 = East, 2 = South, 3 = West

def turnController(orientation, keys):
    if keys[pygame.K_UP]  and orientation != 2:
        orientation = 0
    elif keys[pygame.K_RIGHT] and orientation != 3:
        orientation = 1
    elif keys[pygame.K_DOWN] and orientation != 0:
        orientation = 2
    elif keys[pygame.K_LEFT] and orientation != 1:
        orientation = 3
    return orientation

def movement(orientation, snakePosX, snakePosY):
    match orientation:
        case 0:
            snakePosY += 1
        case 1:
            snakePosX += 1
        case 2:
            snakePosY -= 1
        case 3:
            snakePosX -= 1
        case default:
            snakePosY += 1
    return (snakePosX, snakePosY)


#Main Function
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            orientation = turnController(orientation, pygame.key.get_pressed())
        if not fruitSpawn:
            fruitPosition = [random.randrange(1, (1280 // 10)) * 10,
                                random.randrange(1, (720 // 10)) * 10]
        fruitSpawn = True
        
        screen.fill(black)
        pygame.draw.rect(screen, white, pygame.Rect(fruitPosition[0], fruitPosition[1], 10, 10))

        position = movement(orientation, snakePosX, snakePosY)
        snakePosX = position[0]
        snakePosY = position[1]
        print("Orientation: " + str(orientation) + " PostionX: " + str(snakePosX) + " PositionY: " + str(snakePosY))
        
        pygame.display.update()

        #render game

        clock.tick(60)