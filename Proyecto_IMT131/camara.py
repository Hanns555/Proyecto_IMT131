import cv2 as cv
from figuras_envivo import procesarImagen, obtenerContorno

class CamaraJugador:
    def __init__(self):
        self.captura = cv.VideoCapture(0)

    def LeerFrame(self):
        ret, imagen = self.captura.read()
        if ret:
            imagen = cv.flip(imagen, 1)
            imagen_procesada = procesarImagen(imagen)
            imagen = obtenerContorno(imagen, imagen_procesada)
            cv.imshow('Jugador', imagen)
        tecla = cv.waitKey(1) & 0xFF
        return tecla == ord('s')

    def CerrarCamara(self):
        self.captura.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    cam = CamaraJugador()