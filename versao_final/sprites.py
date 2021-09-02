import pygame
import os


"""
to do list (anthon):
    - Criar uma classe abstrata Animacao que funciona como um DAO para as sprites, para facilitar quando for implementar animações em obstaculos (q inclusive ja fecha com o princípio open-closed)
    - Instanciar classes provenientes da classe Animacao nas classes correspontes Ex.: AnimacaoCavaleiro() em Jogador
    - Manipular as classes filhas de Animacao dentro das classes correspondentes, facilita a leitura e o entendimento
    - organizar o projeto em arq. MVC
"""


class AnimacaoCavaleiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.__path = 'versao_final/src/cavaleiro/'
        self.__animacao_jogador_movendo = []
        self.__animacao_jogador_pulando = []
        self.popular_animacoes()

        self.movendo = True
        self.pulando = False

        self.imagem_atual = 0
        self.image = self.__animacao_jogador_movendo[self.imagem_atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]

        self.image = pygame.transform.scale(self.image, (26*2,29*2))
        

    def popular_animacoes(self):
        try:
            for sprite in os.listdir(self.__path):
                if sprite.startswith('movimento'):
                    self.__animacao_jogador_movendo.append(pygame.image.load(self.__path + sprite))

                elif sprite.startswith('pulo'):
                    self.__animacao_jogador_pulando.append(pygame.image.load(self.__path + sprite))

        except FileNotFoundError as e:
            print(e)


    def update(self):
        if self.movendo:
            self.imagem_atual += 0.020
            if self.imagem_atual >= len(self.__animacao_jogador_movendo):
                self.imagem_atual = 0
            self.image = self.__animacao_jogador_movendo[int(self.imagem_atual) - 1]

        if self.pulando:
            self.movendo = False
            self.imagem_atual += 0.020
            if self.imagem_atual >= len(self.__animacao_jogador_pulando):
                self.movendo = True
            self.image = self.__animacao_jogador_pulando[int(self.imagem_atual) - 1]
        
        self.image = pygame.transform.scale(self.image, (26*2,29*2))
        print(self.rect.topleft)


todas_as_sprites = pygame.sprite.Group()
cavaleiro = AnimacaoCavaleiro()
todas_as_sprites.add(cavaleiro)
