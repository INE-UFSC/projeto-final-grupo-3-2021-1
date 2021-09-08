import pygame
from abc import ABC


class Personagem(ABC):

    def __init__(self, vida, vida_maxima, velocidade, posicao):
        self.__cor = (255, 0, 0)
        self.__mostrar = True
        self.__vida = vida
        self.__vida_maxima = vida_maxima
        self.__invulneravel = False
        self.__tempo_inicial_inv = 0
        self.__tempo_inv = 0
        self.__velocidade = velocidade
        self.__posicao = posicao


    @property
    def cor(self) -> tuple:
        return self.__cor

    @property
    def mostrar(self) -> bool:
        return self.__mostrar

    @property
    def vida(self) -> int:
        return self.__vida

    @property
    def vida_maxima(self) -> int:
        return self.__vida_maxima

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @property
    def posicao(self) -> list:
        return self.__posicao

    @property
    def invulneravel(self) -> bool:
        return self.__invulneravel

    @property
    def tempo_inicial_inv(self) -> float:
        return self.__tempo_inicial_inv

    @property
    def tempo_inv(self) -> float:
        return self.__tempo_inv

    @cor.setter
    def cor(self, nova: tuple):
        self.__cor = nova

    @mostrar.setter
    def mostrar(self, mostrar: bool):
        self.__mostrar = mostrar

    @tempo_inicial_inv.setter
    def tempo_inicial_inv(self, novo: float):
        self.__tempo_inicial_inv = novo

    @tempo_inv.setter
    def tempo_inv(self, novo: float):
        self.__tempo_inv = novo

    @invulneravel.setter
    def invulneravel(self, novo: bool):
        self.__invulneravel = novo

    @vida.setter
    def vida(self, vida: int):
        self.__vida = vida

    @velocidade.setter
    def velocidade(self, nova: int):
        self.__velocidade = nova

    @posicao.setter
    def posicao(self, nova):
        self.__posicao = nova

    # Torna o Personagem invulnerável por um determinado tempo, que, assume 0.5 segundos caso o valor não for especificado
    def tornar_invulneravel_por(self, tempo_inv=500):
        self.__tempo_inicial_inv = pygame.time.get_ticks()
        self.__tempo_inv = tempo_inv
        self.__invulneravel = True
