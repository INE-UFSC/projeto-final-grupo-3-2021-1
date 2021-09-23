from singleton import Singleton
import pygame

# constantes globais
class Constantes(Singleton):
    def __init__(self):
        super().__init__()
        self.LIMITE_ESQUERDA = 0
        self.LIMITE_DIREITA = 908
        self.LIMITE_CHAO = 420
        self.VELOCIDADE_QUEDA = 0.06
        self.VELOCIDADE = 10
        
        # self.font = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 32)

# class ConstantesVisuais(Singleton):

#     def __init__(self):
#         super().__init__()
#         self.__carregar_fontes()
#         self.__carregar_imagens()

#     def __carregar_fontes(self):
#         self.FONTE_32 = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 32)
#         self.FONTE_20 = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 20)
#         self.FONTE_16 = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 16)

#     def __carregar_imagens(self):
#         self.FUNDO_FINAL = pygame.image.load("versao_final/src/backgrounds/tela_final.png")
#         self.FUNDO_MENU = pygame.image.load("versao_final/src/backgrounds/tela_inicial.png")
#         self.FUNDO_RANKING = pygame.image.load("versao_final/src/backgrounds/tela_ranking.png")
#         self.UNDO_JOGO = None
#         self.FUNDO_JOGO_INV = None
