import pygame


class Tela:
    
    # resolução da tela
    def __init__(self, display = (928, 600)):
        self.display = display
        pygame.display.set_caption("Quebra Ossos")

        # setup da janela
        self.screen = pygame.display.set_mode(display)

tela = Tela()
