from curses.ascii import ESC
import random
import pygame

from classes.classAsteroid import Asteroid
from classes.classConfigTela import ConfigTela
from classes.classEfeitosSonoros import Som
from classes.classNave import MotherShip
from pygame.locals import *

from classes.classShot import Shot

gameover = False

if __name__ == '__main__':
    tela = ConfigTela()
    som = Som()
    objectGroup = pygame.sprite.Group()
    asteroidGroup = pygame.sprite.Group()
    shotGroup = pygame.sprite.Group()
    tela.setaimagemfundo(objectGroup)

    ship = MotherShip(objectGroup)
    asteroid = Asteroid(objectGroup, asteroidGroup)
    timer = 0
    while True:
        tela.clock.tick(60) # frames por segundo

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == QUIT or event.key == ESC:
                    tela.fecharJogo()
                elif event.key == pygame.K_SPACE:
                    newShot = Shot.atira(objectGroup, shotGroup)
                    newShot.rect.center = ship.rect.center

        if not gameover:
            tela.corTelaDefault()
            objectGroup.update()
            objectGroup.draw(tela.display)
            tela.timer += 1
            # a cada 1 segundo, há 50% de chances de um asteroide novo aparecer.
            if tela.timer > 60:
                tela.timer = 0
                newasteroid = asteroid.verificanovoasteroide(objectGroup, asteroidGroup)

            collisions = pygame.sprite.spritecollide(ship, asteroidGroup, False, pygame.sprite.collide_mask)
            if collisions:
                gameover = True
            pygame.sprite.groupcollide(shotGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

            # pygame.key.get_pressed()  # Captura os eventos de tecla pressionada
            pygame.display.update()
