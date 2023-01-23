import cv2
import numpy as np

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

archivo=open("arrays.txt","w")
archivo.close

for detection in detections[0][0]:
     
     if detection[2] > 0.30:
          label = classes[detection[1]]
          box = detection[3:7] * [width, height, width, height]
          x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
          cX = x+((w-x)//2)
          cY = y+((h-y)//2)
          
          rectangle = cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
          cv2.putText(image, "Conf: {:.2f}".format(detection[2] * 100), (x, y - 5), 1, 1.2, (255, 0, 0), 2)
          cv2.putText(image, label, (x, y - 25), 1, 1.2, (255, 0, 0), 2)
   
          detec2=np.append(detection,[cX, cY])
          archivo=open("arrays.txt","a")
          archivo.write("["+ "\n")
          for i in range(len(detec2)):
               archivo.write(str(detec2[i])+"\n")
          archivo.write("]"+"\n")
          archivo.close
          
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
