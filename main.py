import pygame
from pygame.locals import *
import sys
from modelos.util import cargar_imagen
from modelos.constructores import *
from modelos.gameConfig import *
import random

def game():
  pygame.init()
  director = Director()
  director.set_constructor(ConstructorHumanos())
  madScientist = Director()
  madScientist.set_constructor(ConstructorZombies())
  img_inicio = cargar_imagen(ImagenCarga)
  img_fondo = cargar_imagen('imagenes/fondo.jpg')
  img_banner = cargar_imagen('imagenes/Banner.png')
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  pygame.mouse.set_visible(False)

  heroe = director.get_heroe()
  banner = director.get_banner()
  zombie1 = madScientist.get_zombie()
  print(zombie1)
  zombies = []
  for i in range(3):
    zombies.append(madScientist.get_zombie())
  print(zombies)
  jugando = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    teclas = pygame.key.get_pressed()
    if teclas[K_SPACE]:
      heroe.ubicar((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
      for i in zombies:
        i.ubicar((random.randint(0, SCREEN_WIDTH),random.randint(0, SCREEN_HEIGHT)))
      jugando = True
    if jugando:
      screen.blit(img_fondo, (0, 0))
      screen.blit(img_banner, (0, SCREEN_HEIGHT-40))
      heroe.update()
      for i in zombies:
        i.update(heroe.rect.x,heroe.rect.y)
      banner.update()
      heroe.draw(screen)
      for i in zombies:
        i.draw(screen)
      banner.draw(screen)
    else:
      screen.blit(img_inicio, (0, 0))
    pygame.display.update()
    pygame.time.delay(10)
    print(jugando)


if __name__ == '__main__':
  game()