import pygame
import time
import random

snake_speed = 15

x_window = 720
y_window = 480

#Color definition
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#Fruit Sprite
class Fruit(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (16, 16))
player = Fruit("sprites/apple.png")

#Initialize pygame and game window
pygame.init()
pygame.display.set_caption("RowdyHacks 2023")
game_window = pygame.display.set_mode((x_window, y_window))

#Sets the controller speed
fps = pygame.time.Clock()

#Default snake position
snake_pos = [100,50]

#Create the beginning snake body
snake_body = [ [100, 50], [90,50], [80, 50], [70, 50] ]

#Fruit positioning and spawn
fruit_pos = [random.randrange(1, (x_window // 10)) * 10, random.randrange(1, (y_window // 10)) * 10]
fruit_spawn = True

#Set default snake direction
direction = "RIGHT"
change_dir = direction

def showFruit():
    game_window.blit(player.image, fruit_pos)

def game_over():
    time.sleep(2)

    #Deactivate pygame
    pygame.quit()

    quit()

#Loop continues the game
while True:

    #Movement keys
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_dir = 'UP'
            if event.key == pygame.K_DOWN:
                change_dir = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_dir = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_dir = 'RIGHT'

    #Prevent multiple simultaneous key inputs 
    if change_dir == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_dir == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_dir == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_dir == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    #Snake movement
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    #Simulates fruit and snake collision 
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        fruit_spawn = False
    else:
        snake_body.pop()

    #Respawn fruit in a different position
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (x_window // 10)) * 10, random.randrange(1, (y_window // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        snake_rect = pygame.draw.rect(game_window, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
    
    polygon_points = ((200, 200), (240, 200), (240, 280), (280, 280),
                      (280, 320), (240, 320), (240, 400), (200, 400),
                      (200, 360), (160, 360), (160, 300), (200, 300), (200, 200))
    border = pygame.draw.polygon(game_window, red, polygon_points, 1)

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > x_window-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > y_window-10:
        game_over()    
    if snake_rect.colliderect(border) :
        game_over()

    #Show's fruit
    showFruit()

    #Refreshing the game screen
    pygame.display.update()

    #Sets the frames per second
    fps.tick(snake_speed)

