from singleton import Singleton


class Constantes(Singleton):
    def __init__(self):
        super().__init__()
        self.limite_esquerda = 0
        self.limite_direita = 908
        self.limite_chao = 484
        self.velocidade_queda = 0.05
        self.velocidade = 10
        self.vermelho = (255, 0, 0)
        self.azul = (0, 0, 255)
        
        