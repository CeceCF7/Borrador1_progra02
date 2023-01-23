import mysql.connector
from mysql.connector import Error

datos1 = []
datos = []
archivo = open("base_datos.txt", "r")
data = archivo.read()
texto = data.replace("[\n", "").replace("\n]", "]").replace("\n", " ").replace("] ", "\n").replace("]", "")
archivo.close()

archivo = open("base_datos2.txt", "w")
data = archivo.write(texto)
archivo.close()

archivo = open("base_datos2.txt", "r")
lineas = archivo.readlines()
for linea in lineas:
	datos1.append(linea.strip('\n'))
for dato in datos1:
    datos.append(dato.split(" "))
for dato in datos:
    for i in range(len(dato)):
        dato[i] = float(dato[i])
archivo.close()

for dato in datos:
    dato[0] = round(dato[0], 1)
    dato[1] = round(dato[1], 6)
    dato[2] = round(float(dato[6]), 3)
    dato[3] = round(float(dato[5]), 2)
    dato[4] = round(float(dato[4]), 2)
    dato.pop(6)
    dato.pop(5)
    dato = tuple(dato)

print(datos)

#UPLOADING INFORMATION TO DATABASE
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        db="db_prueba"
        )
    cur = connection.cursor()
    sql_1 = "INSERT INTO sensor (marca, modelo, angulo_vertical, angulo_horizontal, coordenadas) VALUES (%s, %s, %s, %s, %s)"
    val_1 = ("genérica", "HC-SR04", 0, 0, "(0, 0, 0)") #EJEMPLO DATOS SENSOR
    cur.execute(sql_1, val_1)
    sql_2 = "INSERT INTO camara (marca, modelo, angulo_vertical, angulo_horizontal, coordenadas) VALUES (%s, %s, %s, %s, %s)"
    val_2 = ("genérica", "ESP32-CAM con cámara OV2640", 0, 0, "(0, 0, 0)") #EJEMPLO DATOS CÁMARA
    cur.execute(sql_2, val_2)
    sql_3 = "INSERT INTO esp32board (marca, modelo) VALUES (%s, %s)"
    val_3 = ("genérica", "NODEMCU-32 30-PIN") #EJEMPLO DATOS ESP32-BOARD
    cur.execute(sql_3, val_3)
    sql_4 = "INSERT INTO obstaculos (label, confianza, distancia, angulo_vertical, angulo_horizontal) VALUES (%s, %s, %s, %s, %s)"
    val_4 = datos
    cur.executemany(sql_4, val_4)
    connection.commit()
    print("Data was uploaded successfully")
except Error as error:
    print("Error loading Obstacles: {}".format(error))
finally:
    if (connection.is_connected()):
        cur.close()
        connection.close()
        print("MySQL connection is closed")
