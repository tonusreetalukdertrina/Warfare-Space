import pygame
from pygame import mixer

import random
import math

#Initialize the game
pygame.init()

#Screen
screen = pygame.display.set_mode((1000, 600))

#Title and Icon
pygame.display.set_caption("Warfare Space")
icon = pygame.image.load('006-fighter-jet.png')
pygame.display.set_icon(icon)

#Music
mixer.music.load('gamemusic.wav')
mixer.music.play(-1)

#Player
playerImg = pygame.image.load('003-ufo.png')
playerX = 470
playerY = 480
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('009-ufo-1.png'))
    enemyX.append(random.randint(0, 835))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.9)
    enemyY_change.append(30)

#Avatar
avatarImg = []
avatarX = []
avatarY = []
avatarX_change = []
avatarY_change = []
num_of_avatars = 3

for i in range(num_of_avatars):
    avatarImg.append(pygame.image.load('004-shredder.png'))
    avatarX.append(random.randint(0, 835))
    avatarY.append(random.randint(50, 150))
    avatarX_change.append(0.9)
    avatarY_change.append(30)

#Bullet
bulletImg = pygame.image.load('001-fire.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready"

#Enemy Bullet
ballImg = pygame.image.load('007-fireball.png')
ballX = random.randint(100, 900)
ballY = 0
ballX_change = 0
ballY_change = 3
ball_state = "ready"

#Background
background = pygame.image.load('Random-1.png')

score_value = 0
font = pygame.font.Font('Bebas-Regular.ttf', 32)
textX = 10
textY = 50

goal_value = random.randint(600, 1000)
goal_font = pygame.font.Font('Bebas-Regular.ttf', 32)
goal_textX = 10
goal_textY = 10

num_of_collision2 = 0
num_of_collision3 = 0

final1_font1 = pygame.font.Font('freesansbold.ttf', 32)
final1_font2 = pygame.font.Font('freesansbold.ttf', 32)
final1_textX1 = 333
final1_textY1 = 240
final1_textX2 = 243
final1_textY2 = 290

final2_font1 = pygame.font.Font('freesansbold.ttf', 32)
final2_font2 = pygame.font.Font('freesansbold.ttf', 32)
final2_textX1 = 333
final2_textY1 = 240
final2_textX2 = 243
final2_textY2 = 290

def show_final1(x1, y1, x2, y2):
    final1_1 = final1_font1.render("GAME OVER", True, (255, 0, 255))
    final1_2 = final1_font2.render("You couldn't reach to your goal", True, (255, 0, 255))
    screen.blit(final1_1, (x1, y1))
    screen.blit(final1_2, (x2, y2))

def show_final2(x1, y1, x2, y2):
    final2_1 = final2_font1.render("SUPERB!!!", True, (255, 0, 255))
    final2_2 = final2_font2.render("You could reach to your goal", True, (255, 0, 255))
    screen.blit(final2_1, (x1, y1))
    screen.blit(final2_2, (x2, y2))


def show_goal(x, y):
    goal = goal_font.render("Goal: " + str(goal_value), True, (255, 0, 255))
    screen.blit(goal, (x, y))

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 0, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x,y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x,y))

def avatar(x, y, i):
    screen.blit(avatarImg[i], (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def fire_ball(x, y):
    global ball_state
    ball_state = "fire"
    screen.blit(ballImg, (x, y))

def isCollision1(enemyX, enemyY, bulletX, bulletY):
    distance1 = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance1 < 27:
        return True
    else:
        return False

def isCollision2(avatarX, avatarY, bulletX, bulletY):
    distance2 = math.sqrt((math.pow(avatarX-bulletX, 2)) + (math.pow(avatarY-bulletY, 2)))
    if distance2 < 27:
        return True
    else:
        return False

def isCollision3(playerX, playerY, ballX, ballY):
    distance3 = math.sqrt((math.pow(playerX-ballX, 2)) + (math.pow(playerY-ballY, 2)))
    if distance3 < 27:
        return True
    else:
        return False

n = 1
c = 0
#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_music = mixer.Sound('mixkit-laser-gun-shot-3110.wav')
                    bullet_music.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if ball_state == "ready" and n > 1 and c==0:
            fire_ball(ballX, ballY)


    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    playerX += playerX_change
    if playerX >= 936:
        playerX = 936
    if playerX <= 0:
        playerX = 1
    for i in range(num_of_enemies):
        if (num_of_collision2 == 3 or num_of_collision3 == 3):
            c += 1
            playerX = 1001
            playerY = 601
            if (score_value < goal_value):
                show_final1(final1_textX1, final1_textY1, final1_textX2, final1_textY2)
                break
            if (score_value >= goal_value):
                show_final2(final2_textX1, final2_textY1, final2_textX2, final2_textY2)
                break

        if enemyY[i] >= 400:
            for j in range(num_of_enemies):
                enemyX[j] = random.randint(0, 835)
                enemyY[j]= random.randint(50, 150)
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.9
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 935:
            enemyX_change[i] = -0.9
            enemyY[i] += enemyY_change[i]

        collision1 = isCollision1(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision1:
            bulletY = 480
            bullet_state = "ready"
            score_value += 6
            enemyX[i] = random.randint(0, 835)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    for i in range(num_of_avatars):
        if (num_of_collision2 == 3 or num_of_collision3 == 3):
            c += 1
            playerX = 1001
            playerY = 601
            if (score_value < goal_value):
                show_final1(final1_textX1, final1_textY1, final1_textX2, final1_textY2)
                break
            if (score_value >= goal_value):
                show_final2(final2_textX1, final2_textY1, final2_textX2, final2_textY2)
                break
        if avatarY[i] >= 400:
            for j in range(num_of_avatars):
                avatarX[j] = random.randint(0, 835)
                avatarY[j] = random.randint(50, 150)
        avatarX[i] += avatarX_change[i]
        if avatarX[i] <= 0:
            avatarX_change[i] = 0.9
            avatarY[i] += avatarY_change[i]
        if avatarX[i] >= 935:
            avatarX_change[i] = -0.9
            avatarY[i] += avatarY_change[i]

        collision2 = isCollision2(avatarX[i], avatarY[i], bulletX, bulletY)
        if collision2:
            num_of_collision2 += 1
            bulletY = 480
            bullet_state = "ready"
            score_value -= 6
            avatarX[i] = random.randint(0, 835)
            avatarY[i] = random.randint(50, 150)
        avatar(avatarX[i], avatarY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if ballY >= 600:
        ballX = random.randint(300, 900)
        ballY = 0
        ball_state = "ready"
    if ball_state == "fire" and c==0:
        fire_ball(ballX, ballY)
        ballY += ballY_change

    collision3 = isCollision3(playerX, playerY, ballX, ballY)
    if collision3:
        fire_music = mixer.Sound('mixkit-falling-hit-757.wav')
        fire_music.play()
        num_of_collision3 += 1
        ballY = random.randint(300, 900)
        bullet_state = "ready"
        score_value -= 3



    player(playerX, playerY)
    show_score(textX, textY)
    show_goal(goal_textX, goal_textY)
    n += 1
    pygame.display.update()
