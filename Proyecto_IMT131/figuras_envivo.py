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
    imagen_bordes = imagen
    #Identificar Figuras
    for c in cnts:
        #Ignorar Ruido ***
        area = cv.contourArea(c)
        if area < 1000 or area > imagen.shape[0] * imagen.shape[1] * 0.8:
            continue
        epsilon = 0.02*cv.arcLength(c,True)
        approx = cv.approxPolyDP(c,epsilon,True)
        x,y,w,h = cv.boundingRect(approx)
        lados = len(approx)
        print(f"Area: {area:.0f} | Lados detectados: {lados}")
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

def procesarImagen(imagen):
    imagen_gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    #Imagen Grises config 
    imagenBlur = cv.GaussianBlur(imagen_gris,(7,7),1)
    imagenCanny = cv.Canny(imagenBlur, 50, 200)
    imagenDilate = cv.dilate(imagenCanny, None, iterations=1)
    imagenErode = cv.erode(imagenDilate, None, iterations=1)
    imagenProcesada = imagenErode
    return imagenProcesada

#imagen = cv.imread('Imagenes/figurasColores.png')
#imagen_procesada = procesarImagen(imagen)
#imagen = obtenerContorno(imagen, imagen_procesada)
#cv.imshow('image', imagen)
#cv.waitKey(0)