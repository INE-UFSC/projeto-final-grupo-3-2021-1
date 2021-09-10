from animacao import AnimacaoGolem, AnimacaoMorcego
import pygame
from tela import tela


class Obstaculo(pygame.sprite.Sprite):

    def __init__(self, posicao: list, velocidade: int, tipo: str):
        self.__posicao = posicao
        self.__velocidade = velocidade
        self.__tipo = tipo
        # self.__retangulo = pygame.Rect(self.__posicao[0], self.__posicao[1], self.__tamanho[0], self.__tamanho[1])

        self.__animacao_morcego = pygame.sprite.Group(AnimacaoMorcego())
        self.rect_morcego = self.__animacao_morcego.sprites()[0].rect

        self.__animacao_golem = pygame.sprite.Group(AnimacaoGolem())
        self.rect_golem = self.__animacao_golem.sprites()[0].rect


    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def posicao(self):
        return self.__posicao

    @property
    def retangulo(self):
        return self.__retangulo

    @velocidade.setter
    def velocidade(self, nova):
        self.__velocidade = nova

    # movimenta o obstaculo
    def movimento(self, dt, aparecer: int):
       self.__posicao[0] -= self.__velocidade * dt
       if self.__posicao[0] <= -80:
           self.__posicao[0] = aparecer

    # desenha os obstaculos
    def desenhar(self):
        if self.__tipo == "Morcego":
            self.__animacao_morcego.sprites()[0].rect.topleft = self.posicao
            self.rect_morcego = self.__animacao_morcego.sprites()[0].rect
            self.__animacao_morcego.draw(tela.screen)

        if self.__tipo == "Golem":
            self.__animacao_golem.sprites()[0].rect.topleft = self.posicao
            self.rect_golem = self.__animacao_golem.sprites()[0].rect
            self.__animacao_golem.draw(tela.screen)

        self.__animacao_morcego.update()
        self.__animacao_golem.update()
        # pygame.draw.rect(tela.screen, (0, 255, 0), self.__retangulo)
        # self.__retangulo = pygame.Rect(self.__posicao[0], self.__posicao[1], self.__tamanho[0], self.__tamanho[1])

    # atualiza os obsculos
    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt, 1228)

