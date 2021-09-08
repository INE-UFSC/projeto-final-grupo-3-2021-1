from singleton import Singleton
import pygame


class Constantes(Singleton):
    def __init__(self):
        super().__init__()
        self.limite_esquerda = 0
        self.limite_direita = 908
        self.limite_chao = 394
        self.velocidade_queda = 0.05
        self.velocidade = 10
        self.vermelho = (255, 0, 0)
        self.azul = (0, 0, 255)
        self.font = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 32)
        
        