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
  madScientist = Director()
  madScientist.set_constructor(ConstructorZombies())
  img_inicio = cargar_imagen(ImagenCarga)
  img_fondo = cargar_imagen('imagenes/fondo.jpg')
  img_banner = cargar_imagen('imagenes/Banner.png')
  img_gameover=cargar_imagen('imagenes/GameOver.jpeg')
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  pygame.mouse.set_visible(False)

  heroe = director.get_heroe()
  banner = director.get_banner()
  zombie1 = madScientist.get_zombie()
  print(zombie1)
  zombiesA = zombiesI
  zombies = []
  for i in range(zombiesA):  
    zombies.append(madScientist.get_zombie())
  print(zombies)
  jugando = False
  gameOver = False
  velocidadFinal=1
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
      if gameOver:
        screen.blit(img_gameover, (0,0))
        fuente = font.Font(None, 30)
        PuntajeFinal = fuente.render("Puntaje Final: " + str(banner.puntos), 1, (255,100,100))
        screen.blit(PuntajeFinal, (SCREEN_WIDTH/3 + 50, 3*SCREEN_HEIGHT/4))
      else:
        zombiesQ = zombiesI + (banner.puntos // UmbralPuntos)
        if zombiesA != zombiesQ:
          zombiesA = zombiesQ
          zombies.append(madScientist.get_zombie())
          last_element = zombies[-1]
          last_element.ubicar((random.randint(0, SCREEN_WIDTH),random.randint(0, SCREEN_HEIGHT)))      
        screen.blit(img_fondo, (0, 0))
        screen.blit(img_banner, (0, SCREEN_HEIGHT-40))
        heroe.update()
        for i in zombies:
          i.update(heroe.rect.x,heroe.rect.y)
          if banner.puntos%1000==0:
            velocidadFinal+=1    
            i.velocidad=random.randint(0, velocidadFinal)
          collideX = abs(heroe.rect.x - i.rect.x)
          collideY = abs(heroe.rect.y - i.rect.y)
          
          if collideX<5 and collideY<5:
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
    print(velocidadFinal)


if __name__ == '__main__':
  game()