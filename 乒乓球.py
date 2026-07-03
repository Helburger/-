from pygame import *
from pygame._sdl2 import Window
window = display.set_mode((500,500))
bg = (0,0,0)
window.fill(bg)
display.set_caption("乒乓球 = Ping Poong")
win = Window.from_display_module()
win.maximize()
isRunning = True
clock = time.Clock()
fps = 60
class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Playersprite(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            if keys_pressed[K_LSHIFT]:
                self.speed = 10
            else:
                self.speed = 5
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
            if keys_pressed[K_LSHIFT]:
                self.speed = 10
            else:
                self.speed = 5
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            if keys_pressed[K_RSHIFT]:
                self.speed = 10
            else:
                self.speed = 5
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
            if keys_pressed[K_RSHIFT]:
                self.speed = 10
            else:
                self.speed = 5
font.init()
scorepad1 = 0
spcreat2 = 0
scorefont = font.SysFont("Verdana", 25)
big_font = font.SysFont("Arial", 70)
Paddel1 = Playersprite('paddel_1.png', 450, 200, 10, 100, 5)
Paddel2 = Playersprite('paddel_2.png', 30, 200, 10, 100, 5)
ball = GameSprite("ball.png", 250, 450, 25, 25, 15)
Win1 = big_font.render('Player 1 Win', True, (255,255,255))
Win2 = big_font.render('Player 2 Win', True, (255,255,255))
speed_x = 7
speed_y = 8

def ballreset():
    global speed_x, speed_y
    ball.rect.x = 500/2
    ball.rect.y = 500/2
    speed_x *= -1
while isRunning:
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    score_text = scorefont.render(f"{scorepad1}:{spcreat2}", True, (255,255,255))
    if ball.rect.y > 500-35 or ball.rect.y < -10:
        speed_y *= -1
    if ball.rect.x > 500 or ball.rect.x < -40:
        speed_x *= -1
    for e in event.get():
        if e.type == QUIT:
            isRunning = False
    if ball.rect.x > 500-30:
        scorepad1 += 1
        ballreset()
    if ball.rect.x < -10:
        spcreat2 += 1
        ballreset()
    print(scorepad1)
    print(spcreat2)
    if sprite.collide_rect(Paddel1, ball) or sprite.collide_rect(Paddel2, ball):
        speed_x *= -1
    if sprite.collide_rect(Paddel1, ball) or sprite.collide_rect(Paddel2, ball):
        speed_y *= -1
    Paddel2.update1()
    Paddel1.update2() 
    window.fill(bg)
    window.blit(score_text, (240,20))
    Paddel1.reset()
    Paddel2.reset()
    ball.reset()

    if scorepad1 >= 5:
        window.blit(Win1, (50,215))
        isRunning = False
    if spcreat2 >= 5:
        window.blit(Win2, (50,215))
        isRunning = False
    display.update()
    clock.tick(fps)