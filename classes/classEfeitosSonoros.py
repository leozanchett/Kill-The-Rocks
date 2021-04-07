from pathlib import Path

import pygame


class Som:
    diretorio = 'sounds'

    def __init__(self):
        self.tema = pygame.mixer.music
        self.tema.load(self.carregaMusicatema())
        self.somTema()

    def somTema(self):
        self.tema.set_volume(0.07)
        self.tema.play(-1)

    @classmethod
    def carregaMusicatema(cls):
        return Path().cwd().as_posix() + '/'+cls.diretorio+'/Black Rock.mp3'