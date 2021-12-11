#PNGTOICO
#Filip Rokita
#www.filiprokita.com

from PIL import Image

pngImg = input(".png: ")
icoImg = pngImg+".ico"

img = Image.open(pngImg)
img.save(icoImg)

print(".ico: "+icoImg)