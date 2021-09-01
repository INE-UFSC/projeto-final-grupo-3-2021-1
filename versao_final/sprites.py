import pygame
import os


class SpritesCavaleiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animacao_jogador_movendo = []
        self.animacao_jogador_movendo.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cav1.png')))
        self.animacao_jogador_movendo.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cav2.png')))
        self.animacao_jogador_movendo.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cav3.png')))
        self.animacao_jogador_movendo.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cav4.png')))
        self.animacao_jogador_movendo.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cav5.png')))
        self.animacao_jogador_movendo.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cav6.png')))
        self.animacao_jogador_movendo.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cav7.png')))
        self.animacao_jogador_movendo.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cav8.png')))


        self.animacao_jogador_pulando = []
        self.animacao_jogador_pulando.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cavpulo1.png')))
        self.animacao_jogador_pulando.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cavpulo2.png')))
        self.animacao_jogador_pulando.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cavpulo3.png')))
        self.animacao_jogador_pulando.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cavpulo4.png')))
        self.animacao_jogador_pulando.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cavpulo5.png')))
        self.animacao_jogador_pulando.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cavpulo6.png')))
        self.animacao_jogador_pulando.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cavpulo7.png')))
        self.animacao_jogador_pulando.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cavpulo8.png')))
        self.animacao_jogador_pulando.append(pygame.image.load(os.path.join('SPRITES','cavaleiro','cavpulo9.png')))

        self.movendo = True
        self.pulando = False

        self.imagem_atual = 0
        self.image = self.animacao_jogador_movendo[self.imagem_atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]

        self.image = pygame.transform.scale(self.image, (26*2,29*2))


    def update(self):
        if self.movendo:
            self.imagem_atual += 0.020
            if self.imagem_atual >= len(self.animacao_jogador_movendo):
                self.imagem_atual = 0
            self.image = self.animacao_jogador_movendo[int(self.imagem_atual) - 1]

        if self.pulando:
            self.movendo = False
            self.imagem_atual += 0.020
            if self.imagem_atual >= len(self.animacao_jogador_pulando):
                self.movendo = True
            self.image = self.animacao_jogador_pulando[int(self.imagem_atual) - 1]
        
        self.image = pygame.transform.scale(self.image, (26*2,29*2))
        print(self.rect.topleft)


todas_as_sprites = pygame.sprite.Group()
cavaleiro = SpritesCavaleiro()
todas_as_sprites.add(cavaleiro)


