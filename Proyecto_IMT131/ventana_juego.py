import tkinter as tk

class Ventana_Principal:
    def __init__(self):
        self.window = tk.Tk()
        self.Titulo()
        self.Tamanio()
        self.Configurar()
        self.MenuTitulo()
        self.Botones()

    def Titulo(self):
        self.window.title("My App")

    def Tamanio(self):
        self.window.geometry("500x520")
        self.window.resizable(False, False)

    def Configurar(self):
        # Fondo oscuro en toda la ventana
        self.window.configure(bg="#1a1a2e")

    def BucleAbierto(self):
        self.window.mainloop()

    # Funciones
    def Comenzar(self):
        print("Comenzaste a jugar")
    def VerRankings(self):
        print("Ver Ranking")
    def Salir(self):
        self.window.destroy()

    def MenuTitulo(self):
        frame_titulo = tk.Frame(self.window, bg="#16213e", padx=40, pady=18)
        frame_titulo.pack(pady=(80, 10))

        tk.Label(
            frame_titulo,
            text="Proyecto",
            bg="#16213e",
            fg="#e8e8f0",
            font=("Arial", 26, "bold"),
        ).pack()

        tk.Label(
            frame_titulo,
            text="Hanns Juan Juliana",
            bg="#16213e",
            fg="#555577",
            font=("Arial", 9),
        ).pack(pady=(2, 0))

    def Botones(self):
        frame = tk.Frame(self.window, bg="#1a1a2e")
        frame.pack(pady=30)

        botones = [
            ("▶  Comenzar",   "#533ab7", "#cdc8f5", self.Comenzar),
            ("🏆  Ver Rankings", "#0f6e56", "#9fe1cb", self.VerRankings),
            ("✕  Salir",      "#2c2c2a", "#b4b2a9", self.Salir),
        ]

        for texto, bg, fg, cmd in botones:
            tk.Button(
                frame,
                text=texto,
                bg=bg,
                fg=fg,
                activebackground=bg,
                activeforeground=fg,
                relief="flat",
                font=("Arial", 13, "bold"),
                width=22,
                height=2,
                cursor="hand2",
                command=cmd,
            ).pack(pady=8)

app = Ventana_Principal()
app.BucleAbierto()