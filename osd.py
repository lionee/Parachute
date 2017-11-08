import pygame

class osd:
    def __init__(self):
        self.font = pygame.font.SysFont("comicsansms", 20)
        self.text = ""

    def update(self, text):
        self.text = text

    def render(self, surface, color):

        scoretext = self.font.render(self.text, 1, color)
        surface.blit(scoretext, (20, 20))