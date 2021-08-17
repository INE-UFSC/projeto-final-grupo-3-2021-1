import pygame

class Personagem(pygame.sprite.Sprite):

    def __init__(self, vida, vida_maxima, velocidade, posicao):
        self.__vida = vida
        self.__vida_maxima = vida_maxima
        self.__velocidade = velocidade
        self.__posicao = posicao

    
    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @property
    def vida_maxima(self):
        return self.__vida_maxima

    @vida_maxima.setter
    def vida_maxima(self):
        pass

    @property
    def dano(self):
        return self.__dano

    @dano.setter
    def dano(self):
        pass

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self):
        pass

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self):
        pass
