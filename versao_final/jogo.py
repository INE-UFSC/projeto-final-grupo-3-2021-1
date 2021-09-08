from jogador import Jogador
from cenario import Cenario
from tela import tela
import pygame


class Jogo():

    def __init__(self, jogador: Jogador, cenario: Cenario, inimigos: list):
        self.__jogador = jogador            # objeto do jogador
        self.__inimigos = inimigos          # lista de objetos dos inimigos na tela
        self.__cenario = cenario            # objeto do cenário
        self.__pontuacao = 0                # pontuação atual do jogo

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador


    # checa as colisões entre obstaculos e poderes e o jogador
    def checar_colisao(self):

        # obstáculos
        for obs in self.__cenario.obstaculos:
            if self.__jogador.rect.colliderect(obs.retangulo) and self.__jogador.invulneravel is False:
                self.__jogador.tornar_invulneravel_por()

                # perde uma vida (tira 1 coraçao na tela)
                self.__jogador.vida -= 1

        # poder
        if self.__cenario.poder_na_tela != None:
            if self.__jogador.rect.colliderect(self.__cenario.poder_na_tela.retangulo):
                self.__cenario.poder_na_tela.usar(self.__jogador)
                self.__cenario.poder_na_tela = None


    # Pontua e mostra a pontuação com base no tempo de jogo e na velocidade dos obstaculos
    def pontuar(self, dt):

        self.__pontuacao += dt * (sum([obs.velocidade for obs in self.__cenario.obstaculos])) / 100

        # mostra na tela a pontuação
        font = pygame.font.Font(pygame.font.get_default_font(), 32)
        text_surface = font.render("{:.1f}".format(self.__pontuacao), True, (255, 255, 255))
        tela.screen.blit(text_surface, (10, 10))


    # desenho das vidas (corações)
    def desenhar_vidas(self):
        for vida_index in range(self.__jogador.vida):
            self.__cenario.coracoes[vida_index].draw(tela.screen)
            self.__cenario.coracoes[vida_index].update()
        #     pygame.draw.rect(tela.screen, (255, 0, 0), self.__jogador.desenho_vidas[vida_index])


    # Responsável por atualizar tudo dentro do jogo, AKA Update Function
    def atualizar(self, dt):
        if self.__jogador.vida > 0:
            self.__jogador.atualizar(dt)    # atualiza o jogador
            self.__cenario.atualizar(dt)    # atualiza cenário (obstaculos e poderes inclusos)
            self.checar_colisao()           # checa as colisões dos obstáculos e poderes com o jogador
            self.desenhar_vidas()           # desenha as vidas do jogador na tela, com base no número atual de vidas
            self.pontuar(dt)                # pontua jogo e imprime a pontuação
        else:
            font = pygame.font.Font(pygame.font.get_default_font(), 40)
            texto_ossos = font.render("OSSOS QUEBRADOS", True, (255, 255, 255))
            texto_perdeu = font.render("GAME OVER, {:.1f} Pontos".format(self.__pontuacao), True, (255, 255, 255))
            tela.screen.blit(texto_ossos,  (232, 200))
            tela.screen.blit(texto_perdeu,  (192, 300))
