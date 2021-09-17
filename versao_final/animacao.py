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
        # TRATAMENTO DE EXCESÇOES para o carregamento das sprites
        except TypeError:
            self.__carregar_multiplas()
        except FileNotFoundError as e:
            print(e)

    # carrega as sprites
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
    
    # pega todas as sprites
    def pegar_sprites(self):
        if self.cache_sprites_aux != []:
            return self.cache_sprites_aux, self.cache_sprites
        else:
            return self.cache_sprites

    # ABSTRAÇAO
    @abc.abstractmethod
    def popular_sprites(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

# HERANÇA de Animacao com uma especializaçao
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

    # pega as sprites e chama a funçao para colocar todas elas em uma lista
    def popular_sprites(self):
        self.__sprites_jogador_movendo, self.__sprites_jogador_pulando = super().pegar_sprites()

    # atualizaçao do desenho da sprite mudando elas
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

        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (26*2,29*2))
        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual


# HERANÇA de Animacao com uma especializaçao
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

    # pega as sprites e chama a funçao para colocar todas elas em uma lista
    def popular_sprites(self):
        self.__sprites_morcego_movendo = super().pegar_sprites()

    # atualiza as sprites mudando elas
    def update(self):
        self.__sprite_atual_index += constante

        if self.__movendo:
            if self.__sprite_atual_index >= len(self.__sprites_morcego_movendo):
                self.__sprite_atual_index = 0
            self.__sprite_atual = self.__sprites_morcego_movendo[int(self.__sprite_atual_index) - 1] 

        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (29*2,17*2))
        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual


# HERANÇA de Animacao com uma especializaçao 
class AnimacaoGolem(Animacao):

    def __init__(self):
        super().__init__('versao_final/src/golem/')
        self.__sprites_golem_movendo = []
        self.popular_sprites()

        self.__sprite_atual_index = 0
        self.__sprite_atual = self.__sprites_golem_movendo[self.__sprite_atual_index]
        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (34*2,38*2))

        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual

        self.__movendo = True

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    # pega as sprites e chama a funçao para colocar todas elas em uma lista
    def popular_sprites(self):
        self.__sprites_golem_movendo = super().pegar_sprites()

    # atualiza as sprites mudando elas
    def update(self):
        self.__sprite_atual_index += constante

        if self.__movendo:
            if self.__sprite_atual_index >= len(self.__sprites_golem_movendo):
                self.__sprite_atual_index = 0
            self.__sprite_atual = self.__sprites_golem_movendo[int(self.__sprite_atual_index) - 1] 

        self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (34*2,38*2))
        self.__rect = self.__sprite_atual.get_rect()
        self.image = self.__sprite_atual

# HERANÇA de Animacao com especializacao
class AnimacaoFundo(Animacao):

    def __init__(self, path: str, posicao_inicial: list):
        super().__init__(path)
        self.__sprite_fundo = []
        self.popular_sprites()

        self.image = self.__sprite_fundo[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = posicao_inicial

        self.jogando = True

    # pega as sprites e chama a funçao para colocar todas elas em uma lista
    def popular_sprites(self):
        self.__sprite_fundo = super().pegar_sprites()

    def update(self):
        pass

# Classe de sprites que nao possuem movimento
class Estatico(pygame.sprite.Sprite):
    def __init__(self, posicao, sprite_path, escala):
        pygame.sprite.Sprite.__init__(self)
        self.posicao = posicao
        self.imagem = pygame.image.load(sprite_path)
        self.imagem = pygame.transform.scale(self.imagem, (17*escala,17*escala))
        self.image = self.imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = [self.posicao[0], self.posicao[1]]

# HERANÇA de Estaico com especializaçao das sprites de quantidade de vida
class EstaticoCoracao(Estatico):

    def __init__(self, posicao):
        super().__init__(posicao, 'versao_final/src/estaticos/coracao.png', 2)

# HERANÇA de Estatico especializaçao das sprites dos poderes (poçoes)
class EstaticoPoder(Estatico):

    def __init__(self, posicao, path):
        super().__init__(posicao, path, 1)
