import cv2 as cv
import multiprocessing as multicore

#ver la version del open cv - print(cv.__version__)
#Para ver la imagen se usa:
#cv.imshow('gris',bordes)
#cv.waitKey(0)
#Para verificar que si detecta contornos - cv.drawContours(imagen, cnts, -1, (255,0,0), 3)

def obtenerContorno(imagen,bordes):
    #Encotrar los contornos de las figuras
    cnts,_ = cv.findContours(bordes, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #Identificar Figuras
    for c in cnts:
        epsilon = 0.01*cv.arcLength(c,True)
        approx = cv.approxPolyDP(c,epsilon,True)
        x,y,w,h = cv.boundingRect(approx)
        match len(approx):
            case 3:
                cv.putText(imagen,'Triangulo', (x,y-5),1,1,(0,0,255),1)
            case 4:
                aspect_ratio = float(w)/h
                if aspect_ratio > 0.95 and aspect_ratio < 1.05:
                    cv.putText(imagen,'Cuadrado', (x,y-5),1,1,(0,0,255),1)
                else:
                    cv.putText(imagen,'Rectangulo', (x,y-5),1,1,(0,0,255),1)
            case 6:
                cv.putText(imagen,'Hexagono', (x,y-5),1,1,(0,0,255),1)
            case _ if len(approx) > 10:  
                cv.putText(imagen, 'Circulo', (x, y-5), 1, 1, (0,0,255), 1)
        imagen_bordes=cv.drawContours(imagen, [approx], 0, (0,255,0), 3)
    return imagen_bordes

imagen = cv.imread('Imagenes/figurasColores.png')
imagen_gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
#Imagen Grises config 
bordes = cv.Canny(imagen_gris, 10, 150)
bordes = cv.dilate(bordes, None, iterations=1)
bordes = cv.erode(bordes, None, iterations=1)
imagen = obtenerContorno(imagen, bordes)
cv.imshow('image', imagen)
cv.waitKey(0)