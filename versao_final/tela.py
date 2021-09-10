import pygame
from singleton import Singleton


class Tela(Singleton):
    
    # resolução da tela
    def __init__(self, display = (928, 600)):
        super().__init__()
        self.display = display
        pygame.display.set_caption("Quebra Ossos")

        # setup da janela
        self.screen = pygame.display.set_mode(display)

tela = Tela()
