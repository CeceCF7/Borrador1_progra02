import mysql.connector
from mysql.connector import Error

#RETRIEVING INFORMATION FROM DATABASE
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
                host="localhost",
                user="root",
                password="password",
                db="db_prueba"
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