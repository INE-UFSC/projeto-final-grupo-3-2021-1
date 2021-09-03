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
        for path in paths:
            self.path = path
            self.__carregar()
            self.cache_sprites_aux = copy(self.cache_sprites)
            self.cache_sprites.clear()
        
    def pegar_sprites(self):
        if self.cache_sprites_aux != []:
            return self.cache_sprites_aux, self.cache_sprites
        else:
            return self.cache_sprites


class AnimacaoCavaleiro(Animacao):
    def __init__(self):
        super().__init__(['versao_final/src/cavaleiro/movimento/', 'versao_final/src/cavaleiro/pulo/'])
        self.__animacao_jogador_movendo = []
        self.__animacao_jogador_pulando = []
        self.popular_animacoes()

        self.movendo = True
        self.pulando = False

        self.imagem_atual = 0
        self.image = self.__animacao_jogador_movendo[self.imagem_atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]

        self.image = pygame.transform.scale(self.image, (26*2,29*2))
        

    def popular_animacoes(self):
        self.__animacao_jogador_movendo, self.__animacao_jogador_pulando = super().pegar_sprites()


    def update(self):
        if self.movendo:
            self.imagem_atual += 0.020
            if self.imagem_atual >= len(self.__animacao_jogador_movendo):
                self.imagem_atual = 0
            self.image = self.__animacao_jogador_movendo[int(self.imagem_atual) - 1]

        if self.pulando:
            self.movendo = False
            self.imagem_atual += 0.020
            if self.imagem_atual >= len(self.__animacao_jogador_pulando):
                self.movendo = True
            self.image = self.__animacao_jogador_pulando[int(self.imagem_atual) - 1]
        
        self.image = pygame.transform.scale(self.image, (26*2,29*2))

class Fundo(Animacao):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.__path = 'versao_final/src/backgrounds/'
        self.__animacao_fundo = []
        self.popular_animacoes()

        self.image = self.__animacao_fundo[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [464, 300]

        self.jogando = True

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
        self.rect = self.imagem_coracao.get_rect()
        self.rect.topleft = [self.posicao[0], self.posicao[1]]


todas_as_sprites = pygame.sprite.Group()

cavaleiro = AnimacaoCavaleiro()
todas_as_sprites.add(cavaleiro)