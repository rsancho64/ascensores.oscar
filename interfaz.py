import tkinter as tk
from tkinter import messagebox
from edificio import Edificio

class AscensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Edificio con Ascensores")
        self.root.geometry("600x400")
        self.centrar_ventana(600, 400)
        
        self.opciones = ["Configurar Edificio", "Agregar Persona", "Iniciar Simulación", "Salir del Ascensor", "Mostrar Estado", "Salir"]
        self.indice_opcion = 0
        
        self.label_titulo = tk.Label(root, text="Sistema de Ascensores", font=("Arial", 18, "bold"))
        self.label_titulo.pack(pady=10)
        
        self.frame_menu = tk.Frame(root)
        self.frame_menu.pack()
        
        self.labels_opciones = []
        for opcion in self.opciones:
            label = tk.Label(self.frame_menu, text=opcion, font=("Arial", 14))
            label.pack(anchor="w", padx=20, pady=2)
            self.labels_opciones.append(label)
        
        self.actualizar_seleccion()
        
        self.root.bind("<Up>", self.mover_arriba)
        self.root.bind("<Down>", self.mover_abajo)
        self.root.bind("<Return>", self.seleccionar_opcion)
        
        self.edificio = None
        
    def centrar_ventana(self, ancho, alto):
        x_ventana = self.root.winfo_screenwidth() // 2 - ancho // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto // 2
        self.root.geometry(f"{ancho}x{alto}+{x_ventana}+{y_ventana}")
        
    def actualizar_seleccion(self):
        for i, label in enumerate(self.labels_opciones):
            if i == self.indice_opcion:
                label.config(bg="blue", fg="white")
            else:
                label.config(bg=self.root.cget("bg"), fg="black")
    
    def mover_arriba(self, event):
        self.indice_opcion = (self.indice_opcion - 1) % len(self.opciones)
        self.actualizar_seleccion()
    
    def mover_abajo(self, event):
        self.indice_opcion = (self.indice_opcion + 1) % len(self.opciones)
        self.actualizar_seleccion()
    
    def seleccionar_opcion(self, event):
        opcion = self.opciones[self.indice_opcion]
        if opcion == "Configurar Edificio":
            self.configurar_edificio()
        elif opcion == "Agregar Persona":
            self.agregar_persona()
        elif opcion == "Iniciar Simulación":
            self.iniciar_simulacion()
        elif opcion == "Salir del Ascensor":
            self.salir_del_ascensor()
        elif opcion == "Mostrar Estado":
            self.mostrar_estado()
        elif opcion == "Salir":
            self.root.quit()
    
    def configurar_edificio(self):
        num_plantas = int(self.obtener_input("Número de plantas:"))
        num_ascensores = int(self.obtener_input("Número de ascensores:"))
        capacidad = int(self.obtener_input("Capacidad de los ascensores (kg):"))
        self.edificio = Edificio(num_plantas, num_ascensores, capacidad)
        messagebox.showinfo("Éxito", "Edificio configurado correctamente.")
    
    def agregar_persona(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        id_persona = len(self.edificio.personas)
        origen = int(self.obtener_input("Planta de origen:"))
        destino = int(self.obtener_input("Planta de destino:"))
        peso = int(self.obtener_input("Peso de la persona (kg):"))
        ascensor_id = int(self.obtener_input("Seleccione el ID del ascensor:"))
        
        if 0 <= ascensor_id < len(self.edificio.ascensores):
            ascensor = self.edificio.ascensores[ascensor_id]
            self.edificio.agregar_persona(id_persona, origen, destino, peso, ascensor)
        else:
            messagebox.showerror("Error", "ID de ascensor inválido.")
    
    def iniciar_simulacion(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        messagebox.showinfo("Simulación", "Iniciando simulación de ascensores...")
        self.edificio.mostrar_estado()
    
    def salir_del_ascensor(self):
        messagebox.showinfo("Acción", "Función para salir del ascensor aún no implementada.")
    
    def mostrar_estado(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        self.edificio.mostrar_estado()
    
    def obtener_input(self, mensaje):
        return tk.simpledialog.askstring("Entrada", mensaje)

if __name__ == "__main__":
    root = tk.Tk()
    app = AscensorApp(root)
    root.mainloop()
