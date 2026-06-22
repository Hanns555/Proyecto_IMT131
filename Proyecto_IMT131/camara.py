import cv2 as cv
from figuras_envivo import procesarImagen, obtenerContorno

class CamaraJugador:
    def __init__(self):
        self.captura=cv.VideoCapture(0)
        self.AbrirCamara()

    def AbrirCamara(self):
        while self.captura.isOpened():
            ret, imagen = self.captura.read()
            if ret:
                bordes = procesarImagen(imagen)
                imagen = obtenerContorno(imagen, bordes)
                cv.imshow('Jugador', imagen)
                if cv.waitKey(1) & 0xFF == ord('s'):
                    break
            else:
                break
            
    def CerrarCamara(self):
        self.captura.release()

Jugador=CamaraJugador()

Jugador.CerrarCamara()