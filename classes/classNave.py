import pygame
from pathlib import Path


class NavePrincipal(pygame.sprite.Sprite):
    diretorioImg = 'images'
    diretorioSom = 'sounds'

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(self.nave())
        # redimensiona a imagem.
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)
        self.ataqueSom = pygame.mixer.Sound(self.carregaAtaque())

    def update(self, *args, **kwargs) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_SPACE]:
            self.somAtaque()
        self.colisao()

    def colisao(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 420:
            self.rect.right = 420

    def somAtaque(self):
        self.ataqueSom.set_volume(0.09)
        self.ataqueSom.play()

    @classmethod
    def carregaAtaque(cls):
        return Path().cwd().as_posix() + '/'+cls.diretorioSom+'/silencer.wav'

    @classmethod
    def nave(cls):
        return Path().cwd().as_posix() + '/'+cls.diretorioImg+'/naveprincipal.png'