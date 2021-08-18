from jogo import Jogo
from jogador import Jogador
from tela import tela
from cenario import Cenario
from obstaculo import Obstaculo
import pygame
import sys, time


class Sistema:

    def __init__(self):
        pygame.init()
        tempo_inicial = time.time()

        self.__estado_jogo = "jogando"
        self.__recorde = 0
        self.__jogo = Jogo(jogador=Jogador(),
                            cenario=Cenario([Obstaculo("Golem", [928,484], 400, [20,50]),
                                            Obstaculo("Morcego", [1500,440], 465, [25,25])]),
                            inimigos=[]
                        )
        
        # loop da janela
        while True:
            # delta time é o tempo de um frame
            tempo_final = time.time()
            dt = tempo_final - tempo_inicial
            tempo_inicial = tempo_final
            

            # sai ao clicar no "x"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            
            tela.screen.fill((0, 0, 0))
            self.__jogo.atualizar(dt)
            pygame.display.update()

    def eventos(self):
        pass

    @property
    def recorde(self):
        return self.__recorde   # VERIFICAR DEPOIS ESTA IMPLEMENTAÇÃO
        
    @recorde.setter
    def recorde(self, novo_recorde):
        self.__recorde = novo_recorde
    
    def ver_recorde(self):
        pass    # MUDAR IMPLEMENTAÇÃO COM PYGAME
    
    #Define o estado do jogo
    def estado_jogo(self):
        pass    # MUDAR IMPLEMENTAÇÃO DEPOIS
