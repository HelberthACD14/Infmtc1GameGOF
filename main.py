import pygame
from pygame.locals import *
import sys
from modelos.util import cargar_imagen
from modelos.constructores import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
ICON_SIZE = 32

def game():
  pygame.init()
  director = Director()
  director.set_constructor(ConstructorHumanos())
  img_inicio = cargar_imagen('imagenes/inicio2.jpg')
  img_fondo = cargar_imagen('imagenes/fondo.jpg')
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  pygame.mouse.set_visible(False)

  heroe = director.get_heroe()
  jugando = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    teclas = pygame.key.get_pressed()
    if teclas[K_SPACE]:
      heroe.ubicar((200,200))
      jugando = True
    if jugando:
      screen.blit(img_fondo, (0, 0))
      heroe.update()
      heroe.draw(screen)
    else:
      screen.blit(img_inicio, (0, 0))
    pygame.display.update()
    pygame.time.delay(10)
    print(jugando)


if __name__ == '__main__':
  game()