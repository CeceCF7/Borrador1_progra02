import mysql.connector
from mysql.connector import Error

#CREATING DATABASE
try:
    db_prueba = mysql.connector.connect( #CAMBIAR CREDENCIALES DE ACCESO
        host="localhost",
        user="root",
        password="password"
        )
    creation = db_prueba.cursor()
    creation.execute("CREATE DATABASE db_prueba")
    print("Database db_prueba has been created")
except Error as error:
    print("Database couldn't be created. Error: {}".format(error))
finally:
    if (db_prueba.is_connected()):
        creation.close()
        print("MySQL connection is closed")

#CREATING TABLES
try:
    connection = mysql.connector.connect( #CAMBIAR CREDENCIALES DE ACCESO
        host="localhost",
        user="root",
        passwd="password",
        db="db_prueba"
        )
    cur = connection.cursor()
    #Table: obstáculos
    cur.execute("CREATE TABLE obstaculos (numero INT AUTO_INCREMENT NOT NULL PRIMARY KEY, label VARCHAR(255) NOT NULL, confianza FLOAT(8,6) NOT NULL, distancia FLOAT(7,3) NOT NULL, angulo_vertical FLOAT(5,2) NOT NULL, angulo_horizontal FLOAT(5,2) NOT NULL)")
    print("Table obstaculos has been created")
    #Table: sensor
    cur.execute("CREATE TABLE sensor (ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, marca VARCHAR(255) NOT NULL, modelo VARCHAR(255) NOT NULL, angulo_vertical FLOAT(5,2) NOT NULL, angulo_horizontal FLOAT(5,2) NOT NULL, coordenadas VARCHAR(255) NOT NULL)")
    print("Table sensor has been created")
    #Table: cámara
    cur.execute("CREATE TABLE camara (ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, marca VARCHAR(255) NOT NULL, modelo VARCHAR(255) NOT NULL, angulo_vertical FLOAT(5,2) NOT NULL, angulo_horizontal FLOAT(5,2) NOT NULL, coordenadas VARCHAR(255) NOT NULL)")
    print("Table camara has been created")
    #Table: ESP32 board
    cur.execute("CREATE TABLE ESP32board (ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, marca VARCHAR(255) NOT NULL, modelo VARCHAR(255) NOT NULL)")
    print("Table ESP32board has been created")
except Error as error:
    print("Error creating Tables: {}".format(error))
finally:
    if (connection.is_connected()):
        cur.close()
        connection.close()
        print("MySQL connection is closed")
