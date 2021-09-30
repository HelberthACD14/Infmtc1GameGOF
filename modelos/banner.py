from pygame import *
from pygame.sprite import Sprite
from modelos.gameConfig import *

class Banner(Sprite):
  instance = None

  def __new__(cls, *arg, **kargs):
    if cls.instance is None:
      cls.instance = object.__new__(cls, *arg, **kargs)
    return cls.instance

  def __init__(self):
    Sprite.__init__(self)
    self.vida = 100
    self.puntos = 0


  def update(self):
      self.puntos += 1

  def draw(self, screen):
    fuente = font.Font(None, 30)
    texto = fuente.render("Puntos: " + str(self.puntos), 1, (100,255,255))
    screen.blit(texto, (SCREEN_WIDTH-140, SCREEN_HEIGHT-20))