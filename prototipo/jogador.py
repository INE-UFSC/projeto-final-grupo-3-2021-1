from personagem import Personagem
import pygame
from time import time
from tela import tela


class Jogador(Personagem):

    def __init__(self): # executado uma vez apenas, definindo os atributos
        super().__init__(vida= 3, vida_maxima= 3, velocidade= 400, posicao= [10,484])
        self.__poder_atual = None
        self.__cor = (255, 0, 0)
        self.__pulando = False
        self.__velocidade_y = 10
        self.__retangulo = pygame.Rect(self.posicao[0], self.posicao[1], 20,50)
        self.__invulneravel = False
        self.__cooldown_inv = 500
        self.__tempo_inicial_inv = None
        self.__vidas = [pygame.Rect(10, 10, 30, 30),
                        pygame.Rect(50, 10, 30, 30),
                        pygame.Rect(90, 10, 30, 30)]


    @property
    def retangulo(self):
        return self.__retangulo

    @property
    def invulneravel(self):
        return self.__invulneravel

    @property
    def tempo_inicial_inv(self):
        return self.__tempo_inicial_inv

    @property
    def vidas(self):
        return self.__vidas

    @tempo_inicial_inv.setter
    def tempo_inicial_inv(self, novo):
        self.__tempo_inicial_inv = novo

    @invulneravel.setter
    def invulneravel(self, novo: bool):
        self.__invulneravel = novo

    @vidas.setter
    def vidas(self, novo: int):
        self.__vidas = novo


    # Permite movimentos ao jogador
    def movimento(self, dt):
        botoes = pygame.key.get_pressed()

        # movimento eixo x
        if botoes[pygame.K_LEFT]:                       # movimento para a esquerda
            self.posicao[0] -= self.velocidade * dt
            if self.posicao[0] < 0:
                self.posicao[0] = 0
        if botoes[pygame.K_RIGHT]:                      # movimento para a direita
            self.posicao[0] += self.velocidade * dt
            if self.posicao[0] > 908:
                self.posicao[0] = 908

        # movimento eixo y
        if self.__pulando is False and botoes[pygame.K_UP]:
            self.__pulando = True

        if self.__pulando:
            self.posicao[1] -= self.__velocidade_y*90 * dt  # tamanho do pulo
            self.__velocidade_y -= 0.040                    # velocidade que o jogador cai

            if self.posicao[1] >= 484:                       # checa a colisão com o chão
                self.posicao[1] = 484
                self.__pulando = False
                self.__velocidade_y = 10


    def eventos(self):
        # evento da invulnerabilidade
        if self.__invulneravel:
            self.__cor = (0, 0, 255)

            agora = pygame.time.get_ticks()
            if agora - self.__tempo_inicial_inv >= self.__cooldown_inv:
                self.__invulneravel = False
                self.__cor = (255, 0, 0)
                print("Pronto pra outra")


    # Usar poder: Permite que o personagem do jogador ultiliza um poder da classe poder
    def usar_poder(self):
        pass


    def desenhar(self):
        # desenho das vidas (corações)
        for vida_index in range(self.vida):
            pygame.draw.rect(tela.screen, (255, 0, 0), self.__vidas[vida_index])

        # Desenho do jogador
        pygame.draw.rect(tela.screen, self.__cor, self.__retangulo)    # jogador
        self.__retangulo = pygame.Rect(self.posicao[0], self.posicao[1], 20,50)


    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt)
        self.eventos()
