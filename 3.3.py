import pygame
from pygame.draw import *


def gus(dx, dy, k, screen, z):
    s1 = []
    w = (255, 255, 255)
    s = pygame.Surface((512, 720), pygame.SRCALPHA)
    for i in range(30):
        s1.append((i + 192, 440 + i ** 2 / 10))
    for i in range(40):
        s1.append((170 - i, 512 - i ** 1.5 / 5))
    x, y = s1[-1]
    for i in range(100):
        s1.append((x - i, y - i ** 1.8 / 50))
    x, y = s1[-1]
    for i in range(160):
        s1.append((x + i, y + i ** 0.79))
    polygon(s, w, [(i + 50, j - 10) for i, j in s1])
    polygon(s, (0, 0, 0), [(i + 50, j - 10) for i, j in s1], 3)
    circle(s, w, (232, 500), 35)
    polygon(s, w, [(i + 10, j + 10) for i, j in s1])
    polygon(s, (0, 0, 0), [(i + 10, j + 10) for i, j in s1], 3)

    s1 = []
    for i in range(25):
        s1.append((i + 370, 507 - i ** 0.5 / 5))
    x, y = s1[-1]
    for i in range(15):
        s1.append((x + i, y + i ** 1.6 / 25))
    x, y = s1[-1]
    for i in range(5):
        s1.append((x - i, y + i ** 0.5 * 6))
    polygon(s, (255, 190, 0), s1)
    polygon(s, (0, 0, 0), s1, 3)

    s1 = []
    y += 3
    for i in range(5):
        s1.append((x + i, y + i ** 0.5 * 3))
    x, y = s1[-1]
    for i in range(25):
        s1.append((x - i, y + i ** 0.5))
    x, y = s1[-1]
    for i in range(24):
        s1.append((x - i, y - i ** 0.7 * 1.3))

    polygon(s, (255, 190, 0), s1)
    polygon(s, (0, 0, 0), s1, 3)

    s1 = []
    for i in range(28):
        s1.append((i + 218, 550 + i ** 2 / 10))
    x, y = s1[-1]
    for i in range(40):
        s1.append((x - i, y - i ** 2 / 20))
    polygon(s, w, [(i + 40, j - 20) for i, j in s1])

    s1 = []
    for i in range(50):
        s1.append((i + 230, 610 + i ** 2 / 80))
    x, y = s1[-1]
    for i in range(50):
        s1.append((x - i, y - i ** 2 / 90))
    polygon(s, w, [(i + 40, j - 20) for i, j in s1])

    s1 = []
    for i in range(30):
        s1.append((i + 280, 640 - i ** 0.5 * 3))
    polygon(s, (255, 190, 71), [(i + 40, j - 20) for i, j in s1])
    polygon(s, (0, 0, 0), [(i + 40, j - 20) for i, j in s1], 1)

    s1 = []
    for i in range(40):
        s1.append((i + 280, 640 - i ** 0.5 * 1))
    polygon(s, (255, 190, 71), [(i + 40, j - 20) for i, j in s1])
    polygon(s, (0, 0, 0), [(i + 40, j - 20) for i, j in s1], 1)

    s1 = []
    for i in range(30):
        s1.append((i + 280, 640 + i ** 0.5 * 3))
    polygon(s, (255, 190, 71), [(i + 40, j - 20) for i, j in s1])
    polygon(s, (0, 0, 0), [(i + 40, j - 20) for i, j in s1], 1)

    s1 = []
    for i in range(13):
        s1.append((280 - i, 640 + i ** 2 / 4))
    polygon(s, (255, 190, 71), [(i + 40, j - 20) for i, j in s1])
    polygon(s, (0, 0, 0), [(i + 40, j - 20) for i, j in s1], 1)

    s1 = []
    for i in range(70):
        s1.append((138 - i, 570 - i ** 2 / 200))
    x, y = s1[-1]
    for i in range(5):
        s1.append((x - i, y - i ** 2 * 3))
    x, y = s1[-1]
    for i in range(70):
        s1.append((x + i, y + i ** 0.8 * 2))
    polygon(s, w, [(i + 40, j - 20) for i, j in s1])

    s1 = []
    for i in range(28):
        s1.append((i + 218, 550 + i ** 2 / 10))
    x, y = s1[-1]
    for i in range(40):
        s1.append((x - i, y - i ** 2 / 20))
    polygon(s, w, s1)

    s1 = []
    for i in range(50):
        s1.append((i + 230, 610 + i ** 2 / 80))
    x, y = s1[-1]
    for i in range(50):
        s1.append((x - i, y - i ** 2 / 90))
    polygon(s, w, s1)

    s1 = []
    for i in range(30):
        s1.append((i + 280, 640 - i ** 0.5 * 3))
    polygon(s, (255, 190, 71), s1)
    polygon(s, (0, 0, 0), s1, 1)

    s1 = []
    for i in range(40):
        s1.append((i + 280, 640 - i ** 0.5 * 1))
    polygon(s, (255, 190, 71), s1)
    polygon(s, (0, 0, 0), s1, 1)

    s1 = []
    for i in range(30):
        s1.append((i + 280, 640 + i ** 0.5 * 3))
    polygon(s, (255, 190, 71), s1)
    polygon(s, (0, 0, 0), s1, 1)

    s1 = []
    for i in range(13):
        s1.append((280 - i, 640 + i ** 2 / 4))
    polygon(s, (255, 190, 71), s1)
    polygon(s, (0, 0, 0), s1, 1)

    ellipse(s, (255, 255, 255), (326, 500, 50, 30))
    ellipse(s, (0, 0, 0), (350, 509, 10, 5))
    ellipse(s, w, (280, 516, 70, 25))
    ellipse(s, w, (167, 509, 150, 65))

    if z == 0:
        screen.blit(pygame.transform.scale(s, (int(512 / k), int(720 / k))), (dx, dy))
    else:
        s = pygame.transform.flip(s, True, False)
        screen.blit(pygame.transform.scale(s, (int(512 / k), int(720 / k))), (dx, dy))


def riba(dx, dy, k, screen, z):
    w = (255, 255, 255)
    s = pygame.Surface((512, 720), pygame.SRCALPHA)
    s1 = []
    for i in range(5):
        s1.append((430 - i, 650 - i ** 2 * 1.5))
    x, y = s1[-1]
    for i in range(46):
        s1.append((x - i, y - i ** 0.5 / 1.5))
    x, y = s1[-1]
    for i in range(24):
        s1.append((x + i, y + i ** 1.8 / 20))
    polygon(s, (120, 45, 45), s1)
    polygon(s, (0, 0, 0), s1, 1)

    s1 = []
    for i in range(30):
        s1.append((360 - i, 650 - i ** 2 / 40))
    x, y = s1[-1]
    for i in range(5):
        s1.append((x + i, y + i ** 2.5))
    polygon(s, (120, 45, 45), s1)
    polygon(s, (0, 0, 0), s1, 1)

    s1 = []
    for i in range(13):
        s1.append((380 - i, 660 + i ** 0.5 * 4))
    x, y = s1[-1]
    for i in range(20):
        s1.append((x + i, y + i ** 0.5))
    x, y = s1[-1]
    for i in range(5):
        s1.append((x + i, y - i ** 2.5))
    polygon(s, (120, 45, 45), s1)
    polygon(s, (0, 0, 0), s1, 1)

    s1 = []
    for i in range(13):
        s1.append((430 - i, 664 + i ** 0.5 * 4))
    x, y = s1[-1]
    for i in range(20):
        s1.append((x + i, y + i ** 0.6))
    x, y = s1[-1]
    for i in range(5):
        s1.append((x + i, y - i ** 2))
    polygon(s, (120, 45, 45), s1)
    polygon(s, (0, 0, 0), s1, 1)

    s1 = []
    for i in range(50):
        s1.append((360 + i, 650 - i ** 0.5 * 2))
    x, y = s1[-1]
    for i in range(50):
        s1.append((x + i, y + i ** 2 / 100))
    x, y = s1[-1]
    for i in range(50):
        s1.append((x - i, y + i ** 0.5 * 2))
    x, y = s1[-1]
    for i in range(50):
        s1.append((x - i, y - i ** 2 / 100))
    polygon(s, (71, 136, 141), s1)
    polygon(s, (0, 0, 0), s1, 1)

    circle(s, (0, 0, 255), (437, 653), 7)
    circle(s, (0, 0, 0), (440, 653), 3)
    line(s, w, (432, 650), (438, 652), 1)

    if z == 0:
        screen.blit(pygame.transform.scale(s, (int(512 / k), int(720 / k))), (dx, dy))
    else:
        s = pygame.transform.flip(s, True, False)
        screen.blit(pygame.transform.scale(s, (int(512 / k), int(720 / k))), (dx, dy))


def chaika(dx, dy, k, screen, a):
    w = (255, 255, 255)
    s = pygame.Surface((512, 720), pygame.SRCALPHA)
    arc(s, w, (85, 230, 70, 26), 0, 3.14, 3)
    arc(s, w, (155, 230, 70, 26), 0, 3.14, 3)
    s = pygame.transform.rotate(s, a)
    screen.blit(pygame.transform.scale(s, (int(512 / k), int(720 / k))), (dx, dy))


pygame.init()

FPS = 30
h = pygame.display.set_mode((512, 720))

w = (255, 255, 255)
rect(h, (0, 102, 128), (0, 0, 512, 720))
rect(h, (255, 153, 83), (0, 290, 512, 80))
rect(h, (222, 135, 170), (0, 190, 512, 100))
rect(h, (205, 135, 222), (0, 130, 512, 60))
rect(h, (141, 95, 211), (0, 80, 512, 50))
rect(h, (33, 33, 120), (0, 0, 512, 80))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

gus(50, 250, 3, h, 0)
gus(20, 250, 1.5, h, 0)
gus(320, 290, 3, h, 1)
riba(50, 250, 3, h, 0)
riba(20, 250, 1.5, h, 0)
riba(320, 290, 3, h, 1)
chaika(-50, 0, 1, h, -20)
chaika(100, 50, 2, h, 0)
chaika(80, 55, 2, h, 0)
chaika(200, 60, 2, h, 0)
chaika(300, 45, 2, h, 0)
chaika(400, 50, 2, h, 0)
chaika(140, 66, 2, h, 0)
chaika(150, -90, 1, h, 0)
chaika(-50, -260, 1, h, 30)
chaika(200, 0, 2, h, 0)
chaika(300, 5, 2, h, 0)
chaika(400, 0, 2, h, 0)
chaika(140, 16, 2, h, 0)

while not finished:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()