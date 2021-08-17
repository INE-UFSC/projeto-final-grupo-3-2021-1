from jogador import Jogador
from obstaculo import Obstaculo
from cenario import Cenario
from tela import tela
import pygame


class Jogo():

    def __init__(self, jogador: Jogador, cenario: Cenario, inimigos: list, obstaculos: list):
        self.jogador = jogador              # objeto do jogador
        self.__inimigos = inimigos          # lista de objetos dos inimigos na tela
        self.__cenario = cenario            # objeto do cenário
        self.__obstaculos = obstaculos      # lista de obstaculos na tela
        self.__pontuacao = 0                # pontuação atual do jogo

    def atualizar_tela(self, dt):
        if self.jogador.vida > 0:

            # atualiza cenário
            self.__cenario.atualizar()

            # atualiza o jogador
            self.jogador.atualizar(dt)

            # atualiza obstáculos
            for obs in self.__obstaculos:
                obs.atualizar(dt, self.jogador)

            pygame.display.update()
