import pygame.ftfont

class Button():

    def __init__(self, infrompy_settings, screen, msg):
        """ Initialise Button attribute """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.txt_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        # Build the button's rect object and center
        self.rect = pygame.Rect(500, 375, self.width, self.height)
        self.rect_center = self.screen_rect.center

        # The button message need to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn our msg into a rendered image and center the text. """
        self.msg_image = self.font.render(msg, True, self.txt_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect_center

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
