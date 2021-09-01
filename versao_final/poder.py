from jogador import Jogador
from tela import tela
import pygame
import abc


# Classe base do poder
class Poder(abc.ABC):

    def __init__(self, diferencial: int, cor: tuple, velocidade: float, posicao: list):
        self.__cor = cor
        self.__diferencial = diferencial
        self.__velocidade = velocidade
        self.__posicao = posicao
        self.__retangulo = pygame.Rect(self.__posicao[0], self.__posicao[1], 10, 10)
    

    @property
    def diferencial(self):
        return self.__diferencial

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

    @retangulo.setter
    def retangulo(self, novo):
        self.__retangulo = novo

    @abc.abstractmethod
    def usar(self, jogador: Jogador):
        pass


    # movimenta o poder
    def movimento(self, dt):
       self.__posicao[0] -= self.__velocidade * dt


    # desenha os poderes no chao
    def desenhar(self):
        pygame.draw.rect(tela.screen, self.__cor, self.__retangulo)
        self.__retangulo = pygame.Rect(self.__posicao[0], self.__posicao[1], 10, 10)


    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt)


# Poder que aumenta 1 ponto de vida
class VidaPoder(Poder):
    
    def __init__(self, velocidade: float, posicao: list):
        super().__init__(diferencial=1, cor=(255, 0, 0), velocidade=velocidade, posicao=posicao)

    def usar(self, jogador: Jogador):
        if jogador.vida != jogador.vida_maxima:
            jogador.vida += 1


# Poder que deixa o jogador invulnerável por 3 segundos
class InvPoder(Poder):

    def __init__(self, velocidade: float, posicao: list):
        super().__init__(diferencial=3000, cor=(0, 0, 255), velocidade=velocidade, posicao=posicao)

    def usar(self, jogador: Jogador):
        jogador.tornar_invulneravel_por(self.diferencial)
