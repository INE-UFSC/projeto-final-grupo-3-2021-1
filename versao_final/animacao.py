import pygame
import abc
import os
from copy import copy
from pygame import constants
from constantes import Constantes


class Animacao(pygame.sprite.Sprite):

    def __init__(self, dimensao, path, velocidade=0.03, rodar_uma_vez=False):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        try:
            self.__carregar_sprites(path)
        except FileNotFoundError as e:
            print(e)
        
        self.sprite_atual_index = 0
        self.velocidade_troca_sprite = velocidade

        self.rodar_uma_vez = rodar_uma_vez
        self.atualizar = True

        self.sprite_atual = self.sprites[self.sprite_atual_index]
        self.rect = self.sprite_atual.get_rect()
        self.dimensao = dimensao

        self.sprite_atual = pygame.transform.scale(self.sprite_atual, (dimensao[0]*2, dimensao[1]*2))
        self.image = self.sprite_atual


    # carrega as sprites
    def __carregar_sprites(self, path):
        for nome_sprite in os.listdir(path):
            self.sprites.append(pygame.image.load(path + nome_sprite))


    # processa o sprite atual, alterando a escala, o rect e a image do pygame.sprite.Sprite
    def processar_sprite(self):
        self.sprite_atual = pygame.transform.scale(self.sprite_atual, (self.dimensao[0]*2, self.dimensao[1]*2))
        self.rect = self.sprite_atual.get_rect()
        self.image = self.sprite_atual


    # troca de sprite com base na velocidade
    def update(self):
        if self.atualizar:
            self.sprite_atual_index += self.velocidade_troca_sprite

            if self.sprite_atual_index >= len(self.sprites):
                self.sprite_atual_index = 0

                if self.rodar_uma_vez:
                    self.atualizar = False

            self.sprite_atual = self.sprites[int(self.sprite_atual_index) - 1] 
            self.processar_sprite()

 
# class Animacao(pygame.sprite.Sprite, abc.ABC):

#     def __init__(self, path):
#         pygame.sprite.Sprite.__init__(self)
#         self.contantes = Constantes()
#         self.cache_sprites = []
#         self.cache_sprites_aux = []
#         self.path = path
#         try:
#             self.__carregar()
#         # TRATAMENTO DE EXCEÇOES para o carregamento das sprites
#         except TypeError:
#             self.__carregar_multiplas()
#         except FileNotFoundError as e:
#             print(e)

#     # carrega as sprites
#     def __carregar(self):
#         for sprite in os.listdir(self.path):
#             self.cache_sprites.append(pygame.image.load(self.path + sprite))

#     # carrega mais de uma sprite
#     def __carregar_multiplas(self):
#         paths = copy(self.path)
#         aux = True

#         for path in paths:
#             self.path = path
#             self.__carregar()

#             if aux:
#                 self.cache_sprites_aux = copy(self.cache_sprites)
#                 self.cache_sprites.clear()
#                 aux = False
    
#     # pega todas as sprites
#     def pegar_sprites(self):
#         if self.cache_sprites_aux != []:
#             return self.cache_sprites_aux, self.cache_sprites
#         else:
#             return self.cache_sprites

#     # ABSTRAÇAO
#     @abc.abstractmethod
#     def popular_sprites(self):
#         pass

#     @abc.abstractmethod
#     def update(self):
#         pass

# HERANÇA de Animacao com uma especializaçao
# class AnimacaoCavaleiro(Animacao):

#     def __init__(self):
#         super().__init__(['versao_final/src/cavaleiro/movimento/', 'versao_final/src/cavaleiro/pulo/'])
#         self.__sprites_jogador_movendo = []
#         self.__sprites_jogador_pulando = []
#         self.popular_sprites()

#         self.__sprite_atual_index = 0
#         self.__sprite_atual = self.__sprites_jogador_movendo[self.__sprite_atual_index]
#         self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (26*2,29*2))

#         self.__rect = self.__sprite_atual.get_rect()
#         self.image = self.__sprite_atual

#     @property
#     def rect(self):
#         return self.__rect

#     @rect.setter
#     def rect(self, rect):
#         self.__rect = rect

#     # pega as sprites e chama a funçao para colocar todas elas em uma lista
#     def popular_sprites(self):
#         self.__sprites_jogador_movendo, self.__sprites_jogador_pulando = super().pegar_sprites()

#     # atualizaçao do desenho da sprite mudando elas
#     def update(self, pulando: bool):
#         self.__sprite_atual_index += self.contantes.atualizar_sprite

#         # seleçao das sprites se ele estiver pulando ou se estiver somente correndo
#         if not pulando:
#             if self.__sprite_atual_index >= len(self.__sprites_jogador_movendo):
#                 self.__sprite_atual_index = 0
#             self.__sprite_atual = self.__sprites_jogador_movendo[int(self.__sprite_atual_index) - 1] 

#         if pulando:
#             if self.__sprite_atual_index >= len(self.__sprites_jogador_pulando):
#                 self.__sprite_atual_index = 0
#             self.__sprite_atual = self.__sprites_jogador_pulando[int(self.__sprite_atual_index) - 1]

#         self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (26*2,29*2))
#         self.__rect = self.__sprite_atual.get_rect()
#         self.image = self.__sprite_atual


# # HERANÇA de Animacao com uma especializaçao
# class AnimacaoMorcego(Animacao):

#     def __init__(self):
#         super().__init__(['versao_final/src/morcego/','versao_final/src/death_bat/'])
#         self.__sprites_morcego_movendo = []
#         self.__sprites_morcego_morrendo = []
#         self.popular_sprites()

#         self.__sprite_atual_index = 0
#         self.__sprite_atual = self.__sprites_morcego_movendo[self.__sprite_atual_index]
#         self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (29*2,17*2))

#         self.__rect = self.__sprite_atual.get_rect()
#         self.image = self.__sprite_atual

#         self.__movendo = True
#         self.__morto = False

#     @property
#     def rect(self):
#         return self.__rect

#     @rect.setter
#     def rect(self, rect):
#         self.__rect = rect

#     # pega as sprites e chama a funçao para colocar todas elas em uma lista
#     def popular_sprites(self):
#         self.__sprites_morcego_movendo, self.__sprites_morcego_morrendo = super().pegar_sprites()

#     # atualiza as sprites mudando elas
#     def update(self):
#         self.__sprite_atual_index += self.contantes.atualizar_sprite

#         if self.__movendo:
#             if self.__sprite_atual_index >= len(self.__sprites_morcego_movendo):
#                 self.__sprite_atual_index = 0
#             self.__sprite_atual = self.__sprites_morcego_movendo[int(self.__sprite_atual_index) - 1]

#         if self.__morto:
#             self.__movendo = False
#             if self.__sprite_atual_index >= len(self.__sprites_morcego_morrendo):
#                 self.__sprite_atual_index = 0
#                 self.__movendo = True
#             self.__sprite_atual = self.__sprites_morcego_morrendo[int(self.__sprite_atual_index) - 1]
            

#         self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (29*2,17*2))
#         self.__rect = self.__sprite_atual.get_rect()
#         self.image = self.__sprite_atual


# # HERANÇA de Animacao com uma especializaçao 
# class AnimacaoGolem(Animacao):

#     def __init__(self):
#         super().__init__(['versao_final/src/golem/','versao_final/src/death_golem/'])
#         self.__sprites_golem_movendo = []
#         self.__sprites_golem_morrendo = []

#         self.popular_sprites()

#         self.__sprite_atual_index = 0
#         self.__sprite_atual = self.__sprites_golem_movendo[self.__sprite_atual_index]
#         self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (34*2,38*2))

#         self.__rect = self.__sprite_atual.get_rect()
#         self.image = self.__sprite_atual

#         self.__movendo = True
#         self.__morto = False

#     # Guetters e setters
#     @property
#     def rect(self):
#         return self.__rect

#     @rect.setter
#     def rect(self, rect):
#         self.__rect = rect

#     # pega as sprites e chama a funçao para colocar todas elas em uma lista
#     def popular_sprites(self):
#         self.__sprites_golem_movendo, self.__sprites_golem_morrendo = super().pegar_sprites()

#     # atualiza as sprites mudando elas
#     def update(self):
#         self.__sprite_atual_index += self.contantes.atualizar_sprite

#         if self.__movendo:
#             if self.__sprite_atual_index >= len(self.__sprites_golem_movendo):
#                 self.__sprite_atual_index = 0
#             self.__sprite_atual = self.__sprites_golem_movendo[int(self.__sprite_atual_index) - 1]

#         if self.__morto:
#             self.__movendo = False
#             if self.__sprite_atual_index >= len(self.__sprites_golem_morrendo):
#                 self.__sprite_atual_index = 0
#                 self.__movendo = True
#             self.__sprite_atual = self.__sprites_morcego_morrendo[int(self.__sprite_atual_index) - 1]

#         self.__sprite_atual = pygame.transform.scale(self.__sprite_atual, (34*2,38*2))
#         self.__rect = self.__sprite_atual.get_rect()
#         self.image = self.__sprite_atual

# # HERANÇA de Animacao com especializacao
# class AnimacaoFundo(Animacao):

#     def __init__(self, path: str, posicao_inicial: list):
#         super().__init__(path)
#         self.__sprite_fundo = []
#         self.popular_sprites()

#         self.image = self.__sprite_fundo[0]
#         self.rect = self.image.get_rect()
#         self.rect.topleft = posicao_inicial

#         self.jogando = True

#     # pega as sprites e chama a funçao para colocar todas elas em uma lista
#     def popular_sprites(self):
#         self.__sprite_fundo = super().pegar_sprites()

#     def update(self):
#         pass

# Classe de sprites que nao possuem alteração de imagens (sem animação, só uma imagem)
class Estatico(pygame.sprite.Sprite):
    def __init__(self, posicao, sprite_path, escala=1, escalar=False):
        pygame.sprite.Sprite.__init__(self)
        self.posicao = posicao
        self.imagem = pygame.image.load(sprite_path)

        if escalar:
            self.imagem = pygame.transform.scale(self.imagem, (17*escala,17*escala))

        self.image = self.imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = [self.posicao[0], self.posicao[1]]


# HERANÇA de Animacao com especializacao
class EstaticoFundo(Estatico):

    def __init__(self, posicao: list, path: str):
        super().__init__(posicao, path)


# HERANÇA de Estatico com especializaçao das sprites de quantidade de vida
class EstaticoCoracao(Estatico):

    def __init__(self, posicao):
        super().__init__(posicao, 'versao_final/src/estaticos/coracao.png', 2, True)


# HERANÇA de Estatico especializaçao das sprites dos poderes (poçoes)
class EstaticoPoder(Estatico):

    def __init__(self, posicao, path):
        super().__init__(posicao, path, 1, True)


# Classe de sprites que nao possuem movimento
# class Estatico(pygame.sprite.Sprite):
#     def __init__(self, posicao, sprite_path, escala):
#         pygame.sprite.Sprite.__init__(self)
#         self.posicao = posicao
#         self.imagem = pygame.image.load(sprite_path)
#         self.imagem = pygame.transform.scale(self.imagem, (17*escala,17*escala))
#         self.image = self.imagem
#         self.rect = self.imagem.get_rect()
#         self.rect.topleft = [self.posicao[0], self.posicao[1]]

# # HERANÇA de Estaico com especializaçao das sprites de quantidade de vida
# class EstaticoCoracao(Estatico):

#     def __init__(self, posicao):
#         super().__init__(posicao, 'versao_final/src/estaticos/coracao.png', 2)

# # HERANÇA de Estatico especializaçao das sprites dos poderes (poçoes)
# class EstaticoPoder(Estatico):

#     def __init__(self, posicao, path):
#         super().__init__(posicao, path, 1)
