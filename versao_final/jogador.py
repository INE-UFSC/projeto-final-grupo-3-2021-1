from personagem import Personagem
import pygame
from tela import tela
from constantes import Constantes


class Jogador(Personagem):

    def __init__(self):
        super().__init__(vida=3, vida_maxima=3, velocidade=400, posicao=[10,484])
        self.constantes = Constantes()
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


    # movimento para a direita
    def movimento_direita(self, dt, seta_direita_pressionada):
        if seta_direita_pressionada:
            self.posicao[0] += self.velocidade * dt
            if self.posicao[0] > self.constantes.limite_direita:
                self.posicao[0] = self.constantes.limite_direita


    # movimento para a esquerda
    def movimento_esquerda(self, dt, seta_esquerda_pressionada):
        if seta_esquerda_pressionada: 
            self.posicao[0] -= self.velocidade * dt
            if self.posicao[0] < self.constantes.limite_esquerda:
                self.posicao[0] = self.constantes.limite_esquerda


    # movimento do pulo
    def movimento_pulo(self, dt, seta_cima_pressionada):
        if self.__pulando is False and seta_cima_pressionada:
            self.__pulando = True
        if self.__pulando:
            self.posicao[1] -= self.__velocidade_y*self.__tamanho_pulo * dt  # tamanho do pulo
            self.__velocidade_y -= self.constantes.velocidade_queda          # velocidade que o jogador cai
            
            # checa a colisão com o chão
            if self.posicao[1] >= self.constantes.limite_chao: 
                self.posicao[1] = self.constantes.limite_chao
                self.__pulando = False
                self.__velocidade_y = self.constantes.velocidade
        

    # eventos do jogador
    def eventos(self):
        
        # aciona timer se jogador está invulnerável
        if self.invulneravel:
            self.cor = self.constantes.azul

            if pygame.time.get_ticks() - self.tempo_inicial_inv >= self.tempo_inv:
                self.invulneravel = False
                self.cor = self.constantes.vermelho


    # movimentos do jogador
    def movimento(self, dt):
        botoes = pygame.key.get_pressed()
        self.movimento_direita(dt, botoes[pygame.K_RIGHT])
        self.movimento_esquerda(dt, botoes[pygame.K_LEFT])
        self.movimento_pulo(dt, botoes[pygame.K_UP])


    # desenha o jogador
    def desenhar(self):
        pygame.draw.rect(tela.screen, self.cor, self.__retangulo)
        self.__retangulo = pygame.Rect(self.posicao[0], self.posicao[1], 20,50)


    # Função de loop do jogador que entra no loop do jogo
    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt)
        self.eventos()
