import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (120, 120, 120), (0, 0, 400, 400))
circle(screen, (255, 120, 0), (200, 200), 200)
circle(screen, (255, 0, 0), (120, 140), 50)
circle(screen, (255, 0, 0), (280, 140), 50)
circle(screen, (0, 0, 0), (120, 140), 20)
circle(screen, (0, 0, 0), (280, 140), 20)
rect(screen, (0, 0, 0), (100, 300, 200, 20))
polygon(screen, (0, 0, 0), ((50, 50), (30, 30), (160, 80), (180, 100)))
polygon(screen, (0, 0, 0), ((350, 50), (370, 30), (240, 80), (220, 100)))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()