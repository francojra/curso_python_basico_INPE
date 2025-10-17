# Usando a biblioteca PIL (Pillow)

from PIL import Image

tamanho = 128,128

nome = "lena.jpg"

im = Image.open(nome)

im.thumbnail(tamanho, Image.ANTIALIAS) #  cria miniatura,com suavizacao

im.save("mini_" + nome)
