import pygame
from tela import tela


class Obstaculo(pygame.sprite.Sprite):

    def __init__(self, posicao: list, velocidade: int, tamanho: list):
        self.__posicao = posicao
        self.__velocidade = velocidade
        self.__tamanho = tamanho
        self.__retangulo = pygame.Rect(self.__posicao[0], self.__posicao[1], self.__tamanho[0], self.__tamanho[1])


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
       if self.__posicao[0] <= -40:
           self.__posicao[0] = aparecer

    # desenha os obstaculos
    def desenhar(self):
        pygame.draw.rect(tela.screen, (0, 255, 0), self.__retangulo)
        self.__retangulo = pygame.Rect(self.__posicao[0], self.__posicao[1], self.__tamanho[0], self.__tamanho[1])

    # atualiza os obsculos
    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt, 1328)
