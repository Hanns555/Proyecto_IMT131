import tkinter as tk
from datos_juego import Jugador
from camara import CamaraJugador

class Ventana_Principal:
    def __init__(self):
        self.window = tk.Tk()
        self.Titulo()
        self.Tamanio()
        self.frame_menu = tk.Frame(self.window)
        self.frame_menu.pack()
        self.MenuTitulo()
        self.Botones()
    
    def Titulo(self):
        self.window.title("PROYECTO")

    def Tamanio(self):
        self.window.geometry("500x520")
        self.window.resizable(False, False)

    def BucleAbierto(self):
        self.window.mainloop()

    def Comenzar(self):
        self.frame_menu.pack_forget()
        self.PantallaRegistro()    

    def VerRankings(self):
        print("Ver Ranking")

    def Salir(self):
        print("Saliendo")
        self.window.destroy()

    def Botones(self):
        tk.Button(
            self.frame_menu, 
            text="Botón 1", 
            bg="red",    
            fg="white", 
            font=("Arial", 16, "bold"),  
            width=20,                  
            height=2,              
            command=self.Comenzar
        ).pack(pady=20)

        tk.Button(
            self.frame_menu,  
            text="Botón 2", 
            bg="green",  
            fg="white",
            font=("Arial", 16, "bold"),  
            width=20,                  
            height=2,  
            command=self.VerRankings
        ).pack(pady=15)

        tk.Button(
            self.frame_menu, 
            text="Salir", 
            bg="blue",   
            fg="white", 
            font=("Arial", 16, "bold"),  
            width=20,                  
            height=2, 
            command=self.Salir
        ).pack(pady=15)

    def MenuTitulo(self):
        tk.Label(
            self.frame_menu,  
            text="MENU", 
            bg="blue",   
            fg="white", 
            font=("Arial", 24, "bold"),  
            width=20,                  
            height=2, 
        ).pack(pady=(80, 40))

    #JUgador Registro
    def PantallaRegistro(self):
        self.frame_registro = tk.Frame(self.window)
        self.frame_registro.pack(pady=20)

        tk.Label(
            self.frame_registro,
            text="Registrar Jugador",
            font=("Arial", 18, "bold")
        ).pack(pady=(0, 20))

        tk.Label(self.frame_registro, text="Nombre:", font=("Arial", 12)).pack()
        self.entry_nombre = tk.Entry(self.frame_registro, font=("Arial", 12), width=25)
        self.entry_nombre.pack(pady=5)

        tk.Label(self.frame_registro, text="Carrera:", font=("Arial", 12)).pack()
        self.entry_carrera = tk.Entry(self.frame_registro, font=("Arial", 12), width=25)
        self.entry_carrera.pack(pady=5)

        tk.Button(
            self.frame_registro,
            text="Guardar",
            bg="green", fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            command=self.GuardarJugador
        ).pack(pady=15)

        tk.Button(
            self.frame_registro,
            text="Volver",
            bg="gray", fg="white",
            font=("Arial", 12),
            width=15,
            command=self.Volver
        ).pack()

    def GuardarJugador(self):
        Player = Jugador()
        nombre = self.entry_nombre.get()
        carrera = self.entry_carrera.get()
        Player.IngresarDatos(nombre, carrera)
        Player.GuardarDatosTXT()
        self.frame_registro.pack_forget()
        self.AbrirCamara()

    def AbrirCamara(self):
        self.camara = CamaraJugador()
        self.LoopCamara()

    def LoopCamara(self):
        salio = self.camara.LeerFrame()
        if salio:
            self.camara.CerrarCamara()
            self.frame_menu.pack()
        else:
            self.window.after(30, self.LoopCamara)

    def Volver(self):
        self.frame_registro.pack_forget()
        self.frame_menu.pack()


app = Ventana_Principal()
app.BucleAbierto()