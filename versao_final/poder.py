from jogador import Jogador
from tela import Tela
from tela import tela
from animacao import EstaticoPoder
import pygame
import abc
from pygame import mixer


# Classe base do poder
class Poder(abc.ABC):

    def __init__(self, diferencial: int, velocidade: float, posicao: list, sprite_path: str):
        self.__diferencial = diferencial
        self.__velocidade = velocidade
        self.__posicao = posicao
        self.__retangulo = pygame.Rect(self.__posicao[0], self.__posicao[1], 10, 10)
        self.__animacao = pygame.sprite.Group(EstaticoPoder(posicao, sprite_path))
    
    # getters
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

    # setters
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
        self.__animacao.sprites()[0].rect.topleft = self.__posicao
        self.__retangulo = self.__animacao.sprites()[0].rect
        self.__animacao.draw(tela.screen)
        # pygame.draw.rect(Tela().screen, self.__cor, self.__retangulo)
        # self.__retangulo = pygame.Rect(self.__posicao[0], self.__posicao[1], 10, 10)


    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt)


# Poder que aumenta 1 ponto de vida
class VidaPoder(Poder):
    
    def __init__(self, velocidade: float, posicao: list):
        super().__init__(diferencial=1,
                        velocidade=velocidade,
                        posicao=posicao,
                        sprite_path='versao_final/src/estaticos/pocao_vida.png')

    def usar(self, jogador: Jogador):
        if jogador.vida != jogador.vida_maxima:
            jogador.vida += 1


# Poder que deixa o jogador invulnerável por 3 segundos
class InvPoder(Poder):

    def __init__(self, velocidade: float, posicao: list):
        super().__init__(diferencial=3000,
                        velocidade=velocidade,
                        posicao=posicao,
                        sprite_path='versao_final/src/estaticos/pocao_inv.png')

    # funçao que é chamado quando o jogador pega o poder, criando um som e chamando a funçao da invulnerabilidade
    def usar(self, jogador: Jogador):
        invencivel = mixer.Sound('versao_final/src/efeitos_sonoros/invenc.mp3')
        invencivel.play(3)
        jogador.tornar_invulneravel_por(self.diferencial)
