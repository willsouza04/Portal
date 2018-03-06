import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    def __init__(self, settings, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.settings = settings

        self.x = randint(1,  settings.screen_width - settings.ball_size)
        self.y = settings.bottom - settings.ball_size

        self.vx = 0
        self.vy = 0

        self.moving_right = False
        self.moving_left = False

        self.almentar = False

    def update(self):
        if self.moving_right and self.vx < 1:
            self.vx += 0.15
        if self.moving_left and self.vx > -1:
            self.vx += -0.15

        if self.x + self.settings.ball_size <= self.settings.screen_width and self.x >= 0:
            self.x += self.vx
        elif self.x + self.settings.ball_size > self.settings.screen_width:
            self.x = self.settings.screen_width - self.settings.ball_size
        else:
            self.x = 0

        if self.y + self.settings.ball_size > self.settings.bottom:
            self.y = self.settings.bottom - self.settings.ball_size

        if self.vx > 0:
            self.vx -= 0.05
        elif self.vx < 0:
            self.vx += 0.05
        if self.vx < 0.05 and self.vx > -0.05:
            self.vx = 0

        self.y += self.vy

        if self.settings.bottom >= self.y + 50:
            self.vy += self.settings.g_speed
        if self.vy > 0 and self.settings.bottom <= self.y + 50:
            self.vy = 0

        if self.almentar:
            if self. vy < -5:
                self.almentar = False
            else:
                self.vy -= self.settings.g_speed * 2

    def saltar(self):
        if not self.settings.bottom > self.y + 50:
            self.almentar = True


    def draw_ball(self):
        pygame.draw.ellipse(self.screen, self.settings.ball_color,
                            [int(self.x), int(self.y), self.settings.ball_size, self.settings.ball_size])