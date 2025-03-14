import tkinter as tk
from building import Building

class GUISimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Ascensores")
        self.building = None
        self.running = False

        # Configuración inicial
        tk.Label(root, text="Número de plantas:").grid(row=0, column=0)
        self.num_floors = tk.Entry(root)
        self.num_floors.grid(row=0, column=1)
        self.num_floors.insert(0, "5")

        tk.Label(root, text="Número de ascensores:").grid(row=1, column=0)
        self.num_elevators = tk.Entry(root)
        self.num_elevators.grid(row=1, column=1)
        self.num_elevators.insert(0, "1")

        tk.Label(root, text="Capacidad de ascensores:").grid(row=2, column=0)
        self.capacity = tk.Entry(root)
        self.capacity.grid(row=2, column=1)
        self.capacity.insert(0, "5")

        # Botones de control
        tk.Button(root, text="Iniciar", command=self.start).grid(row=3, column=0)
        tk.Button(root, text="Parar", command=self.stop).grid(row=3, column=1)
        tk.Button(root, text="Estado", command=self.show_status).grid(row=3, column=2)

        # Área de estado
        self.status_text = tk.Text(root, height=10, width=50)
        self.status_text.grid(row=4, column=0, columnspan=3)

    def start(self):
        if not self.building:
            self.building = Building(
                int(self.num_floors.get()),
                int(self.num_elevators.get()),
                int(self.capacity.get())
            )
        self.running = True
        self.update()

    def stop(self):
        self.running = False

    def update(self):
        if self.running:
            self.building.run_simulation()
            self.show_status()
            self.root.after(1000, self.update)  # Actualiza cada segundo

    def show_status(self):
        self.status_text.delete(1.0, tk.END)
        status = self.building.get_status()
        self.status_text.insert(tk.END, str(status))