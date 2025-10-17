# Usando a biblioteca PIL (Pillow)

from PIL import Image

im = Image.open("lena.ppm")

print(im.format, im.size, im.mode)

im.show()
