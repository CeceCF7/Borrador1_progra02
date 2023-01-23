def obtener_angulos(ancho, largo, Lista):
    
    for k in range(0,15):
        
        for j in range(0,15):
        
            for i in range(0,len(Lista)): 
        
                if (ancho*j/15<=Lista[i][0][0]<=ancho*(j+1)/15) and (largo*k/15<=Lista[i][0][1]<=largo*(k+1)/15):
                    Lista[i].append(6*(j+1)) #horizontal      
                    Lista[i].append(2*(k+1)) #vertical
        
    return Lista

img_ancho=800
img_largo=800
Lista_centroides= [
   [(50,50), 0.5],
   [(300,50), 0.4],
   [(300,300), 0.3],
   [(800,400), 0.2],
   [(800,800), 0.7]
]

l2=obtener_angulos(img_ancho, img_largo, Lista_centroides)
print(l2)