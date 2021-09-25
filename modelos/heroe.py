from pygame import *
from pygame.sprite import Sprite

class Heroe(Sprite):
  instance = None

  def __new__(cls, *arg, **kargs):
    if cls.instance is None:
      cls.instance = object.__new__(cls, *arg, **kargs)
    return cls.instance

  def __init__(self):
    Sprite.__init__(self)
    self.sentido = 0
    self.velocidad = 2
    self.cont = 0
    self.vida = 100
    self.puntos = 0

  def ubicar(self, pos):
    self.rect.x = pos[0]
    self.rect.y = pos[1]

  def set_sprites(self, sprites):
    self.imagenes = sprites
    self.image = self.imagenes[self.sentido][0]
    self.rect = self.image.get_rect()

  def update(self):
    teclas = key.get_pressed()
    if teclas[K_LEFT]:
      self.rect.left -= self.velocidad
      self.sentido = 1
    if teclas[K_RIGHT]:
      self.rect.left += self.velocidad
      self.sentido = 0
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
      self.puntos += 1

      self.rect.top %= 300
      self.rect.left %= 300

  def draw(self, screen):
    fuente = font.Font(None, 20)
    texto = fuente.render("puntos: " + str(self.puntos), 1, (20,20,50))
    screen.blit(self.image, self.rect)
    screen.blit(texto, (self.rect.x - 20, self.rect.y -15))
