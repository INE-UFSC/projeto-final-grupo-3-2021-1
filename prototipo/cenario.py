from tela import tela
import pygame


class Cenario:

    def __init__(self, obstaculos: list):
        self.__obstaculos = obstaculos  # lista de obstaculos na tela


    @property
    def obstaculos(self):
        return self.__obstaculos
    
    # desenha o chão do game
    def desenhar(self):
        pygame.draw.line(tela.screen, (255,255,0), (0,578), (928,578), 90)

    
    def atualizar(self, dt):
        self.desenhar()

        # atualiza os obstáculos
        for obs in self.__obstaculos:
            obs.atualizar(dt)
