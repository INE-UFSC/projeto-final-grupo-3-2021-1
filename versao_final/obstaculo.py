from animacao import Animacao, AnimacaoGolem, AnimacaoMorcego
import pygame
from tela import tela
from random import randint


class Obstaculo():

    def __init__(self, posicao: list, velocidade: int, animacoes: list):
        self.__vivo = True
        self.__posicao = posicao
        self.__aparecer_entre = (1228, 1500)
        self.__velocidade = velocidade
        
        self.__animacoes = animacoes
        self.__animacao_atual = pygame.sprite.Group(self.__animacoes[0])
        self.__rect = self.__animacao_atual.sprites()[0].rect


    # Getters e setters
    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def posicao(self):
        return self.__posicao

    @property
    def rect(self):
        return self.__rect

    @velocidade.setter
    def velocidade(self, nova):
        self.__velocidade = nova


    # troca a animacao
    def trocar_animacao(self, animacao_index: int):
        if self.__animacao_atual.index(self.__animacao_atual.sprites()[0]) != animacao_index:
            self.__animacao_atual = pygame.sprite.Group(self.__animacoes[animacao_index])

    # movimenta o obstaculo
    def movimento(self, dt, aparecer: int):
        if self.__vivo:
            self.__posicao[0] -= self.__velocidade * dt
            if self.__posicao[0] <= -80:
                self.__posicao[0] = aparecer

    # desenha o obstaculo
    def desenhar(self):
        self.__animacao_atual.sprites()[0].rect.topleft = self.posicao
        self.__rect = self.__animacao_atual.sprites()[0].rect
        self.__animacao_atual.draw(tela.screen)

        self.__animacao_atual.update()

        if self.__vivo is False:
            pass

    # reseta a posicao, não "mata" de verdade
    def matar(self):
        self.__vivo = False
        self.trocar_animacao(1)
        
    # main loop
    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt, randint(self.__aparecer_entre[0], self.__aparecer_entre[1]))


class Morcego(Obstaculo):
    
    def __init__(self, posicao: list, velocidade: int):
        super().__init__(posicao,
                        velocidade,
                        [Animacao((29, 17), 'versao_final/src/morcego/movimento/'),
                        Animacao((29, 17), 'versao_final/src/morcego/morte/')])


class Golem(Obstaculo):
    
    def __init__(self, posicao: list, velocidade: int):
        super().__init__(posicao,
                        velocidade,
                        [Animacao((34, 38), 'versao_final/src/golem/movimento/'),
                        Animacao((34, 38), 'versao_final/src/golem/morte/')])