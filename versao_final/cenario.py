from tela import tela
from poder import InvPoder, VidaPoder
from random import choice
from animacao import EstaticoCoracao, AnimacaoFundo
import pygame


class Cenario:

    def __init__(self, obstaculos: list):
        self.__obstaculos = obstaculos      # lista de obstaculos
        self.__poder_na_tela = None         # atual poder na tela
        self.__tempo_invocado = 0           # o tempo em que o ultimo poder foi invocado
        self.__velocidade_acumulada = 0     # velocidade acumulada da aceleração do cenário
        self.__aceleracao = 5
        self.__coracoes = [pygame.sprite.Group(coracao) for coracao in [EstaticoCoracao([800, 10]),
                                                                        EstaticoCoracao([840, 10]),
                                                                        EstaticoCoracao([880, 10])]]

        self.__posicao_fundo = [0, 0]
        self.__posicao_fundo_inv = [928, 0]
        self.__fundos = pygame.sprite.Group(AnimacaoFundo('versao_final/src/backgrounds/fundo_jogo/fundo_nrml/', self.__posicao_fundo),
                                            AnimacaoFundo('versao_final/src/backgrounds/fundo_jogo/fundo_inv/', self.__posicao_fundo_inv))

    @property
    def coracoes(self):
        return self.__coracoes

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
            self.__poder_na_tela = choice([InvPoder(400+self.__velocidade_acumulada, [1328, 424]),
                                            VidaPoder(400+self.__velocidade_acumulada, [1328, 424])])

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


    def mover_cenario(self, dt):
        self.__posicao_fundo[0] -= (0.5 + self.__velocidade_acumulada*dt/3)
        self.__posicao_fundo_inv[0] -= (0.5 + self.__velocidade_acumulada*dt/3)

        fundo_index = 0
        for posicao in [self.__posicao_fundo, self.__posicao_fundo_inv]:
            if posicao[0] <= -928:
                posicao[0] = 928

            self.__fundos.sprites()[fundo_index].rect.topleft = posicao
            fundo_index += 1


    # desenha o chão do game
    def desenhar(self):
        self.__fundos.draw(tela.screen)
        self.__fundos.update()
        # pygame.draw.line(tela.screen, (255,255,0), (0,578), (928,578), 90)


    def atualizar(self, dt):
        self.desenhar()
        self.mover_cenario(dt)
        self.invocador(dt)

        # atualiza os obstáculos
        for obs in self.__obstaculos:
            obs.atualizar(dt)
