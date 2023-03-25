import pygame

#Pygame set up
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#Snake Head Position
posX = 0
posY = 0
orientation = 0 #0 = North, 1 = East, 2 = South, 3 = West

#Main Function
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP  and orientation != 2:
                orientation = 0
            elif event.key == pygame.K_RIGHT and orientation != 3:
                orientation = 1
            elif event.key == pygame.K_DOWN and orientation != 0:
                orientation = 2
            elif event.key == pygame.K_LEFT and orientation != 1:
                orientation = 3
    match orientation:
        case 0:
            posY += 1
        case 1:
            posX += 1
        case 2:
            posY -= 1
        case 3:
            posX -= 1
        case default:
            posY += 1
    print("Orientation: " + str(orientation) + " PostionX: " + str(posX) + " PositionY: " + str(posY))
    screen.fill("Purple")

    #render game

    pygame.display.flip()
    clock.tick(60)

pygame.quit()