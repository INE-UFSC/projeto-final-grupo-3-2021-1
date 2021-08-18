from personagem import Personagem
import pygame
from tela import tela


class Jogador(Personagem):

    def __init__(self):
        super().__init__(vida=3, vida_maxima=3, velocidade=400, posicao=[10,484])
        self.__tamanho_pulo = 55
        self.__pulando = False
        self.__velocidade_y = 10
        self.__retangulo = pygame.Rect(self.posicao[0], self.posicao[1], 20,50)
        self.__desenho_vidas = [pygame.Rect(800, 10, 30, 30),
                                pygame.Rect(840, 10, 30, 30),
                                pygame.Rect(880, 10, 30, 30)]


    @property
    def retangulo(self):
        return self.__retangulo

    @property
    def tamanho_pulo(self):
        return self.__tamanho_pulo

    @tamanho_pulo.setter
    def tamanho_pulo(self, novo):
        self.__tamanho_pulo = novo

    # movimentos do jogador
    def movimento(self, dt):

        botoes = pygame.key.get_pressed()

        # movimento para a esquerda
        if botoes[pygame.K_LEFT]: 
            self.posicao[0] -= self.velocidade * dt
            if self.posicao[0] < 0:
                self.posicao[0] = 0

        # movimento para a direita
        if botoes[pygame.K_RIGHT]:
            self.posicao[0] += self.velocidade * dt
            if self.posicao[0] > 908:
                self.posicao[0] = 908

        # movimento para cima
        if self.__pulando is False and botoes[pygame.K_UP]:
            self.__pulando = True
        if self.__pulando:
            self.posicao[1] -= self.__velocidade_y*self.__tamanho_pulo * dt         # tamanho do pulo
            self.__velocidade_y -= 0.05                                             # velocidade que o jogador cai
            
            # checa a colisão com o chão
            if self.posicao[1] >= 484: 
                self.posicao[1] = 484
                self.__pulando = False
                self.__velocidade_y = 10

    # eventos do jogador
    def eventos(self):
        
        # aciona timer se jogador está invulnerável
        if self.invulneravel:
            self.cor = (0, 0, 255)

            if pygame.time.get_ticks() - self.tempo_inicial_inv >= self.tempo_inv:
                self.invulneravel = False
                self.cor = (255, 0, 0)
            

    # desenha o jogador e a sua vida
    def desenhar(self):

        # desenho das vidas (corações)
        for vida_index in range(self.vida):
            pygame.draw.rect(tela.screen, (255, 0, 0), self.__desenho_vidas[vida_index])

        # Desenho do jogador
        pygame.draw.rect(tela.screen, self.cor, self.__retangulo)
        self.__retangulo = pygame.Rect(self.posicao[0], self.posicao[1], 20,50)

    # Função de loop do jogador que entra no loop do jogo
    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt)
        self.eventos()
