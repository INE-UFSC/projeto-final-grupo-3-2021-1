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
        # self.font = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 32)
