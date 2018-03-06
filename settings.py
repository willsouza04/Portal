class Settings():

    def __init__(self, screenSize):
        # Configurações da tela
        self.screen_width = screenSize[0]
        self.screen_height = screenSize[1]
        self.bg_color = (0, 0, 0)
        self.bottom = self.screen_height - 100

        self.portal_size = (10, 80)

        self.ball_color = (255, 255, 255)
        self.ball_size = 50
        self.g_speed = 0.15
