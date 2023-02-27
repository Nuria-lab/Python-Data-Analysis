##el script debe estar en la misma carpeta que está el entorno virtual
##seleccionar como intérprete el path en la carpeta del entorno virtual creado
# C:\Users\user\proyecto1\env_1\Scripts\python.exe   (ejemplo)


import cv2
import easyocr

reader = easyocr.Reader(["es"], gpu=True) #designar idioma en el que se leerá, y si se usará gpu

#la ruta a la imagen:
#usar barras dobles (\\), y poner el nombre del documento de imagen con su extensión
path=r"C:\\Users\\nuria\\Desktop\\PYTHON\\Visual Recognition\\letter_recogn_prueba_1_easyocr\\image_1.jpeg"

img = cv2.imread(path)   #el (path,0) significa escala de grises

result = reader.readtext(img)   #readtext es el método por el cual python interpretará los caracteres

for res in result:
    print("result", res)

    p0=res[0][0]
    p1=res[0][1]
    p2=res[0][2]
    p3=res[0][3]
    
    
    #ubicando los cuatro puntos de cada texto encontrado:
    img = cv2.circle(img,p0,2,(255,0,0),2) #azul
    img = cv2.circle(img,p1,2,(0,255,0),2) #verde
    img = cv2.circle(img,p2,2,(0,0,255),2) #rojo
    img = cv2.circle(img,p3,2,(0,0,0),2) #negro

    cv2.imshow("image", img)

    cv2.waitKey(0)




#cv2.imshow("image", img)
#cv2.waitKey(0)
cv2.destroyAllWindows()
