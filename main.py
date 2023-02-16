import pygame
import random
import math

# initialize the pygame

pygame.init()
# background
background = pygame.image.load("5471985.jpg")
# creating the Display

screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("    Space Invader")

# player

playerimg = pygame.image.load('playership.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.2)
    enemyY_change.append(40)

# Bullet

bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # keystrokes

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # player boundary
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # enemy boundary
for i in range(num_of_enemies):
    enemyX[i] += enemyX_change[i]
    if enemyX[i] <= 0:
        enemyX_change[i] = 0.3
        enemyY[i] += enemyY_change[i]
    elif enemyX[i] >= 736:
        enemyX_change[i] = -0.3
        enemyY[i] += enemyY_change[i]

    # collision
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX[i] = random.randint(0, 735)
        enemyY[i] = random.randint(50, 150)

    enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)


    pygame.display.update()
