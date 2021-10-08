from modelos.util import *
# Windows size configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
zombiesI = 2
UmbralPuntos = 500

if SCREEN_WIDTH>=800 and SCREEN_HEIGHT>=600:
    ImagenCarga='imagenes/inicio.jpg'
else:
    ImagenCarga='imagenes/inicio2.jpg'

img_inicio = cargar_imagen(ImagenCarga)
img_fondo = cargar_imagen('imagenes/fondo.jpg')
img_banner = cargar_imagen('imagenes/Banner.png')
img_gameover=cargar_imagen('imagenes/GameOver.jpeg')
