# Usando a biblioteca PIL (Pillow)

from PIL import Image

im = Image.open("lena.ppm")

im.save("lena.jpg", "JPEG") # Pega a imagem .ppm e salva em formato JPEG

# im2 = Image.open("cer.webp")

# im2.save("cer.jpg", "JPEG") # Pega a imagem .ppm e salva em formato JPEG

