import pygame
from pygame.sprite import Sprite
from random import randint

class Portal(Sprite):
    def __init__(self, settings, screen, exit):
        super(Portal, self).__init__()
        self.screen = screen
        self.settings = settings

        self.rect = pygame.Rect(0, 0, settings.portal_size[0], settings.portal_size[1])

        self.color = (randint(1, 255), randint(1, 255), randint(1, 255))

        if exit == None:
            self.rect.center = (randint(1 + settings.portal_size[0], settings.screen_width - settings.portal_size[0]),
                                settings.bottom - (settings.portal_size[1] / 2))
            self.exit = Portal(settings, screen, self)
            self.clone = False
        else:
            self.rect.center = (randint(1 + settings.portal_size[0], settings.screen_width - settings.portal_size[0]),
                                randint(1 + settings.portal_size[1], settings.bottom - settings.portal_size[1] - (settings.portal_size[1] / 2)))
            self.exit = exit
            self.color = self.exit.color
            self.clone = True

    def check_collision(self, settings, screen, ball, portais):
        if(self.rect.top > ball.y + settings.ball_size or
            self.rect.bottom < ball.y or
            self.rect.left > ball.x + settings.ball_size or
            self.rect.right < ball.x):
            if not self.clone:
                self.exit.check_collision(settings, screen, ball, portais)
        else:
            if ball.x < self.rect.centerx:
                ball.x = int(self.exit.rect.centerx + settings.portal_size[0]/2 + 1)
            else:
                ball.x = int(self.exit.rect.centerx - (settings.ball_size + settings.portal_size[0]/2) - 1)
            ball.y = int(self.exit.rect.centery)
            """portal = Portal(settings, screen, None)
            portais.add(portal)"""

    def draw_portal(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        if not self.clone:
            self.exit.draw_portal()