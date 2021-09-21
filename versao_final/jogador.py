from pygame import surface
from pygame.surfarray import blit_array
from personagem import Personagem
import pygame
from tela import tela
from constantes import Constantes
from animacao import AnimacaoCavaleiro

# HERANÇA de personagem com especializaçao
class Jogador(Personagem):

    def __init__(self):
        super().__init__(vida=3, vida_maxima=3, velocidade=400, posicao=[10,420])
        self.constantes = Constantes()
        self.__animacao = pygame.sprite.Group(AnimacaoCavaleiro())
        self.__tamanho_pulo = 55
        self.__velocidade_y = 10

        self.__pulando = False
        
        #self.__imagem = cavaleiro.animacao_jogador_movendo[cavaleiro.imagem_atual]
        self.__rect = self.__animacao.sprites()[0].rect


    @property
    def rect(self):
        return self.__rect


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
            pulo = pygame.mixer.Sound('versao_final/src/efeitos_sonoros/pulo.wav')
            pulo.play()
            self.__pulando = True
        if self.__pulando:
            self.posicao[1] -= self.__velocidade_y*self.__tamanho_pulo * dt  # tamanho do pulo
            self.__velocidade_y -= self.constantes.velocidade_queda          # velocidade que o jogador cai
            
            # checa a colisão com o chão
            if self.posicao[1] >= self.constantes.limite_chao: 
                self.posicao[1] = self.constantes.limite_chao
                self.__velocidade_y = self.constantes.velocidade
                self.__pulando = False
        

    # eventos do jogador
    def eventos(self, dt):
        # aciona timer e oscila desenho se jogador está invulnerável
        if self.invulneravel:            
            self.mostrar = not self.mostrar
            
            if pygame.time.get_ticks() - self.tempo_inicial_inv >= self.tempo_inv:
                self.invulneravel = False
                self.mostrar = True


    # movimentos do jogador
    def movimento(self, dt):
        botoes = pygame.key.get_pressed()
        self.movimento_direita(dt, botoes[pygame.K_RIGHT])
        self.movimento_esquerda(dt, botoes[pygame.K_LEFT])
        self.movimento_pulo(dt, botoes[pygame.K_UP])


    # desenha o jogador
    def desenhar(self):
        self.__animacao.sprites()[0].rect.topleft = self.posicao
        self.__rect = self.__animacao.sprites()[0].rect

        if self.mostrar:
            self.__animacao.draw(tela.screen)
        
        self.__animacao.update(self.__pulando)


    # Função de loop do jogador que entra no loop do jogo
    def atualizar(self, dt):
        self.movimento(dt)
        self.desenhar()
        self.eventos(dt)

