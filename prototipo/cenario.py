from tela import tela
from poder import InvPoder, VidaPoder
from random import choice
import pygame


class Cenario:

    def __init__(self, obstaculos: list):
        self.__obstaculos = obstaculos      # lista de obstaculos
        self.__poder_na_tela = None         # atual poder na tela
        self.__tempo_invocado = 0           # o tempo em que o ultimo poder foi invocado
        self.__velocidade_acumulada = 0     # velocidade acumulada da aceleração do cenário
        self.__aceleracao = 5

    @property
    def obstaculos(self):
        return self.__obstaculos

    @property
    def poder_na_tela(self):
        return self.__poder_na_tela

    @poder_na_tela.setter
    def poder_na_tela(self, novo):
        self.__poder_na_tela = novo


    # invoca poderes na tela
    def invocador(self, dt):
        if pygame.time.get_ticks() - self.__tempo_invocado >= 10000:
            self.__poder_na_tela = choice([InvPoder(400+self.__velocidade_acumulada, [1328, 494]),
                                            VidaPoder(400+self.__velocidade_acumulada, [1328, 494])])

            self.__tempo_invocado = pygame.time.get_ticks()

        if self.__poder_na_tela != None:
            self.__poder_na_tela.atualizar(dt)


    # acelera todos os objetos do cenário (obstáculos e poderes)
    def acelerar(self):
        if self.obstaculos[0].posicao[0] <= -39:
            for obs in self.__obstaculos:
                obs.velocidade += self.__aceleracao
            self.__velocidade_acumulada += self.__aceleracao

            if self.poder_na_tela != None:
                self.__poder_na_tela.velocidade += self.__aceleracao
    

    # desenha o chão do game
    def desenhar(self):
        pygame.draw.line(tela.screen, (255,255,0), (0,578), (928,578), 90)


    def atualizar(self, dt):
        self.desenhar()
        self.invocador(dt)
        self.acelerar()

        # atualiza os obstáculos
        for obs in self.__obstaculos:
            obs.atualizar(dt)
