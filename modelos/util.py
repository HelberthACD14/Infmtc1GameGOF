from pygame import image

def cargar_imagen(nombre):
  imagen = image.load(nombre)
  return imagen #.convert_alpha()
