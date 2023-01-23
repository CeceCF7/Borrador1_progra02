from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, QPoint
from PyQt5 import QtCore, QtWidgets
import numpy as np
import sys
import serial
import time
from PIL import Image
import requests
from io import BytesIO

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        loadUi('Interfaz.ui', self)

        self.bt_normal.hide()
        self.click_posicion = QPoint()
        self.bt_minimize.clicked.connect(lambda: self.showMinimized())
        self.bt_normal.clicked.connect(self.control_bt_normal)
        self.bt_maximize.clicked.connect(self.control_bt_maximize)
        self.bt_close.clicked.connect(lambda: self.close())
    
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        self.frame_superior.mouseMoveEvent = self.mover_ventana

        self.serial = QSerialPort()
        self.bt_update.clicked.connect(self.read_ports)
        self.bt_connect.clicked.connect(self.serial_connect)
        self.bt_disconnect.clicked.connect(lambda: self.serial.close())
        self.read_ports()

        self.save_photo.clicked.connect(self.guardar_foto)
        self.calculate.clicked.connect(self.enviar_datos)

    def read_ports(self):
        self.baudrates = ['1200', '2400', '4800', '9600', '19200', '38400', '115200']
        portList = []
        ports = QSerialPortInfo().availablePorts()
        for i in ports:
            portList.append(i.portName())

        self.cb_list_ports.clear()
        self.cb_list_baudrates.clear()
        self.cb_list_ports.addItems(portList)
        self.cb_list_baudrates.addItems(self.baudrates)
        self.cb_list_baudrates.setCurrentText('9600')

    def serial_connect(self):
        self.serial.waitForBytesWritten(100)
        self.port = self.cb_list_ports.currentText()
        self.baud = self.cb_list_baudrates.currentText()
        self.serial.setBaudRate(int(self.baud))
        self.serial.setPortName(self.port)
        self.serial.open(QIODevice.ReadWrite)

    def read_data(self):
        if not self.serial.canReadLine(): return
        rx = self.serial.readLine().decode('utf-8')
        if rx.endswith("."):
            rx = rx[:-1]
            return rx

    def send_data(self,data):
        data = data + '\n'
        print('data')
        if self.serial.isOpen():
            self.serial.write(data.encode())
    
    def guardar_foto(self):
        url = "http://192.168.7.186/cam-lo.jpg"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        try:
            img.save('Camara.jpg')
        except IOError:
            print("cannot convert")  #infile
            
    def obtener_lista(self):
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
        
        return general 
    
    def obtener_angulos(self, Lista, ancho=800, largo=800):
        
        for k in range(0,15):
            
            for j in range(0,15):
            
                for i in range(0,len(Lista)): 
            
                    if (ancho*j/15<=Lista[i][2]<ancho*(j+1)/15) and (largo*k/15<=Lista[i][3]<largo*(k+1)/15):
                        Lista[i].append(6*(j+1)) #horizontal      
                        Lista[i].append(2*(k+1)) #vertical    
        return Lista

    def calcularDistancia(self, lista_angulos):
        lista_distancia=[]
        arduino = serial.Serial('COM3',9600)
        for x in range(len(lista_angulos)):
            time.sleep(2)
            arduino.write(lista_angulos[x].encode())
            time.sleep(3)
            distancia = arduino.readline()
            number = distancia.decode().split()
            lista_distancia.append(int(number[0]))
        arduino.close()
        return lista_distancia

    def enviar_datos(self):
        listax=self.obtener_lista()
        listay=self.obtener_angulos(listax)
        listaz=[]
        
        for i in range(len(listay)):
            angle2=str(listay[i][len(listay)-1])
            angle1=str(listay[i][len(listay)-2])
            formato = angle1 + ',' + angle2 + '/'
            listaz.append(formato)            
        
        lista_a = self.calcularDistancia(listaz)

        for y in range(len(listay)):
            listay[y].append(lista_a[y])

        #escribiendo en el archivo
        archivo=open("base_datos.txt","w")
        for i in range(len(listay)):
            archivo.write("["+"\n")
            for j in range(0,7):
                archivo.write(str(listay[i][j])+"\n")
            archivo.write("]"+"\n")
        archivo.close  

    def control_bt_normal(self):
        self.showNormal()
        self.bt_normal.hide()
        self.bt_maximize.show()

    def control_bt_maximize(self):
        self.showMaximized()
        self.bt_maximize.hide()
        self.bt_normal.show()
    
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    
    def mousePressEvent(self, event):
        self.click_posicion = event.globalPos()
    
    def mover_ventana(self,event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_posicion)
                self.click_posicion = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 5 or event.globalPos().x() <= 5 :
            self.showMaximized()
            self.bt_maximize.hide()
            self.bt_normal.show()
        else:
            self.showNormal()
            self.bt_normal.hide()
            self.bt_maximize.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())
