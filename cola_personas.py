class ColaDePersonas:
    def __init__(self):
        self.cola = []

    def agregar_persona(self, persona):
        self.cola.append(persona)

    def remover_persona(self):
        if self.cola:
            return self.cola.pop(0)
        return None

    def __repr__(self):
        return f"Cola: {self.cola}"