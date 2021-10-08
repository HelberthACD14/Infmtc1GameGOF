from pygame import *
from pygame.sprite import Sprite
from modelos.gameConfig import *

class Banner(Sprite):
  instance = None
  vida=0

  def __new__(cls, *arg, **kargs):
    if cls.instance is None:
      cls.instance = object.__new__(cls, *arg, **kargs)
    return cls.instance

  def __init__(self):
    Sprite.__init__(self)
    self.vida = 200
    self.puntos = 0

  def update(self):
      self.puntos += 1

  def zombieBite(self):
    self.vida -= 1


  def draw(self, screen):
    fuente = font.Font(None, 30)
    textoPuntos = fuente.render("Puntos: " + str(self.puntos), 1, (100,255,255))
    screen.blit(textoPuntos, (SCREEN_WIDTH-140, SCREEN_HEIGHT-20))
    textoVida = fuente.render("Vida: " + str(self.vida), 1, (255,100,100))
    screen.blit(textoVida, (0, SCREEN_HEIGHT-20))
