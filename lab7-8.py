from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        canv.delete(self.id)
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def hittest(self, obj):
        for i in range(100):
            if (obj.x - self.x - self.vx / 100 * i) ** 2 +\
                    (obj.y - self.y - self.vy / 100 * i) ** 2 < (obj.r + self.r) ** 2:
                return True
        return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.new_target()

    def new_target(self):
        r = self.r = rnd(2, 50)
        x = self.x = rnd(600, 788 - self.r)
        y = self.y = rnd(300, 588 - self.r)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self):
        canv.coords(self.id, -10, -10, -10, -10)

    def move(self):
        if self.live:
            self.x += self.vx
            self.y -= self.vy
            if self.x + self.r > 800:
                self.vx = -self.vx
            if self.x - self.r < 0:
                self.vx = -self.vx
            if self.y + self.r > 600:
                self.vy = -self.vy
            if self.y - self.r < 0:
                self.vy = -self.vy
            canv.delete(self.id)
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 10
balls = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    point = 0
    score = canv.create_text(30, 30, text=point, font='28')
    t1.live = 1
    while t1.live or balls or t2.live:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                point += 1
                canv.delete(score)
                score = canv.create_text(30, 30, text=point, font='28')
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                point += 1
                canv.delete(score)
                score = canv.create_text(30, 30, text=point, font='28')
            if t1.live == 0 and t2.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрел(a / ов)')
        canv.update()
        t2.move()
        t1.move()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()
