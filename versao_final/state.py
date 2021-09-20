from abc import ABC, abstractmethod
from tela import tela
import pygame
import sys


class State(ABC):

    def __init__(self, sistema, fundo, musica):
        self._sistema = sistema
        self.__setup(fundo, musica)

    def __setup(self, fundo, musica):
        try:
            self._sistema.fundo_atual = pygame.image.load(fundo)
        except TypeError:
            self._sistema.fundo_atual = None

        self._sistema.musica_atual = musica

    @property
    def sistema(self):
        return self._sistema

    @sistema.setter
    def sistema(self, sistema):
        self._sistema = sistema

    @abstractmethod
    def executar(self):
        pass


class Menu(State):

    def __init__(self, sistema,
                        fundo="versao_final/src/backgrounds/tela_inicial.png",
                        musica='versao_final/src/musicas/menu.mp3'):

        super().__init__(sistema, fundo, musica)
        self.sistema.tocar_musica(loop=True)

        self.button_jogar = pygame.Rect(40, 180, 374 , 94)
        self.button_ranking = pygame.Rect(40, 280, 374 , 94)
        self.button_sair = pygame.Rect(40, 380, 374 , 94)


    def executar(self):
        self.sistema.desenhar_fundo()
        mx, my = pygame.mouse.get_pos()
        proximo_estado = None

        if self.sistema.click:
            for bttn in [self.button_jogar, self.button_ranking, self.button_sair]:
                if bttn.collidepoint((mx, my)):
                    if bttn == self.button_jogar: 
                        proximo_estado = Jogando(self.sistema)
                    elif bttn == self.button_ranking:
                        proximo_estado = Ranking(self.sistema)
                    elif bttn == self.button_sair:
                        self.sistema.sair()

        if proximo_estado != None:
            self.sistema.proximo_estado(proximo_estado)


class Jogando(State):

    def __init__(self, sistema,
                        fundo=None,
                        musica='versao_final/src/musicas/jogo.mp3'):

        super().__init__(sistema, fundo, musica)
        self.sistema.tocar_musica(loop=True)


    def executar(self):
        self.sistema.jogo.atualizar(self.sistema.dt)

        if self.sistema.jogo.jogador.vida <= 0:
            self.sistema.proximo_estado(Final(self.sistema))


class Ranking(State):

    def __init__(self, sistema,
                        fundo="versao_final/src/backgrounds/tela_ranking.png",
                        musica=None):

        super().__init__(sistema, fundo, musica)
        self.sistema.atualizar_posicoes()

        self.font = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 20)
        self.texto_ranks = [self.font.render(f"{i+1} - {self.sistema.ranking[i][0]}:"+"{:.1f}".format(self.sistema.ranking[i][1]), True, pygame.Color('white')) for i in range(len(self.sistema.ranking))]
        self.button_voltar = pygame.Rect(20, 500, 224 , 74)


    def executar(self):
        self.sistema.desenhar_fundo()
        mx, my = pygame.mouse.get_pos()

        posicao_y = 170
        for text in self.texto_ranks:
            tela.screen.blit(text, (310, posicao_y))
            posicao_y += 30

        if self.sistema.click and self.button_voltar.collidepoint((mx, my)):
            self.sistema.proximo_estado(Menu(self.sistema))


class Final(State):

    def __init__(self, sistema,
                        fundo="versao_final/src/backgrounds/tela_final.png",
                        musica='versao_final/src/musicas/game_over.mp3'):

        super().__init__(sistema, fundo, musica)
        self.sistema.tocar_musica()

        self.font = pygame.font.Font('versao_final/src/fonte/pressstart.ttf', 16)
        self.button_salvar = pygame.Rect(705, 510, 210, 74)
        self.input_box = pygame.Rect(500, 172, 274, 40)

        self.color_inactive = pygame.Color('white')
        self.color_active = pygame.Color('gray')
        self.color = self.color_inactive

        self.active = False
        self.nome = ''


    def executar(self):
        self.sistema.desenhar_fundo()
        mx, my = pygame.mouse.get_pos()

        if self.sistema.click:
            # Toggle the active variable.
            self.active = self.input_box.collidepoint((mx, my))

        if self.active:
            for event in self.sistema.eventos:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.nome = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.nome = self.nome[:-1]
                    else:
                        self.nome += event.unicode


        if self.button_salvar.collidepoint((mx, my)):
            if self.sistema.click:
                self.sistema.salvar(self.nome)

                self.sistema.reiniciar_jogo()
                self.sistema.proximo_estado(Menu(self.sistema))


        # muda a cor
        self.color = self.color_active if self.active else self.color_inactive

        # renderiza texto
        txt_surface = self.font.render(self.nome, True, self.color)
        txt_pontuacao = self.font.render("{:.1f}".format(self.sistema.jogo.pontuacao), True, pygame.Color("white"))

        # desenha
        tela.screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+10))
        tela.screen.blit(txt_pontuacao, (400, 238))
        pygame.draw.rect(tela.screen, self.color, self.input_box, 2)

