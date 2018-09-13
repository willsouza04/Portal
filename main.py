import pygame, os, ctypes, sys

from pygame.sprite import Group

from settings import Settings
from portal import Portal
from ball import Ball

def run_game():
    pygame.init()
    pygame.display.set_caption("Portal")

    user32 = ctypes.windll.user32
    screenSize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    screen = pygame.display.set_mode((screenSize), pygame.FULLSCREEN)

    settings = Settings(screenSize)
    settings.g_speed = settings.g_speed / 65

    portais = Group()
    portal_inicial = Portal(settings, screen, None)
    portais.add(portal_inicial)

    ball = Ball(settings, screen)

    while True:
        check_events(ball)

        ball.update()

        screen.fill(settings.bg_color)

        for portal in portais:
            portal.check_collision(settings, screen, ball, portais)
            portal.draw_portal()

        pygame.draw.line(screen, (255, 255, 255), [0, settings.bottom], [settings.screen_width, settings.bottom], 5)

        ball.draw_ball()

        pygame.display.flip()

def check_events(ball):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_RIGHT:
                ball.moving_right = True
            elif event.key == pygame.K_LEFT:
                ball.moving_left = True
            elif event.key == pygame.K_UP:
                ball.saltar()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ball.moving_right = False
            elif event.key == pygame.K_LEFT:
                ball.moving_left = False

run_game()
