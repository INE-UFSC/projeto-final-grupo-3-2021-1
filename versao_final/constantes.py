from singleton import Singleton
import pygame

# constantes globais
class Constantes(Singleton):
    def __init__(self):
        super().__init__()
        self.limite_esquerda = 0
        self.limite_direita = 908
        self.limite_chao = 420
        self.velocidade_queda = 0.06
        self.velocidade = 10
        self.atualizar_sprite = 0.030
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
