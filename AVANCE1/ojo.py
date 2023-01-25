import mysql.connector
from mysql.connector import Error
import cv2
import numpy as np
       #CREDENCIALES DE ACCESO
my_host = "localhost"
my_user = "root"
my_password = "valiente360"
my_database = "db_prueba"

        # LISTA VACÍA PARA LAS DISTANCIAS
distancias = []
        
try:
    connection = mysql.connector.connect(
        host=my_host,
        user=my_user,
        passwd=my_password,
        db=my_database
        )
    cur = connection.cursor()
    cur.execute("SELECT * FROM obstaculos")
    for registro in cur.fetchall():
        Distancia = registro[0]
        distancias.append(Distancia)
    print("Data has been retrieved successfully")
except Error as error:
    print("Error al ejecutar el procedimiento: {}".format(error))
finally:
    if (connection.is_connected()):
        cur.close()
        connection.close()
        print("MySQL connection is closed")
        
print(distancias)
        #  "distancias" es la lista con las distancias de la base de datos
archivo=open("arrays.txt","r")
contenido=archivo.read()
lista=contenido.split("\n")
archivo.close()
        
general=[]
lista1=[]
for i in range(int((len(lista)-1)/11)):
    for j in range((11*i)+2,(11*i)+4):
        lista1.append(float(lista[j]))
                
    for k in range((11*i)+8, (11*i)+10):
        lista1.append(float(lista[k]))
    general.append(lista1)
    lista1=[]
        

print(general)

prototxt = "model/MobileNetSSD_deploy.prototxt.txt"
# Weights
model = "model/MobileNetSSD_deploy.caffemodel"
# Class labels
classes = {0:"background", 1:"airplane", 2:"bicycle",
          3:"bird", 4:"boat",
          5:"bottle", 6:"bus",
          7:"car", 8:"cat",
          9:"chair", 10:"cow",
          11:"diningtable", 12:"dog",
          13:"horse", 14:"motorbike",
          15:"person", 16:"pottedplant",
          17:"sheep", 18:"sofa",
          19:"train", 20:"tvmonitor"}

# Load the model
net = cv2.dnn.readNetFromCaffe(prototxt, model)

# ----------- READ THE IMAGE AND PREPROCESSING -----------
image = cv2.imread("Camara.jpg")
height, width, _ = image.shape
image_resized = cv2.resize(image, (300, 300))

# Create a blob
blob = cv2.dnn.blobFromImage(image_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5))

# ----------- DETECTIONS AND PREDICTIONS -----------
net.setInput(blob)
detections = net.forward()

print(general[0][2])
print(classes[int(general[0][0])])

for i in range(len(general)):
    cv2.putText(image, f'Objeto:', (int(general[i][2])-20,int(general[i][3])  - 40), 1, 1.1, (57, 255, 20), 2)
    cv2.putText(image, f'{classes[int(general[i][0])]}', (int(general[i][2])-20,int(general[i][3])  - 20), 1, 1.1, (255, 0, 0), 2)
    cv2.putText(image,f'Dist:' ,(int(general[i][2])-25, int(general[i][3]) ), 1, 1.1, (57, 255, 20), 2)
    cv2.putText(image,f'{distancias[i]}' ,(int(general[i][2]+20), int(general[i][3])), 1, 1.1, (255, 0, 0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# {classes[int(general[i][0])]}