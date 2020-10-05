import pygame
from pygame.draw import *
from random import randint

pygame.init()
name = input('Ваше имя: ')

class Balls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        type = str(randint(1, 3))
        self.image = pygame.image.load(type + '.png')
        self.image.set_colorkey((255, 255, 255))
        self.r = (randint(40, 100))
        self.image = pygame.transform.scale(self.image, (self.r, self.r))
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 1100)
        self.rect.y = randint(100, 600)
        self.vx = randint(-2, 2)
        self.vy = randint(-2, 2)
        self.time = randint(120, 240)
        if type == 1 or type == 3:
            self.count = self.vx ** 2 + self.vy ** 2
        else:
            self.count = self.vx ** 2 * 2 + self.vy ** 2 * 2

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.x < 0 or self.rect.x > 1201 - self.r:
            self.vx = - self.vx
        if self.rect.y < 0 or self.rect.y > 701 - self.r:
            self.vy = - self.vy
        if randint(1, self.time) == 1:
            self.kill()

    def hit(self):
        return self.count

    def click(self, s):
        x = s[0]
        y = s[1]
        if (x - self.rect.x - self.r / 2) ** 2 + (y - self.rect.y - self.r / 2) ** 2 < self.r ** 2 / 4:
            return True
        else:
            return False


FPS = 60
screen = pygame.display.set_mode((1200, 700))
balls1 = pygame.sprite.Group()
clock = pygame.time.Clock()

ball = Balls()
balls1.add(ball)
balls1.update()
pygame.display.flip()
finished = False
count = 0

while not finished:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    f1 = pygame.font.Font(None, 72)
    text1 = f1.render('Score:  ' + str(count), 1, (255, 0, 0))
    screen.blit(text1, (10, 50))
    balls1.update()
    balls1.draw(screen)
    pygame.display.flip()
    if randint(0, 30) == 1:
        ball = Balls()
        balls1.add(ball)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in balls1:
                if i.click(event.pos):
                    count += i.hit()
                    i.kill()
fk = []
try:
    f = open('score.txt')
    for line in f:
        fk.append(line)
    f.close()
    f = open('score.txt', 'w')
    fk.append(name + ' - ' + str(count) + '\n')
    for i in fk:
        f.write(i)
    f.close()
except:
    f = open('score.txt', 'w')
    for i in fk:
        f.write(i)
    f.write(name + ' - ' + str(count) + '\n')
    f.close()
pygame.quit()