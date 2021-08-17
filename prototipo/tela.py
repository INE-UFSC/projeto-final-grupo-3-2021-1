import pygame

class Tela:

    def __init__(self, display = (928, 600)):# resolução da tela
        self.display = display
        pygame.display.set_caption("Quebra Ossos")
        self.screen = pygame.display.set_mode(display)# setup da janela

tela = Tela()
        
        


