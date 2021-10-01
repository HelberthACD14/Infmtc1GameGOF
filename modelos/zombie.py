from pygame import *
from pygame.sprite import Sprite
from modelos.gameConfig import *
import random
import time


class Zombie(Sprite):
  #instance = None
  locationHumano = None
  def __new__(cls, *arg, **kargs):
    #if cls.instance is None:
    cls.instance = object.__new__(cls, *arg, **kargs)
    return cls.instance

  def __init__(self):
    Sprite.__init__(self)
    self.sentido = 0
    self.velocidad = 1
    self.cont = 0
    #self.locationHumano=None

  def ubicar(self, pos):
    self.rect.x = pos[0]
    self.rect.y = pos[1]

  def set_sprites(self, sprites):
    self.imagenes = sprites
    self.image = self.imagenes[self.sentido][0]
    self.rect = self.image.get_rect()

  def update(self,Xper,Yper):
        xDelta= Xper - self.rect.x 
        yDelta= Yper - self.rect.y
        IrIzquierda=xDelta<-(self.velocidad)
        IrDerecha=xDelta>(self.velocidad)
        IrAbajo=yDelta>(self.velocidad)
        IrArriba=yDelta<-(self.velocidad)
        if IrIzquierda: 
            self.rect.left -= self.velocidad
            self.sentido = 1
        if IrDerecha:
            self.rect.left += self.velocidad
            self.sentido = 0
        if IrAbajo:
            self.rect.top += self.velocidad
            self.sentido = 3
        if IrArriba:
            self.rect.top -= self.velocidad
            self.sentido = 2
    
        if IrIzquierda or IrDerecha or IrArriba or IrAbajo:
            self.image = self.imagenes[self.sentido][self.cont]
            self.cont += 1
            self.cont %= 3

            self.rect.top %= SCREEN_HEIGHT-60
            self.rect.left %= SCREEN_WIDTH
           
            
            
      
  
  def draw(self, screen):
      screen.blit(self.image, self.rect)

         
  
    

          