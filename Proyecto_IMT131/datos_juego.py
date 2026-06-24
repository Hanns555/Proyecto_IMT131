class Jugador:
    def __init__(self):
        self._nombre=""
        self._carrera=""
        self.__puntos=0

    def IngresarDatos(self,nombre,carrera):
        self._nombre=nombre
        self._carrera=carrera
        
    def Mostrar(self):
       print(self._nombre,self._carrera)

    def GuardarDatosTXT(self):
        with open("datos.txt","a") as file:
            file.write(f"{self._nombre},{self._carrera}\n")
