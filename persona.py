class Persona:
    def __init__(self, id_persona, origen, destino, peso):
        self.id = id_persona
        self.origen = origen
        self.destino = destino
        self.peso = peso
    
    def __repr__(self):
        return f"Persona-{self.id} ({self.origen} → {self.destino}, {self.peso}kg)"
