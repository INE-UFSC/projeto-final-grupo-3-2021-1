from animacao import AnimacaoGolem, AnimacaoMorcego
import pygame
from tela import tela


class Obstaculo():

    def __init__(self, posicao: list, velocidade: int, tipo: str):
        self.__posicao = posicao
        self.__velocidade = velocidade
        self.__tipo = tipo
        
        self.__animacao_morcego = AnimacaoMorcego(0.03, 'versao_final/src/morcego/')
        self.rect_morcego = pygame.Rect(0, 0, 0, 0)

        self.__animacao_golem = AnimacaoGolem(0.03, 'versao_final/src/golem/')
        self.rect_golem = pygame.Rect(0, 0, 0, 0)

    # Getters e setters
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
        #    self.__velocidade += 10

    # desenha os obstaculos
    def desenhar(self):
        if self.__tipo == "Morcego":
            self.__animacao_morcego.update(self.__posicao)
            self.rect_morcego = self.__animacao_morcego.acompanhar_posicao(self.__posicao)
            self.__animacao_morcego.draw(tela.screen)

        if self.__tipo == "Golem":
            self.__animacao_golem.update(self.__posicao)
            self.rect_golem = self.__animacao_morcego.acompanhar_posicao(self.__posicao)
            self.__animacao_golem.draw(tela.screen)


    # atualiza os obsculos
    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt, 1228)

