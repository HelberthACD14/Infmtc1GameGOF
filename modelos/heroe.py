from pygame import *
from pygame.sprite import Sprite
from modelos.gameConfig import *

class Heroe(Sprite):
  instance = None

  def __new__(cls, *arg, **kargs):
    if cls.instance is None:
      cls.instance = object.__new__(cls, *arg, **kargs)
    return cls.instance

  def __init__(self):
    Sprite.__init__(self)
    self.sentido = 0
    self.velocidad = 3
    self.cont = 0

  def ubicar(self, pos):
    self.rect.x = pos[0]
    self.rect.y = pos[1]

  def get_location(self):
      cordenadas=[self.rect.x,self.rect.y]
      return cordenadas

  def set_sprites(self, sprites):
    self.imagenes = sprites
    self.image = self.imagenes[self.sentido][0]
    self.rect = self.image.get_rect()

  def update(self):
    teclas = key.get_pressed()
    if teclas[K_RIGHT]:
          self.rect.left += self.velocidad
          self.sentido = 0
    if teclas[K_LEFT]:
      self.rect.left -= self.velocidad
      self.sentido = 1
    if teclas[K_DOWN]:
      self.rect.top += self.velocidad
      self.sentido = 2
    if teclas[K_UP]:
      self.rect.top -= self.velocidad
      self.sentido = 3
    
    if teclas[K_LEFT] or teclas[K_RIGHT] or teclas[K_UP] or teclas[K_DOWN]:
      self.image = self.imagenes[self.sentido][self.cont]
      self.cont += 1
      self.cont %= 3

      self.rect.top %= SCREEN_HEIGHT-60
      self.rect.left %= SCREEN_WIDTH

  def draw(self, screen):
    screen.blit(self.image, self.rect)


