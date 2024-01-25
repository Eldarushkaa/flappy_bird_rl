import numpy as np
import pygame as pg
import random as r

Z = 2


def sigmoid(x):
    return np.array([[max(0, int(a))] for a in x])
    #return 1 / (1 + np.exp(-x))


def massp(bp):
    global bh1
    global bh2
    bp = bird0.mp(bp)
    bp = bird1.mp(bp)
    bp = bird2.mp(bp)
    bp = bird3.mp(bp)
    bp = bird4.mp(bp)
    bp = bird5.mp(bp)
    bp = bird6.mp(bp)
    bp = bird7.mp(bp)
    bp = bird8.mp(bp)
    bp = bird9.mp(bp)
    return bp


def massgravity():
    bird0.speed -= 1
    bird1.speed -= 1
    bird2.speed -= 1
    bird3.speed -= 1
    bird4.speed -= 1
    bird5.speed -= 1
    bird6.speed -= 1
    bird7.speed -= 1
    bird8.speed -= 1
    bird9.speed -= 1


def masschek():
    bird0.check()
    bird1.check()
    bird2.check()
    bird3.check()
    bird4.check()
    bird5.check()
    bird6.check()
    bird7.check()
    bird8.check()
    bird9.check()

    global running
    if not (bird0.life or bird1.life or bird2.life or bird3.life or bird4.life or
       bird5.life or bird6.life or bird7.life or bird8.life or bird9.life):
        running = False


def massjump():
    bird0.jump()
    bird1.jump()
    bird2.jump()
    bird3.jump()
    bird4.jump()
    bird5.jump()
    bird6.jump()
    bird7.jump()
    bird8.jump()
    bird9.jump()


def koef(x):
    return min((x / 200) ** 4, 100)


class Bird(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill((255, 220, 10))
        self.rect = self.image.get_rect()
        self.rect.center = (width / 4, height / 2)
        self.rect.centery += 1 * 20
        self.speed = r.random() * 20
        k1, k2 = np.random.random((Z, 2)) * 4, np.random.random((1, Z)) * 4
        self.h1 = np.random.random((Z, 2)) * 2 - 1
        self.h2 = np.random.random((1, Z)) * 2 - 1
        self.h1 = (self.h1 + bh1 * (koef(bp) * k1)) / (1 + k1 * koef(bp))
        self.h2 = (self.h2 + bh2 * (koef(bp) * k2)) / (1 + k2 * koef(bp))

    def update(self):
        self.rect.y -= self.speed
        if self.life:
            self.points += 1

    def mp(self, bp):
        global bh1, bh2
        if self.points > bp:
            bp = self.points
            bh1, bh2 = self.h1, self.h2
        return bp

    def jump(self):
        self.n6 = sigmoid(self.h1 @ [[self.rect.bottom - window.rect.bottom], [window.rect.right]]).transpose()
        if sum((self.n6 * self.h2)[0]) > 0:
            self.speed = 15

    def check(self):
        if self.rect.bottom >= height or self.rect.top <= 0 or \
                ((self.rect.right >= wall.rect.left and self.rect.left <= wall.rect.right) and
                 (self.rect.top <= window.rect.top or self.rect.bottom >= window.rect.bottom)):
            self.life = False
            all_sprites.remove(self)

    h1 = np.zeros((Z, 2))
    h2 = np.zeros((1, Z))
    n6 = np.zeros((1, Z))

    life = True

    speed = 0

    points = 0


class Wall(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((70, 800))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (width + 35, height / 2)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 1:
            self.rect.left = width


class Window(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((70, 200))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (width + 35, 550)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 1:
            self.rect.left = width
            self.rect.top = r.randint(50, 550)
            if abs(self.rect.top - window2.rect.top) > 400:
                self.rect.top = (self.rect.top + 300) / 2


# colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 220, 10)
green = (20, 200, 0)
blue = (3, 229, 254)

# consts
width = 550
height = 800
fps = 30

bh1 = np.zeros((Z, 2))
bh2 = np.zeros((1, Z))

n = 500000

bp = 0
points = 0
bscore = 0

critical_score = 10000

for i in range(n):

    pg.init()
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    wall = Wall()
    wall2 = Wall()
    all_sprites.add(wall)
    all_sprites.add(wall2)
    window = Window()
    window2 = Window()
    all_sprites.add(window)
    all_sprites.add(window2)
    bird0 = Bird()
    bird1 = Bird()
    bird2 = Bird()
    bird3 = Bird()
    bird4 = Bird()
    bird5 = Bird()
    bird6 = Bird()
    bird7 = Bird()
    bird8 = Bird()
    bird9 = Bird()
    bird0.image.fill((255, 210, 10))
    bird1.image.fill((255, 200, 20))
    bird2.image.fill((255, 190, 30))
    bird3.image.fill((255, 180, 40))
    bird4.image.fill((255, 170, 50))
    bird5.image.fill((255, 160, 60))
    bird6.image.fill((255, 150, 70))
    bird7.image.fill((int(r.random() * 255), int(r.random() * 255), int(r.random() * 255)))
    bird8.image.fill((int(r.random() * 255), int(r.random() * 255), int(r.random() * 255)))
    bird9.image.fill((255, 120, 100))
    all_sprites.add(bird0)
    all_sprites.add(bird1)
    all_sprites.add(bird2)
    all_sprites.add(bird3)
    all_sprites.add(bird4)
    all_sprites.add(bird5)
    all_sprites.add(bird6)
    all_sprites.add(bird7)
    all_sprites.add(bird8)
    all_sprites.add(bird9)

    score = 0
    wall2.rect.centerx += width / 2 + 35
    window2.rect.centerx += width / 2 + 35

    running = True
    while running:
        if score > critical_score:
            clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        massjump()
        massgravity()

        masschek()

        if window.rect.right - 3 < width / 4 - 15 < window.rect.right + 3:
            score += 1
            wall, wall2 = wall2, wall
            window, window2 = window2, window

        all_sprites.update()
        screen.fill(blue)
        all_sprites.draw(screen)
        font = pg.font.SysFont('couriernew', 20)
        text = font.render('Generation = ' + str(i + 1), True, 'Black')
        screen.blit(text, (50, 30))
        font = pg.font.SysFont('couriernew', 20)
        text = font.render('Score = ' + str(score), True, 'Black')
        screen.blit(text, (50, 50))
        pg.display.flip()

    bp = massp(bp)
    print(str(i + 1) + '. ' + str(score) + '(' + str(bscore) + ')')
    if score > bscore:
        bscore = score
