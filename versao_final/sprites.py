import pygame


class Sprites(pygame.sprite.Sprite):
    animacao_jogador_movendo = [pygame.image.load('SPRITES/Cavaleiro/cavaleiro_movimento1.png'),
                                pygame.image.load('SPRITES/Cavaleiro/cavaleiro_movimento2.png'),
                                pygame.image.load('SPRITES/Cavaleiro/cavaleiro_movimento3.png'),
                                pygame.image.load('SPRITES/Cavaleiro/cavaleiro_movimento4.png'),
                                pygame.image.load('SPRITES/Cavaleiro/cavaleiro_movimento5.png'),
                                pygame.image.load('SPRITES/Cavaleiro/cavaleiro_movimento6.png'),
                                pygame.image.load('SPRITES/Cavaleiro/cavaleiro_movimento7.png'),
                                pygame.image.load('SPRITES/Cavaleiro/cavaleiro_movimento8.png')]

    animacao_golem = [pygame.image.load('SPRITES/Golem/golem1'),
                        pygame.image.load('SPRITES/Golem/golem2'),
                        pygame.image.load('SPRITES/Golem/golem3'),
                        pygame.image.load('SPRITES/Golem/golem4'),
                        pygame.image.load('SPRITES/Golem/golem5'),
                        pygame.image.load('SPRITES/Golem/golem6'),
                        pygame.image.load('SPRITES/Golem/golem7'),
                        pygame.image.load('SPRITES/Golem/golem8')]

    animacao_morcego = [pygame.image.load('SPRITES/Morcego/morcego_movimento_1'),
                        pygame.image.load('SPRITES/Morcego/morcego_movimento_1'),
                        pygame.image.load('SPRITES/Morcego/morcego_movimento_1'),
                        pygame.image.load('SPRITES/Morcego/morcego_movimento_1'),
                        pygame.image.load('SPRITES/Morcego/morcego_movimento_1'),
                        pygame.image.load('SPRITES/Morcego/morcego_movimento_1'),
                        pygame.image.load('SPRITES/Morcego/morcego_movimento_1'),
                        pygame.image.load('SPRITES/Morcego/morcego_movimento_1')]
    
    sprite_coracao = []

imagens = Sprites()
        