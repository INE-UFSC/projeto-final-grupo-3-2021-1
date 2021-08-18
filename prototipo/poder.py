from jogador import Jogador
from tela import tela
import pygame
import abc

# Classe base do poder
class Poder(abc.ABC):

    def __init__(self, diferencial: int, cor: tuple, posicao: list):
        self.__diferencial = diferencial 
        self.__cor = cor
        self.__posicao = []
        self.__retangulo = pygame.Rect()
    
    @property
    def diferencial(self):
        return self.__diferencial

    @abc.abstractmethod
    def usar(self, jogador: Jogador):
        pass
    
    # desenha os poderes no chao
    def desenhar(self):
        pygame.draw.rect(tela.screen, self.__cor, self.__retangulo)
        self.__retangulo = pygame.Rect(self.__posicao[0], self.__posicao[1], 10,10)

    def atualizar(self):
        self.desenhar()

# Poder que aumenta 1 ponto de vida
class VidaPoder(Poder):
    
    def __init__(self):
        super().__init__(diferencial=1, cor=(255, 0, 0))

    def usar(self, jogador: Jogador):
        jogador.vida += 1
        del self

# Poder que deixa o jogador invulnerável por 3 segundos
class InvPoder(Poder):

    def __init__(self):
        super().__init__(diferencial=3000, cor=(0, 0, 255))

    def usar(self, jogador: Jogador):
        jogador.tornar_invulneravel_por(self.diferencial)
        del self

# Poder que dobra o tamanho do pulo
class PuloPoder(Poder):
    
    def __init__(self):
        super().__init__(diferencial=2, cor=(0, 255, 0))

    def usar(self, jogador: Jogador):
        jogador.__tamanho_pulo *= self.__diferencial
        del self
