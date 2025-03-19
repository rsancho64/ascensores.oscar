class Ascensor:
    def __init__(self, id, capacidad):
        self.id = id
        self.capacidad = capacidad
        self.ocupantes = []
        self.piso_actual = 0
    
    def agregar_ocupante(self, persona):
        self.ocupantes.append(persona)
    
    def __repr__(self):
        return f"Ascensor-{self.id} en Piso-{self.piso_actual} ({sum(p.peso for p in self.ocupantes)}kg/{self.capacidad}kg)"
