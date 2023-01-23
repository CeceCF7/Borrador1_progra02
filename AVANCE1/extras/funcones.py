def obtener_angulos(ancho, largo, Lista):
    
    for k in range(0,15):
        
        for j in range(0,15):
        
            for i in range(0,len(Lista)): 
        
                if (ancho*j/15<=Lista[i][2]<ancho*(j+1)/15) and (largo*k/15<=Lista[i][3]<largo*(k+1)/15):
                    Lista[i].append(6*(j+1)) #horizontal      
                    Lista[i].append(2*(k+1)) #vertical    
    return Lista

def obtener_lista():
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


    
