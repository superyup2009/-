import pygame, sys, random
from pygame.locals import *

def ready1():
    game_ready_Font1 = pygame.font.SysFont('Sans', 100, 1, 1)
    game_ready_Message = 'Ready'
    screen.blit(bgimage, (0, 0))
    screen.blit(image_kirby, r1)
    screen.blit(image_monster, r2)
    screen.blit(game_ready_Font1.render(game_ready_Message, True, (0, 0, 0)), (120,180))
    pygame.display.update()
    pygame.time.delay(1500)

def ready2():
    game_ready_Font2 = pygame.font.SysFont('Sans', 100, 1, 1)
    game_ready_Message2 = '   go'
    screen.blit(bgimage, (0, 0))
    screen.blit(image_kirby, r1)
    screen.blit(image_monster, r2)
    screen.blit(game_ready_Font2.render(game_ready_Message2, True, (0, 0, 0)), (120, 180))
    pygame.display.update()
    pygame.time.delay(1500)

def loading():
    screen = pygame.display.set_mode((500, 600))
    game_start_image = pygame.image.load('game_start.jpg')
    game_start_image = pygame.transform.scale(game_start_image, (500, 600))

    game_loading_Fonat = pygame.font.SysFont('Sans', 30, 1, 1)
    game_loading_Message = 'Press a space key to start'

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return 0
        screen.blit(game_start_image, (0, 0))
        screen.blit(game_loading_Fonat.render(game_loading_Message, True, (0, 0, 0)), (25, 0))
        pygame.display.update()

def gameover():
    screen = pygame.display.set_mode((500, 600))
    gameoverImage = pygame.image.load('game_over.jpg')
    gameoverImage = pygame.transform.scale(gameoverImage, (500, 600))
    gameoverfont = pygame.font.SysFont('Sans', 30, 1, 1)
    gameovermessage = 'Press the space key to restart'
    scoreFont = pygame.font.SysFont('Sans', 25, 1, 1)
    scoremessage = 'Your best score: ' + str(second) + 'seconds'

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return loading()
            bgMusic.stop()
            screen.blit(gameoverImage, (0, 0))
            screen.blit(gameoverfont.render(gameovermessage, True, (255, 255, 255)), (25, 0))
            screen.blit(scoreFont.render(scoremessage, True, (0, 0, 0)), (25, 80))
            pygame.display.update()

clock = pygame.time.Clock()
pygame.init()

loading()

width = 500
height = 600
screen = pygame.display.set_mode((width, height))

r1 = pygame.Rect(0, 0, 80, 80)
r2 = pygame.Rect(width-80, height-80, 80, 80)

image_kirby = pygame.image.load('kirby.png')
image_kirby = pygame.transform.scale(image_kirby, (r1.w, r1.h))
image_monster = pygame.image.load('monster.png')
image_monster = pygame.transform.scale(image_monster, (r2.w, r2.h))
bgimage = pygame.image.load('bgimage.jpg')
bgimage = pygame.transform.scale(bgimage, (500, 600))
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()
pygame.mixer.init(22050, -16, 2, 512)
bgMusic = pygame.mixer.music
bgMusic.load('bgm.mp3')
bgMusic.play(-1)
bgMusic.set_volume(0.3)
speed = [7, 2]
crash_sound = pygame.mixer.Sound('crash.wav')
crash_sound.set_volume(0.2)
timeFont1 = pygame.font.SysFont('Sans', 40, 1, 1)
timeFont2 = pygame.font.SysFont('Sans', 40, 1, 1)
second = -1
start_time = 0
delay = 0

while True:
    clock.tick(300)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    r2.x += speed[0]
    r2.y += speed[1]

    KeyInput = pygame.key.get_pressed()
    if KeyInput[K_LEFT] and r1.left >= 0:
        r1.left -= 2
    elif KeyInput[K_RIGHT] and r1.right <= width:
        r1.right += 2
    elif KeyInput[K_UP] and r1.top >= 0:
        r1.top -= 2
    elif KeyInput[K_DOWN] and r1.bottom <= height:
        r1.bottom += 2

    if r2.left < 0 or r2.right > width:
        if speed[0] > 0:
            speed[0] = -random.uniform(1, 3)
        elif speed[0] < 0:
            speed[0] = random.uniform(1, 3)

    if r2.top < 0 or r2.bottom > height:
        if speed[1] > 0:
            speed[1] = -random.uniform(1, 3)
        elif speed[1] < 0:
            speed[1] = random.uniform(1, 3)
    if r1.colliderect(r2):
        crash_sound.play()
        r1.x = random.randint(0, width-r1.w)
        r1.y = random.randint(0, height-r1.h)
        r1.width -= 2
        r1.height -= 2
        image_kirby = pygame.image.load('kirby.png')
        image_kirby = pygame.transform.scale(image_kirby, (r1.w, r1.h))

    #screen.fill((0, 0, 0))
    screen.blit(bgimage, (0, 0))
    #pygame.draw.rect(screen, (0, 0, 255), r1)
    screen.blit(image_kirby, r1)
    #pygame.draw.ellipse(screen, (0, 255, 0), r2)
    screen.blit(image_monster, r2)

    timeMessage = 'Time: '
    time_Font1 = timeFont1.render(timeMessage, True, (0, 0, 0))
    screen.blit(time_Font1, (0,0))
    timeMessage2 = str(second) + 's'
    time_Font2 = timeFont2.render(timeMessage2, True, (0, 0, 0))
    screen.blit(time_Font2, (100, 0))
    time_since_enter = pygame.time.get_ticks() - start_time
    if time_since_enter > 1000:
        start_time = pygame.time.get_ticks()
        second += 1
    if delay == 0:
        ready1()
        ready2()
        delay = 1

    if r1.width < 50:
        gameover()
        delay = 0
        r1.width = 80
        r1.height = 80
        r1.x = 0
        r1.y = 0
        r2.x = width - 80
        r2.y = height - 80
        image_kirby = pygame.image.load('kirby.png')
        image_kirby = pygame.transform.scale(image_kirby, (r1.w, r1.h))
        second = -1
        screen = pygame.display.set_mode((width, height))
        screen.blit(bgimage, (0, 0))

        bgMusic = pygame.mixer.music
        bgMusic.load('bgm.mp3')
        bgMusic.play(-1)
        bgMusic.set_volume(0.3)
        pygame.display.update()
    pygame.display.update()
