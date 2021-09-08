import pygame
import abc
import os
from copy import copy


"""
to do list (anthon):
    - Criar uma classe abstrata Animacao que funciona como um DAO para as sprites, para facilitar quando for implementar animações em obstaculos (q inclusive ja fecha com o princípio open-closed)
    - Instanciar classes provenientes da classe Animacao nas classes correspontes Ex.: AnimacaoCavaleiro() em Jogador
    - Manipular as classes filhas de Animacao dentro das classes correspondentes, facilita a leitura e o entendimento
    - organizar o projeto em arq. MVC
"""


class Animacao(pygame.sprite.Sprite, abc.ABC):

    def __init__(self, path):
        pygame.sprite.Sprite.__init__(self)
        self.cache_sprites = []
        self.cache_sprites_aux = []
        self.path = path
        try:
            self.__carregar()
        except TypeError:
            self.__carregar_multiplas()
        except FileNotFoundError as e:
            print(e)

    def __carregar(self):
        for sprite in os.listdir(self.path):
            self.cache_sprites.append(pygame.image.load(self.path + sprite))

    def __carregar_multiplas(self):
        paths = copy(self.path)
        aux = True

        for path in paths:
            self.path = path
            self.__carregar()

            if aux:
                self.cache_sprites_aux = copy(self.cache_sprites)
                self.cache_sprites.clear()
                aux = False
        
    def pegar_sprites(self):
        if self.cache_sprites_aux != []:
            return self.cache_sprites_aux, self.cache_sprites
        else:
            return self.cache_sprites

    @abc.abstractmethod
    def popular_sprites(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass


class AnimacaoCavaleiro(Animacao):

    def __init__(self):
        super().__init__(['versao_final/src/cavaleiro/movimento/', 'versao_final/src/cavaleiro/pulo/'])
        self.__sprites_jogador_movendo = []
        self.__sprites_jogador_pulando = []
        self.popular_sprites()

        self.__sprite_atual_index = 0
        self.__sprite_atual = self.__sprites_jogador_movendo[self.__sprite_atual_index]
        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (26*2,29*2))

        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual


    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect


    def popular_sprites(self):
        self.__sprites_jogador_movendo, self.__sprites_jogador_pulando = super().pegar_sprites()


    def update(self, pulando: bool):
        self.__sprite_atual_index += 0.020

        if not pulando:
            if self.__sprite_atual_index >= len(self.__sprites_jogador_movendo):
                self.__sprite_atual_index = 0
            self.__sprite_atual = self.__sprites_jogador_movendo[int(self.__sprite_atual_index) - 1] 

        if pulando:
            if self.__sprite_atual_index >= len(self.__sprites_jogador_pulando):
                self.__sprite_atual_index = 0
            self.__sprite_atual = self.__sprites_jogador_pulando[int(self.__sprite_atual_index) - 1]

        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (26*2,29*2))
        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual


class AnimacaoFundo(Animacao):

    def __init__(self):
        super().__init__('versao_final/src/backgrounds/')
        self.__sprite_fundo = []
        self.popular_sprites()

        self.image = self.__animacao_fundo[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [464, 300]

        self.jogando = True

    def popular_sprites(self):
        self.__sprite_fundo = super().pegar_sprites()

    def update(self):
        if self.jogando:
            self.rect.topleft[0] += 10
        if self.rect.topleft[0] <= 464:
            self.rect.topleft[0] = 0


class EstaticoCoracao(pygame.sprite.Sprite):

    def __init__(self, posicao= []):
        pygame.sprite.Sprite.__init__(self)
        self.posicao = posicao
        self.imagem_coracao = pygame.image.load('versao_final/src/estaticos/coracao.png')
        self.imagem_coracao = pygame.transform.scale(self.imagem_coracao, (17*2,17*2))
        self.image = self.imagem_coracao
        self.rect = self.imagem_coracao.get_rect()
        self.rect.topleft = [self.posicao[0], self.posicao[1]]