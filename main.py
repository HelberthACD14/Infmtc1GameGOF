import pygame
from pygame import rect
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
  
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.mouse.set_visible(False)
 
  banner = director.get_banner()
  heroe = director.get_heroe()

  director.set_constructor(ConstructorZombies())

  zombiesA = zombiesI
  zombies = []
  for i in range(zombiesA):  
    zombies.append(director.get_zombie())

  jugando = False
  gameOver = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    teclas = pygame.key.get_pressed()


    if teclas[K_SPACE]:
      heroe.live = 200
      heroe.ubicar((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
      for i in zombies:
        i.ubicar((random.randint(0, SCREEN_WIDTH),random.randint(0, SCREEN_HEIGHT)))
      jugando = True

    if jugando:
      if gameOver:
        screen.blit(img_gameover, (0,0))
        fuente = font.Font(None, 30)
        PuntajeFinal = fuente.render("Puntaje Final: " + str(banner.puntos), 1, (255,100,100))
        screen.blit(PuntajeFinal, (SCREEN_WIDTH/3 + 50, 3*SCREEN_HEIGHT/4))
      else:

        zombiesQ = zombiesI + (banner.puntos // UmbralPuntos)
        if zombiesA != zombiesQ:
          zombiesA = zombiesQ
          zombies.append(director.get_zombie())
          last_element = zombies[-1]
          last_element.ubicar((random.randint(0, SCREEN_WIDTH),random.randint(0, SCREEN_HEIGHT)))      
        
        screen.blit(img_fondo, (0, 0))
        screen.blit(img_banner, (0, SCREEN_HEIGHT-40))
        heroe.update()

        for i in zombies:
          i.update(heroe.rect.x,heroe.rect.y)
          if heroe.rect.colliderect(i.rect):
            banner.zombieBite()
        banner.update()
        heroe.draw(screen)
        for i in zombies:
          i.draw(screen)
        banner.draw(screen)
        if banner.vida < 1:
          gameOver = True  
    else:
      screen.blit(img_inicio, (0, 0))
    pygame.display.update()
    pygame.time.delay(10)

    


if __name__ == '__main__':
  game()