import cv2
import numpy as np

distancia = [10,20,30,40,50,60,70,80,90,100]
# ----------- READ DNN MODEL -----------
# Model architecture
prototxt = "model/MobileNetSSD_deploy.prototxt.txt"
# Weights
model = "model/MobileNetSSD_deploy.caffemodel"
# Class labels
classes = {0:"background", 1:"aeroplane", 2:"bicycle",
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

archivo=open("base_datos2.txt","r")
contenido=archivo.read()
lista=contenido.split("\n")
archivo.close()

for i in range(len(contenido))
    cv2.putText(image, label, (x, y - 25), 1, 1.2, (255, 0, 0), 2)
    cv2.putText(image, f'distancia:{str(distancia[rectangle])}', (x, y - 5), 1, 1.2, (255, 0, 0), 2)