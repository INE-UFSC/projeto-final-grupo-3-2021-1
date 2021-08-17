import pygame
from tela import tela


class Obstaculo():

    def __init__(self, tipo: str, posicao: list, velocidade: int, tamanho: list):
        self.__tipo = tipo
        self.posicao_obstaculo = posicao
        self.__velocidade = velocidade
        self.__tamanho = tamanho
        self.__retangulo = pygame.Rect(self.posicao_obstaculo[0], self.posicao_obstaculo[1], self.__tamanho[0], self.__tamanho[1])
        self.__cor = (0, 255, 0)

    def desenhar(self):
        pygame.draw.rect(tela.screen, self.__cor, self.__retangulo)
        self.__retangulo = pygame.Rect(self.posicao_obstaculo[0], self.posicao_obstaculo[1], self.__tamanho[0], self.__tamanho[1])

    def checar_colisao(self, jogador):
        if self.__retangulo.colliderect(jogador.retangulo) and jogador.invulneravel is False:
            jogador.invulneravel = True
            jogador.tempo_inicial_inv = pygame.time.get_ticks()

            # perde uma vida e deixa de desenhar um coração na tela
            jogador.vida -= 1
            print(jogador.vida)

    def movimento(self, dt, aparecer):
       self.posicao_obstaculo[0] -= self.__velocidade * dt
       if self.posicao_obstaculo[0] <= -40:
           self.posicao_obstaculo[0] = aparecer
           self.__velocidade += 10

    def atualizar(self, dt, jogador):
        self.desenhar()
        self.movimento(dt, 1128)
        self.movimento(dt, 1328)     # movimento do obstaculo
        self.checar_colisao(jogador)
