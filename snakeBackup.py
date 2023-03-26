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
orange = pygame.Color(211, 67, 13)
dark_blue = pygame.Color(12, 35, 64)

#Initialize pygame and game window
pygame.init()
pygame.display.set_caption("RowdyHacks 2023")
game_window = pygame.display.set_mode((x_window, y_window))

#Sets the controller speed
fps = pygame.time.Clock()

#Default snake position
snake_pos = [100,50]

#Create the beginning snake body
snake_body = [ [100, 50] ]

#Fruit positioning and spawn
fruit_pos = [random.randrange(1, (x_window // 10)) * 10, random.randrange(1, (y_window // 10)) * 10]
fruit_spawn = True

#Obstacle positioning and spawn
obst_pos = []
obst_spawn = True

#Randomly generate obstacle position
def obst_pos_gen():
    return [random.randrange(1, (x_window // 10)) * 10, random.randrange(1, (y_window // 10)) * 10]

#Set default snake direction
direction = "RIGHT"
change_dir = direction

#Initializes the score
score = 0

def game_over():
    screen_font = pygame.font.SysFont("times new roman", 50)

    game_over_surface = screen_font.render("Final Score: " + str(score), True, red)
    
    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (x_window / 2, y_window / 4)

    #Draw text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    #Deactivate pygame
    pygame.quit()

    quit()

#Calls on the position generator once
print(obst_pos_gen()[0])

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
        #Increases snake speed whenever a fruit is consumed
        snake_speed += 2
        score += 10
    else:
        snake_body.pop()

    #Respawn fruit in a different position
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (x_window // 10)) * 10, random.randrange(1, (y_window // 10)) * 10]

    fruit_spawn = True
    game_window.fill(dark_blue)

    for pos in snake_body:
        snake_rect = pygame.draw.rect(game_window, orange, pygame.Rect(
          pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_pos[0], fruit_pos[1], 10, 10))
    
    obst1 = pygame.draw.rect(game_window, red, pygame.Rect(obst_pos_gen()[0], obst_pos_gen()[1], random.randrange(1, 25), random.randrange(1, 75)))
    #obst2 = pygame.draw.rect(game_window, red, pygame.Rect(obst_pos_gen()[0], obst_pos_gen()[1], random.randrange(1, 25), random.randrange(1, 75)))

    pygame.display.flip()
    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > x_window-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > y_window-10:
        game_over()
    if snake_rect.colliderect(obst1): 
        game_over()

    #Refreshing the game screen
    pygame.display.update()

    #Sets the frames per second
    fps.tick(snake_speed)

