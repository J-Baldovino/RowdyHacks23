from bullet import Bullet
import pygame
import random

#Color values
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#Fruit Sprite
class Fruit(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (32, 32))
player = Fruit("sprites/apple.png")

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

#Snake Position
snakePosX = 100
snakePosY = 100
orientation = 0 #0 = North, 1 = East, 2 = South, 3 = West
snake_body = [[100,100],
              [90, 100],
              [80, 100],
              [70, 100]  
            ]
bullets = []

def turnController(orientation, keys):
    if keys[pygame.K_UP]  and orientation != 2:
        orientation = 0
    elif keys[pygame.K_RIGHT] and orientation != 3:
        orientation = 1
    elif keys[pygame.K_DOWN] and orientation != 0:
        orientation = 2
    elif keys[pygame.K_LEFT] and orientation != 1:
        orientation = 3
    elif keys[pygame.K_SPACE]:
        print("pew") #debug code
        bullets.append(Bullet(snakePosX, snakePosY, orientation))
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
    return (snakePosX, snakePosY)

#Display Fruit
def showFruit():
    screen.blit(player.image, fruitPosition)

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

        for pos in snake_body:
            pygame.draw.rect(screen, green, 
                             pygame.Rect(pos[0], pos[1], 10, 10))

        i = 0 #debug code    
        for bullet in bullets:
            i += 1 #debug code
            bullet.bulletTravel()
            pygame.draw.rect(screen, white, 
                             pygame.Rect(bullet.getPosX(), bullet.getPosY(), 10, 10))
            print("Bullet " + str(i) + ": " + " Orientation: " + str(bullet.getOrientation()) + " PositionX: " + str(bullet.getPosX()) + " PositionY: " + str(bullet.getPosY()))

        screen.fill(black)
        showFruit()

        position = movement(orientation, snakePosX, snakePosY)
        snakePosX = position[0]
        snakePosY = position[1]
        print("Orientation: " + str(orientation) + " PostionX: " + str(snakePosX) + " PositionY: " + str(snakePosY)) #debug code
        
        pygame.display.update()

        #render game

        clock.tick(60)