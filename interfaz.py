import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from edificio import Edificio
from persona import Persona

class AscensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Edificio con Ascensores")
        self.centrar_ventana(600, 400)

        self.opciones = ["Configurar Edificio", "Agregar Persona", "Iniciar Simulación", "Mostrar Estado", "Salir"]
        self.indice_opcion = 0
        self.simulaciones_realizadas = 0

        self.label_titulo = tk.Label(root, text="Sistema de Ascensores", font=("Arial", 18, "bold"))
        self.label_titulo.pack(pady=10)

        self.frame_menu = tk.Frame(root)
        self.frame_menu.pack()

        self.labels_opciones = []
        for opcion in self.opciones:
            label = tk.Label(self.frame_menu, text=opcion, font=("Arial", 14))
            label.pack(anchor="w", padx=20, pady=2)
            label.bind("<Button-1>", self.click_opcion)
            self.labels_opciones.append(label)

        self.info_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.info_label.pack(pady=10)

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

    def seleccionar_opcion(self, event=None):
        opcion = self.opciones[self.indice_opcion]
        self.ejecutar_opcion(opcion)

    def click_opcion(self, event):
        for i, label in enumerate(self.labels_opciones):
            if event.widget == label:
                self.indice_opcion = i
                self.actualizar_seleccion()
                self.seleccionar_opcion()

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
            self.edificio.agregar_persona(len(self.edificio.personas), int(origen), int(destino), int(peso), self.edificio.ascensores[int(ascensor_id)])
            self.actualizar_info()
            messagebox.showinfo("Éxito", "Persona agregada correctamente.")

    def iniciar_simulacion(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return

        self.simulaciones_realizadas += 1
        if random.randint(1, 5) == 3:
            ascensor = random.choice(self.edificio.ascensores)
            messagebox.showerror("Fallo en el sistema", f"El Ascensor {ascensor.id} se ha averiado y está fuera de servicio.")
            self.edificio.ascensores.remove(ascensor)
        
        ventana_simulacion = tk.Toplevel(self.root)
        ventana_simulacion.title("Simulación en curso")
        ventana_simulacion.geometry("400x300")
        texto = tk.Label(ventana_simulacion, text="Simulación en proceso...", font=("Arial", 14))
        texto.pack(pady=20)
        
        for persona in self.edificio.personas:
            for ascensor in self.edificio.ascensores:
                if persona in ascensor.ocupantes:
                    mensaje = f"Persona {persona.id} viajando en Ascensor {ascensor.id}"
                    texto.config(text=mensaje)
                    ventana_simulacion.update()
                    self.root.after(2000)
        
        messagebox.showinfo("Simulación", "La simulación ha finalizado.")
        ventana_simulacion.destroy()

    def mostrar_estado(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        estado = "\n".join(str(ascensor) for ascensor in self.edificio.ascensores)
        messagebox.showinfo("Estado del Edificio", estado)

    def actualizar_info(self):
        if self.edificio:
            self.info_label.config(
                text=f"Edificio: {self.edificio.num_plantas} plantas, {len(self.edificio.ascensores)} ascensores"
            )

    def obtener_input(self, mensaje):
        return simpledialog.askstring("Entrada", mensaje, parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = AscensorApp(root)
    root.mainloop()
