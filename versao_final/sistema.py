from jogo import Jogo
from tela import tela
from singleton import Singleton
from DAO.pontuacoesDAO import PontuacoesDAO
from state import State
import pygame
import sys, time
import pygame
from pygame import mixer


# HERANÇA do Singleton
class Sistema(Singleton):

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(500, 100)

        self.__jogo = Jogo()                        # objeto do jogo
        self.__pontuacoes_dao = PontuacoesDAO()     # DAO das pontuacoes
        self.__ranking = {}                         # ranking das pontuacoes

        self.__estado = None                        # estado da janela
        self.__click = False                        # interação do usuário com a janela
        self.__fundo_atual = None
        self.__clock = pygame.time.Clock()

        self.menu()


    @property
    def estado_jogo(self):
        return self.__estado

    @estado_jogo.setter
    def estado_jogo(self, novo_estado):
        self.__estado = novo_estado

    # A SER IMPLEMENTADO AINDA
    def proximo_estado(self, estado: State):
        self.__estado = estado


    # Atualiza as posiçoes do ranking organizando do maior para o menor
    def atualizar_posicoes(self):
        ordenar_ranking = lambda item: item[1]
        self.__ranking = self.__pontuacoes_dao.get_all()
        self.__ranking = sorted(self.__ranking, key=ordenar_ranking, reverse=True)


    # salva a pontuacao
    def salvar(self, nome: str, pontuacao: float):
        self.__pontuacoes_dao.add(nome, pontuacao)
        self.atualizar_posicoes()


    # desenha o atual fundo em cada seção do menu
    def desenhar_fundo(self):
        tela.screen.blit(self.__fundo_atual, self.__fundo_atual.get_rect())


    # atualiza o display da janela
    def atualizar_tela(self):
        pygame.display.update()
        tela.screen.fill((0, 0, 0))


    # eventos de input do usuário
    def checar_eventos(self):
        self.__eventos = pygame.event.get()
        for event in self.__eventos:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.__click = True
            else:
                self.__click = False


    # Estado de jogo 
    def jogando(self):
        self.__estado = "jogando"
        tempo_inicial = time.time()

        mixer.init()
        mixer.music.load('versao_final/src/musicas/jogo.mp3')
        mixer.music.play(-1)
                    
        while self.__estado == "jogando":

            # delta time é o tempo de um frame
            tempo_final = time.time()
            dt = tempo_final - tempo_inicial
            tempo_inicial = tempo_final

            self.__clock.tick(300)
            self.__jogo.atualizar(dt)
            
            if self.__jogo.final:
                self.final()
            
            self.checar_eventos()
            self.atualizar_tela()
            
    # Estado de seleçao (menu)   
    def menu(self):
        self.__estado = "menu"
        self.__fundo_atual = pygame.image.load("versao_final/src/backgrounds/tela_inicial.png")

        mixer.init()
        mixer.music.load('versao_final/src/musicas/menu.mp3')
        mixer.music.play(-1)

        while self.__estado == "menu":
            mx, my = pygame.mouse.get_pos()

            button_jogar = pygame.Rect(40, 180, 374 , 94)
            button_ranking = pygame.Rect(40, 280, 374 , 94)
            button_sair = pygame.Rect(40, 380, 374 , 94)
            
            if self.__click:
                for bttn in [button_jogar, button_ranking, button_sair]:
                    if bttn.collidepoint((mx, my)):
                        if bttn == button_jogar: 
                            self.jogando()
                        elif bttn == button_ranking:
                            self.ranking()
                        elif bttn == button_sair:
                            sys.exit()
            
            self.checar_eventos()
            self.desenhar_fundo()
            self.atualizar_tela()
            
    # Tela do ranking
    def ranking(self):
        self.__estado = "ranking"
        self.__fundo_atual = pygame.image.load("versao_final/src/backgrounds/tela_ranking.png")
        self.atualizar_posicoes()

        font = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 20)
        texto_ranks = [font.render(f"{i+1} - {self.__ranking[i][0]}:"+"{:.1f}".format(self.__ranking[i][1]), True, pygame.Color('white')) for i in range(len(self.__ranking))]
        button_voltar = pygame.Rect(20, 500, 224 , 74)


        while self.__estado == "ranking":
            self.desenhar_fundo()
            mx, my = pygame.mouse.get_pos()

            posicao_y = 170
            for text in texto_ranks:
                tela.screen.blit(text, (310, posicao_y))
                posicao_y += 30

            if self.__click and button_voltar.collidepoint((mx, my)):
                self.menu()
            
            self.checar_eventos()
            self.atualizar_tela()

    # Tela após perder o jogo
    def final(self):
        self.__estado = "final"
        self.__fundo_atual = pygame.image.load("versao_final/src/backgrounds/tela_final.png")

        mixer.init()
        mixer.music.load('versao_final/src/musicas/game_over.mp3')
        mixer.music.play()

        font = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 16)
        button_salvar = pygame.Rect(705, 510, 210, 74)
        input_box = pygame.Rect(500, 172, 274, 40)
        color_inactive = pygame.Color('white')
        color_active = pygame.Color('gray')
        color = color_inactive


        active = False
        text = ''
        
        while self.__estado == "final":
            mx, my = pygame.mouse.get_pos()

            self.checar_eventos()

            if self.__click:
                # Toggle the active variable.
                active = input_box.collidepoint((mx, my))

            if active:
                for event in self.__eventos:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode


            if button_salvar.collidepoint((mx, my)):
                if self.__click:
                    self.salvar(text, self.__jogo.pontuacao)

                    del self.__jogo
                    self.__jogo = Jogo()
                    self.menu()

            self.desenhar_fundo()

            # muda a cor
            color = color_active if active else color_inactive
            txt_surface = font.render(text, True, color)
            txt_pontuacao = font.render("{:.1f}".format(self.__jogo.pontuacao), True, pygame.Color("white"))
            tela.screen.blit(txt_surface, (input_box.x+5, input_box.y+10))
            tela.screen.blit(txt_pontuacao, (400, 238))
            pygame.draw.rect(tela.screen, color, input_box, 2)
            
            self.atualizar_tela()
