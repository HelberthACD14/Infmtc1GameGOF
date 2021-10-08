import pygame
from pygame.locals import *
import sys
from modelos.util import cargar_imagen
from modelos.constructores import *
from modelos.gameConfig import *
import random
from modelos.observador import *


def game():
  pygame.init()
  director = Director()
  publisher = Publisher();
  
  director.set_constructor(ConstructorHumanos())
  
  img_inicio = cargar_imagen(ImagenCarga)
  img_fondo = cargar_imagen('imagenes/fondo.jpg')
  img_banner = cargar_imagen('imagenes/Banner.png')
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  pygame.mouse.set_visible(False)

  
  banner = director.get_banner()
  heroe = director.get_heroe()
  liveHeroe= heroe.live
  subcriptor = Subscriber(heroe)
  publisher.register(subcriptor)
  
  director.set_constructor(ConstructorZombiez())
  
  zombie1 = director.get_zombie()
  zombie2 = director.get_zombie()
  zombie3 = director.get_zombie()
  heroeSize=pygame.Rect(heroe.rect.left,heroe.rect.top,25,19)
  
  
  """random1 = [
              random.randrange(800,600),
              random.randrange(800,600)
            ]"""
  
  pos2 =[random.randint(SCREEN_HEIGHT,SCREEN_WIDTH),random.randint(SCREEN_HEIGHT,SCREEN_WIDTH)]
  pos3 =[random.randint(SCREEN_HEIGHT,SCREEN_WIDTH),random.randint(SCREEN_HEIGHT,SCREEN_WIDTH)]
  jugando = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    teclas = pygame.key.get_pressed()
    if teclas[K_SPACE]:
      heroe.ubicar((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
      zombie1.ubicar((0,SCREEN_HEIGHT/random.randint(1,5)))#divisor= random.randint(1,5)
      zombie2.ubicar((0,SCREEN_HEIGHT/random.randint(1,5)))
      zombie3.ubicar((SCREEN_WIDTH/random.randint(1,5),0))
      
      
      jugando = True
    if jugando:
      screen.blit(img_fondo, (0, 0))
      screen.blit(img_banner, (0, SCREEN_HEIGHT-40))
      heroe.update()
      heroe.get_location()
      #print(cordenadas)
      #zombie1.setHumanoLocation(cordenadas)
      zombie1.update(heroe.rect.x,heroe.rect.y)
      zombie1.velocidad=4
      #zombie2.update(heroe.rect.x,heroe.rect.y)
      #zombie2.velocidad=2
      #zombie3.update(heroe.rect.x,heroe.rect.y)
      #zombie3.velocidad=3
      banner.update()
      heroe.draw(screen)
      zombie1.draw(screen)
      #zombie2.draw(screen)
      #zombie3.draw(screen)
      #Revisamos las colisiones
      #print (heroe.rect.colliderect(zombie1.rect))
      if heroe.rect.colliderect(zombie1.rect):
         heroe.live=heroe.live-1
         publisher.dispatch(heroe)
      if heroe.live==0:
                  
      
      #print (screen)
      #zombie1.draw(screen)
      #zombie2.draw(screen)
      banner.draw(screen)
    else:
      screen.blit(img_inicio, (0, 0))
    pygame.display.update()
    pygame.time.delay(20)
    #print(jugando)


if __name__ == '__main__':
  game()