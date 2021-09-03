from pygame import surface
from pygame.surfarray import blit_array
from personagem import Personagem
import pygame
from tela import tela
from constantes import Constantes
from animacao import todas_as_sprites
from animacao import cavaleiro


class Jogador(Personagem):

    def __init__(self):
        super().__init__(vida=3, vida_maxima=3, velocidade=400, posicao=[10,484])
        self.constantes = Constantes()
        self.__tamanho_pulo = 55
        self.__velocidade_y = 10
        self.__pulando = False

        self.__movendo = True 
        #self.__imagem = cavaleiro.animacao_jogador_movendo[cavaleiro.imagem_atual]
        self.__rect = cavaleiro.rect
        cavaleiro.rect.topleft = [self.posicao[0], self.posicao[1]]


    @property
    def rect(self):
        return self.__rect

    # @property
    # def desenho_vidas(self):
    #     return self.__desenho_vidas


    # movimento para a direita
    def movimento_direita(self, dt, seta_direita_pressionada):
        if seta_direita_pressionada:
            self.posicao[0] += self.velocidade * dt
            cavaleiro.rect.topleft = [self.posicao[0], self.posicao[1]]
            if self.posicao[0] > self.constantes.limite_direita:
                self.posicao[0] = self.constantes.limite_direita


    # movimento para a esquerda
    def movimento_esquerda(self, dt, seta_esquerda_pressionada):
        if seta_esquerda_pressionada: 
            self.posicao[0] -= self.velocidade * dt
            cavaleiro.rect.topleft = [self.posicao[0], self.posicao[1]]
            if self.posicao[0] < self.constantes.limite_esquerda:
                self.posicao[0] = self.constantes.limite_esquerda


    # movimento do pulo
    def movimento_pulo(self, dt, seta_cima_pressionada):
        if self.__pulando is False and seta_cima_pressionada:
            self.__pulando = True
            cavaleiro.pulando = True
        if self.__pulando:
            self.posicao[1] -= self.__velocidade_y*self.__tamanho_pulo * dt  # tamanho do pulo
            self.__velocidade_y -= self.constantes.velocidade_queda          # velocidade que o jogador cai
            
            # checa a colisão com o chão
            if self.posicao[1] >= self.constantes.limite_chao: 
                self.posicao[1] = self.constantes.limite_chao
                self.__pulando = False
                cavaleiro.pulando = False
                cavaleiro.movendo = True
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
        todas_as_sprites.draw(tela.screen)
        todas_as_sprites.update()


    # Função de loop do jogador que entra no loop do jogo
    def atualizar(self, dt):
        self.desenhar()
        self.movimento(dt)
        # self.animacao()
        self.eventos()
