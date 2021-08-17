from tela import tela
import pygame


class Cenario:

    def __init__(self):
        self.imagem = None
    
    def desenhar(self):
        pygame.draw.line(tela.screen, (255,255,0), (0,578), (928,578), 90)#(255,255,0), (0,536), (928,536), 5)

    def atualizar(self):
        self.desenhar()