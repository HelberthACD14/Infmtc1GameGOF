import pygame
from pygame.locals import *
import sys
from modelos.util import cargar_imagen
from modelos.constructores import *
from modelos.gameConfig import *

def game():
  pygame.init()
  director = Director()
  director.set_constructor(ConstructorHumanos())
  img_inicio = cargar_imagen(ImagenCarga)
  img_fondo = cargar_imagen('imagenes/fondo.jpg')
  img_banner = cargar_imagen('imagenes/Banner.png')
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  pygame.mouse.set_visible(False)

  heroe = director.get_heroe()
  banner = director.get_banner()
  jugando = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    teclas = pygame.key.get_pressed()
    if teclas[K_SPACE]:
      heroe.ubicar((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
      jugando = True
    if jugando:
      screen.blit(img_fondo, (0, 0))
      screen.blit(img_banner, (0, SCREEN_HEIGHT-40))
      heroe.update()
      banner.update()
      heroe.draw(screen)
      banner.draw(screen)
    else:
      screen.blit(img_inicio, (0, 0))
    pygame.display.update()
    pygame.time.delay(10)
    print(jugando)


if __name__ == '__main__':
  game()