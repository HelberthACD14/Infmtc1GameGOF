from abc import ABC, abstractmethod
from .productos import *

class FabricaAbstracta(ABC):
  @abstractmethod
  def crear_izquierda(self):
    pass

  @abstractmethod
  def crear_derecha(self):
    pass

  @abstractmethod
  def crear_arriba(self):
    pass

  @abstractmethod
  def crear_abajo(self):
    pass

class FabricaHumano(FabricaAbstracta):
  def crear_izquierda(self):
    producto = IzquierdaHumano()
    return producto.get_sprites()

  def crear_derecha(self):
    producto = DerechaHumano()
    return producto.get_sprites()

  def crear_arriba(self):
    producto = ArribaHumano()
    return producto.get_sprites()

  def crear_abajo(self):
    producto = AbajoHumano()
    return producto.get_sprites()