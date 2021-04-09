import sys
from pathlib import Path

import pygame
from uteis.style import CINZA_CLARO

class ConfigTela:
    diretorioImg = 'images'


    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode([840, 480])
        pygame.display.set_caption('KILL THE ROCKS')
        self.display.fill(CINZA_CLARO)
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.imagemfundo = None

    def setaimagemfundo(self, _aobjgroup):
        self.imagemfundo = pygame.sprite.Sprite(_aobjgroup)
        self.imagemfundo.image = pygame.image.load(self.imagemdefundo())
        self.imagemfundo.image = pygame.transform.scale(self.imagemfundo.image, [840, 480])
        self.imagemfundo.rect = self.imagemfundo.image.get_rect()

    def corTelaDefault(self):
        self.display.fill(CINZA_CLARO)

    def fecharJogo(self):
        pygame.quit()
        sys.exit()

    @classmethod
    def imagemdefundo(cls):
        return Path().cwd().as_posix() + '/' + cls.diretorioImg + '/fundo.png'