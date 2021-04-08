from curses.ascii import ESC
import random
import pygame

from classes.classAsteroid import Asteroid
from classes.classConfigTela import ConfigTela
from classes.classEfeitosSonoros import Som
from classes.classNave import MotherShip
from pygame.locals import *

if __name__ == '__main__':
    tela = ConfigTela()
    som = Som()
    objectGroup = pygame.sprite.Group()
    asteroidGroup = pygame.sprite.Group()

    ship = MotherShip(objectGroup)
    asteroid = Asteroid(objectGroup, asteroidGroup)
    timer = 0
    while True:
        tela.clock.tick(60) # frames por segundo

        for event in pygame.event.get():
            if event.type == QUIT or event.type == ESC:
                tela.fecharJogo()
        tela.corTelaDefault()
        objectGroup.update()
        objectGroup.draw(tela.display)
        timer += 1
        # a cada 1 segundo, há 50% de chances de um asteroide novo aparecer.
        if timer > 60:
            timer = 0
            if random.random() < 0.5:
                newAsteroid = Asteroid(objectGroup, asteroidGroup)

        collisions = pygame.sprite.spritecollide(ship, asteroidGroup, False)
        if collisions:
            print('GAME OVER !')
            tela.fecharJogo()

        # pygame.key.get_pressed()  # Captura os eventos de tecla pressionada
        pygame.display.update()
