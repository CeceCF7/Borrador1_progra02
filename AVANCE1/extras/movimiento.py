import serial
import time

lista_distancia=[]
lista_angulos=['40,10/','20,0/']

def calcularDistancia(lista):
    arduino = serial.Serial('COM3',9600)
    for x in range(len(lista)):
        time.sleep(2)
        arduino.write(lista[x].encode())
        time.sleep(3)
        distancia = arduino.readline()
        number = distancia.decode().split()
        lista_distancia.append(int(number[0]))
    arduino.close()

print(calcularDistancia(lista_angulos))
print(lista_distancia)


