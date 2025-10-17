# Usando a biblioteca PIL (Pillow)

from PIL import Image

from PIL import ImageDraw

img = Image.open("lena.jpg")

draw = ImageDraw.Draw(img)

texto = "Eu me chamo Jeanne e fiz o curso de Python..."

pos = 50, 50

draw.text(pos, texto)

img.save("lena_com_texto.jpg")

img.show() 
