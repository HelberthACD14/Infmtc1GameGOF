from abc import ABC, abstractmethod

from .heroe import *
from .fabricas import *
from .banner import *
from .zombie import *


class Director:
  __constructor__ = None
 
  def set_constructor(self, constructor):
    self.__constructor__ = constructor    

  def get_heroe(self):
    heroe = Heroe()
    heroe.set_sprites(self.__constructor__.get_sprites())
    return heroe
  def get_banner(self):
    banner = Banner()
    return banner

  def get_zombie(self):
    zombie = Zombie()
    zombie.set_sprites(self.__constructor__.get_sprites())
    return zombie  


class Constructor(ABC):
  def get_sprites(self):
    pass

class ConstructorHumanos(Constructor):
  def __init__(self):
    self.fabrica = FabricaHumano()

  def get_sprites(self):
    return [self.fabrica.crear_derecha(),
            self.fabrica.crear_izquierda(),
            self.fabrica.crear_abajo(),
            self.fabrica.crear_arriba()]

class ConstructorZombiez(Constructor):
  def __init__(self):
    self.fabrica = FabricaZombie()
  def get_sprites(self):
    return [self.fabrica.crear_derecha(),
            self.fabrica.crear_izquierda(),
            self.fabrica.crear_abajo(),
            self.fabrica.crear_arriba()]

  
            
  
