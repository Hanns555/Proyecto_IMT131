import tkinter as tk

#Ventana Secundaria: popup=tk.Toplevel()

class Ventana_Principal:
    def __init__(self):
        self.window=tk.Tk()
        self.Titulo()
        self.Tamanio()
        self.MenuTitulo()
        self.Botones()
    
    def Titulo(self):
        self.window.title("My App")
    def Tamanio(self):
        self.window.geometry("1000x750")
    def BucleAbierto(self):
        self.window.mainloop()

    #Botones Funciones
    def Comenzar(self):
        print("Comenzaste a jugar") 
    def VerRankings(self):
        print("Ver Ranking")
    def Salir(self):
        print("Saliendo")
        self.window.destroy()

    #Botones Caracteristicas
    def Botones(self):
        tk.Button(
            self.window, 
            text="Botón 1", 
            bg="red",    
            fg="white", 
            #Botton Caracteristicas
            font=("Arial", 16, "bold"),  
            width=20,                  
            height=2,              
            #Funcion Bontton     
            command=self.Comenzar
        ).pack(pady=20)
        tk.Button(
            self.window, 
            text="Botón 2", 
            bg="green",  
            fg="white",
            #Botton Caracteristicas
            font=("Arial", 16, "bold"),  
            width=20,                  
            height=2,  
            #Funcion Bontton 
            command=self.VerRankings
        ).pack(pady=15)
        tk.Button(
            self.window, 
            text="Salir", 
            bg="blue",   
            fg="white", 
            #Botton Caracteristicas
            font=("Arial", 16, "bold"),  
            width=20,                  
            height=2, 
            #Funcion Bontton 
            command=self.Salir
        ).pack(pady=15)

    def MenuTitulo(self):
        tk.Label(
            self.window, 
            text="MENU", 
            bg="blue",   
            fg="white", 
            #Botton Caracteristicas
            font=("Arial", 24, "bold"),  
            width=20,                  
            height=2, 
        ).pack(pady=(80, 40))


app=Ventana_Principal()



app.BucleAbierto()
