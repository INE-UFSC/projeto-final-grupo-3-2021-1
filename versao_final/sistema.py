from jogo import Jogo
from jogador import Jogador
from tela import tela
from cenario import Cenario
from obstaculo import Obstaculo
from singleton import Singleton
from DAO.rankingDAO import RankingDAO
import pygame
import sys, time
import pygame


""" to do list:
        - mover toda a lógica de desenho e apresentação de informações para a view
        - achar um jeito melhor para fazer a lógica de estados (código muito repetitivo)
        ✓ - ajeitar botões
        ✓ - desenho dos backgrounds
"""


class Sistema(Singleton):

    def __init__(self):
        pygame.init()
        self.__estado_jogo = None     # a ser implementado com o menu
        self.__ranking_dao = RankingDAO()
        self.__ranking = {}
        self.__jogo = Jogo()

        self.__click = False
        self.__fundo_atual = None
        self.__clock = pygame.time.Clock()

        self.menu()


    @property
    def recorde(self):
        return self.__recorde   # VERIFICAR DEPOIS ESTA IMPLEMENTAÇÃO

    @property
    def estado_jogo(self):
        return self.__estado_jogo

    @estado_jogo.setter
    def estado_jogo(self, novo_estado):
        self.__estado_jogo = novo_estado
        
    @recorde.setter
    def recorde(self, novo_recorde):
        self.__recorde = novo_recorde

    # salva a pontuacao
    def salvar(self):
        pass


    # desenha o atual fundo em cada seção do menu
    def desenhar_fundo(self):
        tela.screen.blit(self.__fundo_atual, self.__fundo_atual.get_rect())

    # atualiza o display da janela
    def atualizar_tela(self):
        pygame.display.update()
        tela.screen.fill((0, 0, 0))

    # eventos de input do usuário
    def checar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.__click = True
            else:
                self.__click = False

    # estado 
    def jogando(self):
        self.__estado_jogo = "jogando"
        tempo_inicial = time.time()
            
        while self.__estado_jogo == "jogando":

            # delta time é o tempo de um frame
            tempo_final = time.time()
            dt = tempo_final - tempo_inicial
            tempo_inicial = tempo_final

            self.__clock.tick(300)
            self.__jogo.atualizar(dt)
            
            if self.__jogo.final:
                print("morreu")
                self.final()
            
            self.checar_eventos()
            self.atualizar_tela()
            
            
    def menu(self):
        self.__estado_jogo = "menu"
        self.__fundo_atual = pygame.image.load("versao_final/src/backgrounds/tela_inicial.png")

        while self.__estado_jogo == "menu":
            mx, my = pygame.mouse.get_pos()

            button_jogar = pygame.Rect(40, 180, 374 , 94)
            button_ranking = pygame.Rect(40, 280, 374 , 94)
            button_sair = pygame.Rect(40, 380, 374 , 94)
            
            if button_jogar.collidepoint((mx, my)):
                if self.__click:
                    self.jogando()
            
            if button_ranking.collidepoint((mx, my)):
                if self.__click:
                    self.ranking()
            
            if button_sair.collidepoint((mx, my)):
                if self.__click:
                    sys.exit()

            
            self.__clock.tick(300)

            self.checar_eventos()
            self.desenhar_fundo()
            self.atualizar_tela()
            
    
    def ranking(self):
        self.__estado_jogo = "ranking"
        self.__fundo_atual = pygame.image.load("versao_final/src/backgrounds/tela_ranking.png")

        while self.__estado_jogo == "ranking":
            mx, my = pygame.mouse.get_pos()

            button_voltar = pygame.Rect(20, 500, 224 , 74)
            
            if button_voltar.collidepoint((mx, my)):
                if self.__click:
                    self.menu()
            
            self.__clock.tick(300)

            self.checar_eventos()
            self.desenhar_fundo()
            self.atualizar_tela()

    def final(self):
        self.__estado_jogo = "final"
        self.__fundo_atual = pygame.image.load("versao_final/src/backgrounds/tela_final.png")

        font = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 16)
        button_salvar = pygame.Rect(705, 510, 210, 74)
        input_box = pygame.Rect(550, 172, 274, 40)
        color_inactive = pygame.Color('white')
        color_active = pygame.Color('gray')
        color = color_inactive
        active = False
        text = ''
        
        while self.__estado_jogo == "final":
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.__click = True
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            # print(text)
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                
                if button_salvar.collidepoint((mx, my)):
                    if self.__click:
                        del self.__jogo
                        self.__jogo = Jogo()
                        print(self.__jogo.final)
                        self.menu()
                        """implementar self.salvar() para atualizar ranking"""

            self.desenhar_fundo()

            txt_surface = font.render(text, True, color)
            txt_pontuacao = font.render("{:.1f}".format(self.__jogo.pontuacao), True, pygame.Color("white"))
            tela.screen.blit(txt_surface, (input_box.x+5, input_box.y+10))
            tela.screen.blit(txt_pontuacao, (450, 238))
            pygame.draw.rect(tela.screen, color, input_box, 2)
            
            self.checar_eventos()
            self.atualizar_tela()
