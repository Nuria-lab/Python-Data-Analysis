# importando archivo CSV y leyendo cada FILA
# los datos de una fila están separados por coma para indicar las columnas


# --- abriendo el csv - leyendo línea a línea - separando columnas por la coma - imprimiendo el valor de la columna

import os


os.chdir ('C:\\Users\\nuria\\Desktop\\Mi bebito fiu fiu')  #esto ponelo para trabajar dentro de la carpeta del data frame
nombre_archivo='mibebito.csv'
lista_de_observaciones=[]

with open(nombre_archivo,'r') as archivo:

    next(archivo,None)   #omite el encabezado

    for linea in archivo:   #va a leer cada fila. En csv, cada fila es como si fuera una sola celda y hay que separar las columnas
        linea=linea.rstrip() #omite saltos de línea
        
        separador=','
        lista=linea.split(',')   #listar separando cada fila por columnas (las comas separan las columnas)

        nombre=lista[0]   #en la posición 0 será código de inmueble. 1 zona. 2 m2. 3 observaciones
        observaciones=lista[3] #esta es la columna de observaciones
        codigo_inmueble=lista[0]

        lista_de_observaciones.append(observaciones)  #creando la nueva lista con las observaciones leídas

        # print (codigo_inmueble, observaciones)

print(lista_de_observaciones)  #acá las observaciones se pasaron a una lista (es una columna, con tanta cantidad de filas como inmuebles haya)

#--- con el código anterior se leen los datos de la columna 'observaciones'
#--- procesamiento de datos, y guardado en una lista (1 sola columna):

import re

columna_de_ambientes=[]    #lista donde se pondrá la cantidad de ambientes

for inmueble in lista_de_observaciones:

    if re.search('1 [ambientes.]', inmueble, re.IGNORECASE) or re.search('mono[ambientes.]', inmueble, re.IGNORECASE):
        #print(observaciones.index(inmueble),'1') 
        columna_de_ambientes.append(1)  #se guarda en float

    
    elif re.search('2 [ambientes.]', inmueble, re.IGNORECASE) or re.search('dos [ambientes.]', inmueble, re.IGNORECASE):
        #print(observaciones.index(inmueble),'2')
        columna_de_ambientes.append(2)
    
    elif re.search('3 [ambientes.]', inmueble, re.IGNORECASE) or re.search('tres [ambientes.]', inmueble, re.IGNORECASE):
        #print(observaciones.index(inmueble),3)
        columna_de_ambientes.append(3)

    elif re.search('4 [ambientes.]', inmueble, re.IGNORECASE) or re.search('cuatro [ambientes.]', inmueble, re.IGNORECASE):
        #print(observaciones.index(inmueble), '4')
        columna_de_ambientes.append(4)

    elif re.search('5 [ambientes.]', inmueble, re.IGNORECASE) or re.search('cinco [ambientes.]', inmueble, re.IGNORECASE):
        #print(observaciones.index(inmueble), '5')
        columna_de_ambientes.append(5)
    
    else:
        #print(observaciones.index(inmueble),'Sin datos')
        columna_de_ambientes.append(None)    #sí o sí tiene que estar esta (con 'sin dato', o 'none')
                                             #'Sin datos' provoca que la celda quede como cadena. Poniendo 'none' la celda queda vacía de dato. Según cómo lo tengan que procesar. Ojo con poner '0' (va a tirar errores muy feos)
print(columna_de_ambientes)  ##<--- en esta lista está la cantidad de ambientes ya clasificada

#---- agregando la columna al csv con pandas

import pandas as pd

datos=pd.read_csv('mibebito.csv')
data_frame=pd.DataFrame(datos)
# print(data_frame)    para verlo
data_frame=data_frame.assign(Ambientes=columna_de_ambientes)  #crea una nueva columna y pone los datos de la lista

data_frame.to_csv('datos con ambientesA.csv', sep=',')  #nuevo archivo con la nueva columna








