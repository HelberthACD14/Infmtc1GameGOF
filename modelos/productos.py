from abc import ABC, abstractmethod
from .util import cargar_imagen

class Abajo(ABC):
  @abstractmethod
  def get_sprites(self):
    pass

class Arriba(ABC):
  @abstractmethod
  def get_sprites(self):
    pass

class Izquierda(ABC):
  @abstractmethod
  def get_sprites(self):
    pass

class Derecha(ABC):
  @abstractmethod
  def get_sprites(self):
    pass

class AbajoHumano(Abajo):
  def get_sprites(self):
    return [cargar_imagen('imagenes/F1.png'),
            cargar_imagen('imagenes/F2.png'),
            cargar_imagen('imagenes/F3.png')]

class ArribaHumano(Arriba):
  def get_sprites(self):
    return [cargar_imagen('imagenes/B1.png'),
            cargar_imagen('imagenes/B2.png'),
            cargar_imagen('imagenes/B3.png')]

class IzquierdaHumano(Izquierda):
  def get_sprites(self):
    return [cargar_imagen('imagenes/I1.png'),
            cargar_imagen('imagenes/I2.png'),
            cargar_imagen('imagenes/I3.png')]

class DerechaHumano(Derecha):
  def get_sprites(self):
    return [cargar_imagen('imagenes/D1.png'),
            cargar_imagen('imagenes/D2.png'),
            cargar_imagen('imagenes/D3.png')]

class AbajoZombie(Abajo):
  def get_sprites(self):
    return [cargar_imagen('imagenes/ZB1.png'),
            cargar_imagen('imagenes/ZB2.png'),
            cargar_imagen('imagenes/ZB3.png')]            

class ArribaZombie(Arriba):
  def get_sprites(self):
    return [cargar_imagen('imagenes/ZF1.png'),
            cargar_imagen('imagenes/ZF2.png'),
            cargar_imagen('imagenes/ZF3.png')]            
class IzquierdaZombie(Izquierda):
  def get_sprites(self):
    return [cargar_imagen('imagenes/ZI1.png'),
            cargar_imagen('imagenes/ZI2.png'),
            cargar_imagen('imagenes/ZI3.png')]            
class DerechaZombie(Derecha):
  def get_sprites(self):
    return [cargar_imagen('imagenes/ZD1.png'),
            cargar_imagen('imagenes/ZD2.png'),
            cargar_imagen('imagenes/ZD3.png')]                                                

          







