import tkinter as tk
from tkinter import messagebox, simpledialog
from edificio import Edificio

class AscensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Edificio con Ascensores")
        self.centrar_ventana(600, 400)
        
        self.edificio = None
        self.personas_agregadas = []
        
        self.crear_widgets()
        self.configurar_eventos()

    def centrar_ventana(self, ancho, alto):
        x_ventana = self.root.winfo_screenwidth() // 2 - ancho // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto // 2
        self.root.geometry(f"{ancho}x{alto}+{x_ventana}+{y_ventana}")
    
    def crear_widgets(self):
        self.label_titulo = tk.Label(self.root, text="Sistema de Ascensores", font=("Arial", 18, "bold"))
        self.label_titulo.pack(pady=10)

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack()

        opciones = ["Configurar Edificio", "Agregar Persona", "Iniciar Simulación", "Mostrar Estado", "Salir"]
        self.botones = []

        for opcion in opciones:
            boton = tk.Button(self.frame_botones, text=opcion, font=("Arial", 12), width=20, command=lambda op=opcion: self.ejecutar_opcion(op))
            boton.pack(pady=5)
            self.botones.append(boton)

        self.info_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.info_label.pack(pady=10)
    
    def configurar_eventos(self):
        self.root.bind("<Return>", lambda event: self.botones[0].invoke())
    
    def ejecutar_opcion(self, opcion):
        if opcion == "Configurar Edificio":
            self.configurar_edificio()
        elif opcion == "Agregar Persona":
            self.agregar_persona()
        elif opcion == "Iniciar Simulación":
            self.iniciar_simulacion()
        elif opcion == "Mostrar Estado":
            self.mostrar_estado()
        elif opcion == "Salir":
            self.root.quit()
    
    def configurar_edificio(self):
        num_plantas = self.obtener_input("Número de plantas:")
        num_ascensores = self.obtener_input("Número de ascensores:")
        capacidad = self.obtener_input("Capacidad de los ascensores (kg):")
        
        if num_plantas and num_ascensores and capacidad:
            self.edificio = Edificio(int(num_plantas), int(num_ascensores), int(capacidad))
            self.actualizar_info()
            messagebox.showinfo("Éxito", "Edificio configurado correctamente.")
    
    def agregar_persona(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return

        origen = self.obtener_input("Planta de origen:")
        destino = self.obtener_input("Planta de destino:")
        peso = self.obtener_input("Peso de la persona (kg):")
        ascensor_id = self.obtener_input("Seleccione el ID del ascensor:")
        
        if origen and destino and peso and ascensor_id:
            ascensor_id = int(ascensor_id)
            if 0 <= ascensor_id < len(self.edificio.ascensores):
                self.edificio.agregar_persona(len(self.personas_agregadas), int(origen), int(destino), int(peso), self.edificio.ascensores[ascensor_id])
                self.personas_agregadas.append(len(self.personas_agregadas))
                self.actualizar_info()
                messagebox.showinfo("Éxito", "Persona agregada correctamente.")
            else:
                messagebox.showerror("Error", "ID de ascensor no válido.")
    
    def iniciar_simulacion(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        messagebox.showinfo("Simulación", "Iniciando simulación de ascensores...")
        self.mostrar_estado()
    
    def mostrar_estado(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        estado = "\n".join([str(ascensor) for ascensor in self.edificio.ascensores])
        self.info_label.config(text=f"Estado del edificio:\n{estado}")
        messagebox.showinfo("Estado del Edificio", estado)
    
    def actualizar_info(self):
        if self.edificio:
            self.info_label.config(text=f"Edificio: {self.edificio.num_plantas} plantas, {len(self.edificio.ascensores)} ascensores")
    
    def obtener_input(self, mensaje):
        return simpledialog.askstring("Entrada", mensaje, parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = AscensorApp(root)
    root.mainloop()
