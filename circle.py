import pygame
import random
import time
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
timer = 0
print('.')
print('.')
print('.')
print("Привет. Меня зовут шарик, моя задача продержаться как можно больше времни, что бы красный шаринган меня не коснулся.")
print("Ты можешь управлять мной с помоью кнопок: вниз, вверх, влево, вправо. Твоя задача продержаться не меньше 30 секунд.")
print("Желаю удачи, если ты готов то нажми Enter.")
bukva=input()
pygame.init()

screen = pygame.display.set_mode([700,500])
pygame.display.set_caption('шарик')

game = False
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
x1_speed = 0
y1_speed = 0
x1_coord = 350
y1_coord = 250
x2_coord = 20
y2_coord = 20
x2_speed = random.randint(1,4)
y2_speed = random.randint(1,4)
x3_coord = 20
y3_coord = 20
x3_speed = random.randint(1,4)
y3_speed = random.randint(1,4)

radius1 = 30
radius2 = 15
radius3 = 15

time.sleep(3)
while not game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x1_speed = -5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x1_speed = 5
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y1_speed = -5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y1_speed = 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                x1_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                y1_speed = 0
    if x1_coord >= 670:
        x1_speed = 0
        x1_coord = 669

    elif x1_coord <= 30:
        x1_speed = 0
        x1_coord = 31

    elif y1_coord >= 470:
        y1_speed = 0
        y1_coord = 469

    elif y1_coord <= 30:
        y1_speed = 0
        y1_coord = 31

    timer = timer + 1

    if timer <1740:
        if x2_coord >= 684:
            x2_speed = random.randint(-5,-3)
        if x2_coord <= 16:
            x2_speed = random.randint(3,5)
        if y2_coord >= 484:
            y2_speed = random.randint(-5,-3)
        if y2_coord <= 16:
            y2_speed = random.randint(3,10)
        if -31 <= x1_coord - x2_coord <= 31 and -31 <= y1_coord - y2_coord <= 31:
            game = True

    if timer >= 1740:
        radius2 = 30
        if x2_coord >= 669:
            x2_speed = random.randint(-10,-5)
        if x2_coord <= 31:
            x2_speed = random.randint(5,10)
        if y2_coord >= 469:
            y2_speed = random.randint(-10,-5)
        if y2_coord <= 31:
            y2_speed = random.randint(5,10)
        if -59 <= x1_coord - x2_coord <= 59 and -59 <= y1_coord - y2_coord <= 59:
            game = True






    x1_coord = x1_coord + x1_speed
    y1_coord = y1_coord + y1_speed
    x2_coord = x2_coord + x2_speed
    y2_coord = y2_coord + y2_speed


    screen.fill(WHITE)
    pygame.draw.circle(screen,GREEN,[x1_coord,y1_coord],radius1)
    pygame.draw.circle(screen,RED,[x2_coord,y2_coord],radius2)

    if timer >= 3540:
        if x3_coord >= 684:
            x3_speed = random.randint(-10,-3)
        if x3_coord <= 16:
            x3_speed = random.randint(3,10)
        if y3_coord >= 484:
            y3_speed = random.randint(-10,-3)
        if y3_coord <= 16:
            y3_speed = random.randint(3,10)
        if -31 <= x1_coord - x3_coord <= 31 and -31 <= y1_coord - y3_coord <= 31:
            game = True
        x3_coord = x3_coord+x3_speed
        y3_coord = y3_coord+y3_speed
        pygame.draw.circle(screen,RED,[x3_coord,y3_coord],radius3)


    pygame.display.flip()
    clock.tick(60)




pygame.quit()
timer = timer//60
if timer < 60:
    timer_sec = timer

    if timer_sec < 30:
        print('Ты продержался', timer_sec ,'секунд, ты проиграл')
    if timer_sec >= 30:
        print('Ты продержался', timer_sec ,'секунд, поздравляю')
if timer >= 60:
    timer_min = timer//60
    timer_sec= timer%10
    print('Ты продержался', timer_min ,'минут', timer_sec ,'секунд')
    print("ты победил!!!")

print("Тебе понравилась игра? Напиши свои пожелания ...")
pozhelaniya = input()
