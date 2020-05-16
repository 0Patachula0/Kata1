import pygame

# Variables
screen_width = 1280
screen_height = 960

# Colores
back_color = (100, 100, 100)
light_gray = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

def mover_rectangulo():
    global speed
    if rectangulo.top + 50 > screen_height:
        rectangulo.top += speed

def mover_bola():
    bola.top

rectangulo = pygame.rect(10, 10, 50, 50)
bola = pygame.Rect(50)

speed = 0
speed_bola_x = 3
speed_bola_y = 3

while True:
    screen.fill(back_color)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = -3
            elif event.key == pygame.K_DOWN:
                speed = 3
        elif event.type == pygame.KEYUP:
            speed = 0
    
    pygame.draw.Rect(screen, back_color, rectangulo)
    pygame.dray.ellipse(screen, back_color, bola)

    pygame.display.flip()
    clock.tick(60)