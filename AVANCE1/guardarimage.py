from PIL import Image
import requests
from io import BytesIO

#Cambiar la direccion IP segun su configuracion
url = "http://192.168.7.186/cam-lo.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))

try:
    img.save('Camara.jpg')
except IOError:
    print("cannot convert", infile)
