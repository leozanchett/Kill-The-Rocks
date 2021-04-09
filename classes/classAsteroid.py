from pathlib import Path

import random as random
import pygame as pygame


class Asteroid(pygame.sprite.Sprite):
    diretorioImg = 'images'

    def __init__(self, *groups):
        super(Asteroid, self).__init__(*groups)
        self.image = pygame.image.load(self.spriteasteroid())
        # redimensiona a imagem.
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(900, random.randint(15, 440), 100, 100)
        #self.ataqueSom = pygame.mixer.Sound(self.carregaataque())
        self.speed = random.randint(1, 5)

    def update(self, *args, **kwargs) -> None:
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

    def __del__(self):
        print(f'{self.__class__.__name__} foi deletado')

    @classmethod
    def verificanovoasteroide(cls, _aobjectgroup, _aasteroidgroup):
        if random.random() < 0.5:
            return cls(_aobjectgroup, _aasteroidgroup)

    @classmethod
    def spriteasteroid(cls):
        return Path().cwd().as_posix() + '/' + cls.diretorioImg + '/asteroides.png'