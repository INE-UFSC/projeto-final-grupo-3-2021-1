from jogo import Jogo
from jogador import Jogador
from tela import tela
from cenario import Cenario
from obstaculo import Obstaculo
from sistema import Sistema
import pygame
import sys, time


pygame.display.set_icon(pygame.image.load('imagens/icon.png'))
pygame.init()

tempo_inicial = time.time()
jogo = Jogo(
        jogador=Jogador(),
        cenario=Cenario(),
        inimigos=[],
        obstaculos=[Obstaculo("Golem", [928,484], 120, [20,50]),
                    Obstaculo("Morcego", [1500,440], 185, [25,25])]
    )
Jogador()

# loop do game
while True:
    # delta time
    tempo_final = time.time()
    dt = tempo_final - tempo_inicial
    tempo_inicial = tempo_final
    

    # sair
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    tela.screen.fill((0, 0, 0))
    jogo.atualizar_tela(dt)


# SISTEMA A SER IMPLEMENTADO
# if __name__ == '__main__':
#     Sistema()