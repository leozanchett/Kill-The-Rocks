from pathlib import Path
from random import random

import pygame


class Shot(pygame.sprite.Sprite):
    diretorioImg = 'images'
    def __init__(self, *groups):
        super(Shot, self).__init__(*groups)
        self.image = pygame.image.load(self.spriteasteroid())
        # redimensiona a imagem.
        self.image = pygame.transform.scale(self.image, [100, 10])
        self.rect = self.image.get_rect()
        # self.ataqueSom = pygame.mixer.Sound(self.carregaataque())
        self.speed = 10

    def update(self, *args, **kwargs) -> None:
        self.rect.x += self.speed
        if self.rect.right > 900:
            self.kill()

    def __del__(self):
        print(f'{self.__class__.__name__} foi deletado')

    @classmethod
    def atira(cls, _aobjectgroup, _aasteroidgroup):
        return cls(_aobjectgroup, _aasteroidgroup)

    @classmethod
    def spriteasteroid(cls):
        return Path().cwd().as_posix() + '/' + cls.diretorioImg + '/shot.png'