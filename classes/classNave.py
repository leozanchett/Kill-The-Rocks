import pygame
from pathlib import Path


class MotherShip(pygame.sprite.Sprite):
    diretorioImg = 'images'
    diretorioSom = 'sounds'

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(self.nave())
        # redimensiona a imagem.
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)
        self.ataqueSom = pygame.mixer.Sound(self.carregaataque())
        self.speed = 0
        self.aceleration = 0.1

    def update(self, *args, **kwargs) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.somataque()
        if (keys[pygame.K_d]) or (keys[pygame.K_a]) or (keys[pygame.K_w]) or (keys[pygame.K_s]):
            self.movimentonave(keys)
        else:
            self.speed *= 0.95
        self.colisao()

    def movimentonave(self, _akey):
        self.speed += self.aceleration
        if self.speed > 6:
            self.speed = 6
        if _akey[pygame.K_d]:
            self.rect.x += self.speed
        if _akey[pygame.K_a]:
            self.rect.x -= self.speed
        if _akey[pygame.K_s]:
            self.rect.y += self.speed
        if _akey[pygame.K_w]:
            self.rect.y -= self.speed

    def colisao(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 420:
            self.rect.right = 420

    def somataque(self):
        self.ataqueSom.set_volume(0.09)
        self.ataqueSom.play()

    @classmethod
    def carregaataque(cls):
        return Path().cwd().as_posix() + '/'+cls.diretorioSom+'/silencer.wav'

    @classmethod
    def nave(cls):
        return Path().cwd().as_posix() + '/'+cls.diretorioImg+'/naveprincipal.png'
