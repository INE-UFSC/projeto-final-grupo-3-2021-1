import pygame
import abc
import os
from copy import copy

from pygame import constants
from constantes import Constantes


"""
to do list (anthon):
    ✓ - Criar uma classe abstrata Animacao que funciona como um DAO para as sprites, para facilitar quando for implementar animações em obstaculos (q inclusive ja fecha com o princípio open-closed)
    ✓ - Instanciar classes provenientes da classe Animacao nas classes correspontes Ex.: AnimacaoCavaleiro() em Jogador
    ✓ - Manipular as classes filhas de Animacao dentro das classes correspondentes, facilita a leitura e o entendimento
    - organizar o projeto em arq. MVC
"""
constante = 0.030

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
        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (26*3,29*3))

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
        self.__sprite_atual_index += constante

        if not pulando:
            if self.__sprite_atual_index >= len(self.__sprites_jogador_movendo):
                self.__sprite_atual_index = 0
            self.__sprite_atual = self.__sprites_jogador_movendo[int(self.__sprite_atual_index) - 1] 

        if pulando:
            if self.__sprite_atual_index >= len(self.__sprites_jogador_pulando):
                self.__sprite_atual_index = 0
            self.__sprite_atual = self.__sprites_jogador_pulando[int(self.__sprite_atual_index) - 1]

        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (26*3,29*3))
        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual


class AnimacaoMorcego(Animacao):

    def __init__(self):
        super().__init__('versao_final/src/morcego/')
        self.__sprites_morcego_movendo = []
        self.popular_sprites()

        self.__sprite_atual_index = 0
        self.__sprite_atual = self.__sprites_morcego_movendo[self.__sprite_atual_index]
        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (29*2,17*2))

        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual

        self.__movendo = True

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def popular_sprites(self):
        self.__sprites_morcego_movendo = super().pegar_sprites()

    def update(self):
        self.__sprite_atual_index += constante

        if self.__movendo:
            if self.__sprite_atual_index >= len(self.__sprites_morcego_movendo):
                self.__sprite_atual_index = 0
            self.__sprite_atual = self.__sprites_morcego_movendo[int(self.__sprite_atual_index) - 1] 

        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (29*2,17*2))
        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual


class AnimacaoGolem(Animacao):

    def __init__(self):
        super().__init__('versao_final/src/golem/')
        self.__sprites_golem_movendo = []
        self.popular_sprites()

        self.__sprite_atual_index = 0
        self.__sprite_atual = self.__sprites_golem_movendo[self.__sprite_atual_index]
        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (34*3,38*3))

        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual

        self.__movendo = True

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def popular_sprites(self):
        self.__sprites_golem_movendo = super().pegar_sprites()

    def update(self):
        self.__sprite_atual_index += constante

        if self.__movendo:
            if self.__sprite_atual_index >= len(self.__sprites_golem_movendo):
                self.__sprite_atual_index = 0
            self.__sprite_atual = self.__sprites_golem_movendo[int(self.__sprite_atual_index) - 1] 

        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (34*3,38*3))
        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual


class AnimacaoFundo(Animacao):

    def __init__(self, path: str, posicao_inicial: list):
        super().__init__(path)
        self.__sprite_fundo = []
        self.popular_sprites()

        self.image = self.__sprite_fundo[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = posicao_inicial

        self.jogando = True

    def popular_sprites(self):
        self.__sprite_fundo = super().pegar_sprites()

    def update(self):
        pass


class Estatico(pygame.sprite.Sprite):
    def __init__(self, posicao, sprite_path):
        pygame.sprite.Sprite.__init__(self)
        self.posicao = posicao
        self.imagem = pygame.image.load(sprite_path)
        self.imagem = pygame.transform.scale(self.imagem, (17*2,17*2))
        self.image = self.imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = [self.posicao[0], self.posicao[1]]

class EstaticoCoracao(Estatico):

    def __init__(self, posicao):
        super().__init__(posicao, 'versao_final/src/estaticos/coracao.png')


class EstaticoPoder(Estatico):

    def __init__(self, posicao, path):
        super().__init__(posicao, path)
