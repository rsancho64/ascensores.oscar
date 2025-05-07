import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time
from edificio import Edificio

class AscensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Edificio con Ascensores")
        self.centrar_ventana(600, 500)
        
        self.edificio = None
        self.simulaciones = 0
        
        self.label_titulo = tk.Label(root, text="Sistema de Ascensores", font=("Arial", 18, "bold"))
        self.label_titulo.pack(pady=10)
        
        self.btn_configurar = tk.Button(root, text="Configurar Edificio", command=self.configurar_edificio)
        self.btn_configurar.pack(pady=5)
        
        self.btn_agregar = tk.Button(root, text="Agregar Persona", command=self.agregar_persona)
        self.btn_agregar.pack(pady=5)
        
        self.btn_simular = tk.Button(root, text="Iniciar Simulación", command=self.iniciar_simulacion)
        self.btn_simular.pack(pady=5)
        
        self.btn_reparar = tk.Button(root, text="Reparar Ascensor", command=self.reparar_ascensor)
        self.btn_reparar.pack(pady=5)

        self.btn_info_edificio = tk.Button(root, text="Mostrar Info del Edificio", command=self.mostrar_info_edificio)
        self.btn_info_edificio.pack(pady=5)
        
        self.info_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.info_label.pack(pady=10)
        
        self.text_estado = tk.Text(root, height=10, width=60)
        self.text_estado.pack(pady=10)
        
        self.actualizar_info()
    
    def centrar_ventana(self, ancho, alto):
        x_ventana = self.root.winfo_screenwidth() // 2 - ancho // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto // 2
        self.root.geometry(f"{ancho}x{alto}+{x_ventana}+{y_ventana}")
    
    def actualizar_info(self):
        if self.edificio:
            estado = "\n".join(str(ascensor) for ascensor in self.edificio.ascensores)
            self.text_estado.delete("1.0", tk.END)
            self.text_estado.insert(tk.END, f"Estado del Edificio:\n{estado}\n")
    
    def configurar_edificio(self):
        num_plantas = int(simpledialog.askstring("Entrada", "Número de plantas:", parent=self.root))
        num_ascensores = int(simpledialog.askstring("Entrada", "Número de ascensores:", parent=self.root))
        capacidad = int(simpledialog.askstring("Entrada", "Capacidad de los ascensores (kg):", parent=self.root))
        
        self.edificio = Edificio(num_plantas, num_ascensores, capacidad)
        self.actualizar_info()
        messagebox.showinfo("Éxito", "Edificio configurado correctamente.")
    
    def agregar_persona(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        
        origen = int(simpledialog.askstring("Entrada", "Planta de origen:", parent=self.root))
        destino = int(simpledialog.askstring("Entrada", "Planta de destino:", parent=self.root))
        peso = int(simpledialog.askstring("Entrada", "Peso de la persona (kg):", parent=self.root))
        ascensor_id = int(simpledialog.askstring("Entrada", "Seleccione el ID del ascensor:", parent=self.root))
        
        if 0 <= ascensor_id < len(self.edificio.ascensores):
            ascensor = self.edificio.ascensores[ascensor_id]
            self.edificio.agregar_persona(len(self.edificio.personas), origen, destino, peso, ascensor)
            self.actualizar_info()
        else:
            messagebox.showerror("Error", "ID de ascensor no válido.")
    
    def iniciar_simulacion(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        
        self.simulaciones += 1
        if random.randint(1, 5) == 3:
            ascensor_averiado = random.choice(self.edificio.ascensores)
            ascensor_averiado.capacidad = 0
            messagebox.showwarning("Fallo", f"El Ascensor {ascensor_averiado.id} se ha averiado!")
        
        for ascensor in self.edificio.ascensores:
            for persona in ascensor.ocupantes[:]:
                self.text_estado.insert(tk.END, f"Persona {persona.id} subiendo en Ascensor {ascensor.id}...\n")
                self.root.update()
                time.sleep(1)
                self.text_estado.insert(tk.END, f"Persona {persona.id} llegó a Planta {persona.destino}\n")
                self.root.update()
                ascensor.ocupantes.remove(persona)
        
        self.actualizar_info()
    
    def reparar_ascensor(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        
        ascensor_id = int(simpledialog.askstring("Entrada", "ID del ascensor a reparar:", parent=self.root))
        
        if 0 <= ascensor_id < len(self.edificio.ascensores):
            ascensor = self.edificio.ascensores[ascensor_id]
            ascensor.capacidad = 500  # Restaurando capacidad a un valor arbitrario
            messagebox.showinfo("Reparado", f"Ascensor {ascensor.id} reparado.")
            self.actualizar_info()
        else:
            messagebox.showerror("Error", "ID de ascensor no válido.")

    def mostrar_info_edificio(self):
        if not self.edificio:
            messagebox.showerror("Error", "Primero configura el edificio.")
            return
        
        info = (
            f"Plantas: {self.edificio.num_plantas}\n"
            f"Ascensores: {len(self.edificio.ascensores)}\n"
            f"Capacidad por ascensor: {self.edificio.capacidad} kg"
        )
        messagebox.showinfo("Información del Edificio", info)

if __name__ == "__main__":
    root = tk.Tk()
    app = AscensorApp(root)
    root.mainloop()

