import pygame
import abc
import os


constante = 0.030

class Animacao(pygame.sprite.Sprite):

    def __init__(self, velocidade, dimensao, path):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        try:
            self.__carregar_sprites(path)
        except FileNotFoundError as e:
            print(e)
        
        self.sprite_atual_index = 0
        self.velocidade_troca_sprite = velocidade

        self.sprite_atual = self.sprites[self.sprite_atual_index]
        self.rect = self.sprite_atual.get_rect()
        self.dimensao = dimensao

        self.sprite_atual = pygame.transform.scale(self.sprite_atual, (dimensao[0]*2, dimensao[1]*2))
        self.image = self.sprite_atual


    # carrega as sprites
    def __carregar_sprites(self, path):
        for nome_sprite in os.listdir(path):
            self.sprites.append(pygame.image.load(path + nome_sprite))


    # processa o sprite atual, alterando a escala, o rect e a imagem atual
    def processar_sprite(self):
        self.sprite_atual = pygame.transform.scale(self.sprite_atual, (self.dimensao[0]*2, self.dimensao[1]*2))
        self.rect = self.sprite_atual.get_rect()
        self.image = self.sprite_atual


    # troca de sprite com base na velocidade, retorna rect do sprite atual
    def atualizar_animacao(self):
        self.sprite_atual_index += constante

        if self.sprite_atual_index >= len(self.sprites):
            self.sprite_atual_index = 0

        self.sprite_atual = self.sprites[int(self.sprite_atual_index) - 1] 
        self.processar_sprite()


# grupo de animcoes do cavaleiro
class AnimacaoCavaleiro(pygame.sprite.Group):

    def __init__(self, velocidade: float, path_mov: str, path_pul: str):
        super().__init__()
        self.__animacao_movendo = Animacao(velocidade, (26, 29), path_mov)
        self.__animacao_pulando = Animacao(velocidade, (26, 29), path_pul)
        self.__anim_atual = None

    # deixa a animacao na mesma posicao do animado
    def acompanhar_posicao(self, pos):
        for anim in [self.__animacao_movendo, self.__animacao_pulando]:
            anim.rect.topleft = pos

        return self.__anim_atual.rect
        
    # lógica de animacao
    def update(self, pos, pulando):
        if pulando:
            self.__anim_atual = self.__animacao_pulando
            self.__animacao_pulando.atualizar_animacao()
        else:
            self.__anim_atual = self.__animacao_movendo
            self.__animacao_movendo.atualizar_animacao()


# HERANÇA de Animacao com uma especializaçao
class AnimacaoMorcego(pygame.sprite.Group):

    def __init__(self, velocidade: float, path: str):
        super().__init__()
        self.__animacao_voando = Animacao(velocidade, (29, 17), path)

    # deixa a animacao na mesma posicao do animado
    def acompanhar_posicao(self, pos):
        self.__animacao_voando.rect.topleft = pos
        return self.__animacao_voando.rect

    # lógica de animacao
    def update(self, pos):
        self.acompanhar_posicao(pos)
        return self.__animacao_voando.atualizar_animacao()


# HERANÇA de Animacao com uma especializaçao 
class AnimacaoGolem(pygame.sprite.Group):

    def __init__(self, velocidade: float, path: str):
        super().__init__()
        self.__animacao_movendo = Animacao(velocidade, (34, 38), path)

    # deixa a animacao na mesma posicao do animado
    def acompanhar_posicao(self, pos):
        self.__animacao_movendo.rect.topleft = pos
        return self.__animacao_movendo.rect


    # lógica de animacao
    def update(self, pos):
        self.acompanhar_posicao(pos)
        return self.__animacao_movendo.atualizar_animacao()
        


# Classe de sprites que nao possuem alteração de imagens (sem animação, só uma imagem)
class Estatico(pygame.sprite.Sprite):
    def __init__(self, posicao, sprite_path, escala=1, escalar=False):
        pygame.sprite.Sprite.__init__(self)
        self.posicao = posicao
        self.imagem = pygame.image.load(sprite_path)

        if escalar:
            self.imagem = pygame.transform.scale(self.imagem, (17*escala,17*escala))

        self.image = self.imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = [self.posicao[0], self.posicao[1]]


# HERANÇA de Animacao com especializacao
class EstaticoFundo(Estatico):

    def __init__(self, posicao: list, path: str):
        super().__init__(posicao, path)


# HERANÇA de Estatico com especializaçao das sprites de quantidade de vida
class EstaticoCoracao(Estatico):

    def __init__(self, posicao):
        super().__init__(posicao, 'versao_final/src/estaticos/coracao.png', 2, True)


# HERANÇA de Estatico especializaçao das sprites dos poderes (poçoes)
class EstaticoPoder(Estatico):

    def __init__(self, posicao, path):
        super().__init__(posicao, path, 1, True)
