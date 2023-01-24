import mysql.connector
from mysql.connector import Error

#TRANSFORMANDO DATOS DE ARCHIVO TXT AL FORMATO ADECUADO
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
        if i == 0:
            pass
        else: 
            dato[i] = float(dato[i])
archivo.close()

for dato in datos:
    dato[1] = round(dato[1], 6)
    dato[2] = round(float(dato[6]), 3)
    dato[3] = round(float(dato[5]), 2)
    dato[4] = round(float(dato[4]), 2)
    dato.pop(6)
    dato.pop(5)
    dato = tuple(dato)

print(datos)

#CREDENCIALES PARA LA CONEXIÓN A MYSQL (CAMBIAR DE ACUERDO A LA COMPU)
my_host = "localhost"
my_user = "root"
my_password = "password"
my_database = "db_prueba"

#SUBIR DATOS A DATABASE
try:
    connection = mysql.connector.connect(
        host=my_host,
        user=my_user,
        passwd=my_password,
        db=my_database
        )
    cur = connection.cursor()
    sql_1 = "INSERT INTO sensor (marca, modelo) VALUES (%s, %s)"
    val_1 = ("genérica", "HC-SR04")
    cur.execute(sql_1, val_1)
    sql_2 = "INSERT INTO camara (marca, modelo) VALUES (%s, %s)"
    val_2 = ("genérica", "ESP32-CAM con cámara OV2640")
    cur.execute(sql_2, val_2)
    sql_3 = "INSERT INTO arduinoboard (marca, modelo) VALUES (%s, %s)"
    val_3 = ("genérica", "ARDUINO UNO")
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

#SACAR DATOS DE DATABASE
idx = {
            "Numero": 0,
            "Label": 1,
            "Confianza": 2,
            "Distancia": 3,
            "Angulo_vertical": 4,
            "Angulo_horizontal": 5,
        }

class radar:
    def __init__(self):
        self.obstaculos = dict()
    
    def load_all_obstaculos(self):
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
                obs = obstaculo()
                Numero = registro[idx["Numero"]]
                Label = registro[idx["Label"]]
                Confianza = registro[idx["Confianza"]]
                Distancia = registro[idx["Distancia"]]
                Angulo_vertical = registro[idx["Angulo_vertical"]]
                Angulo_horizontal = registro[idx["Angulo_horizontal"]]
                obs.set_obstaculo(Numero, Label, Confianza, Distancia, Angulo_vertical, Angulo_horizontal)
                self.obstaculos[Numero]= obs
            print("Obstacles have been loaded successfully")
        except Error as error:
            print("Error al ejecutar el procedimiento: {}".format(error))
        finally:
            if (connection.is_connected()):
                cur.close()
                connection.close()
                print("MySQL connection is closed")
    
    def report_obstaculos(self):
        print(f"REPORTE DE OBSTÁCULOS")
        print(f"-------------------")
        for clave in self.obstaculos:
            print(self.obstaculos[clave])

class obstaculo:
    def __init__(self):
        self.numero = 0
        self.label = 0
        self.confianza = 0
        self.distancia = 0
        self.angulo_v = 0
        self.angulo_h = 0
    
    def __str__(self):
        return f"El obstáculo número {self.numero}, de label {self.label}, se encuentra a una distancia de {self.distancia} con ángulo vertical {self.angulo_v} y ángulo horizontal {self.angulo_h} (Confianza: {self.confianza})"
    
    def set_obstaculo(self, numero, label, confianza, distancia, angulo_v, angulo_h):
        self.numero = numero
        self.label = label
        self.confianza = confianza
        self.distancia = distancia
        self.angulo_v = angulo_v
        self.angulo_h = angulo_h

test = radar()
test.load_all_obstaculos()
test.report_obstaculos()