import funcones as fc

listax=[]

listax=fc.obtener_lista()
listay=[]
listay=fc.obtener_angulos(600,600,listax)
#agregando valores cualquiera como distancia
for i in range(len(listay)):
    listay[i].append(i+20)

#escribiendo en el archivo
archivo=open("base_datos.txt","w")
for i in range(len(listay)):
    archivo.write("["+"\n")
    for j in range(0,7):
        archivo.write(str(listay[i][j])+"\n")
    archivo.write("]"+"\n")
archivo.close