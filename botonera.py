class Botonera:
    def __init__(self):
        self.botones = set()

    def presionar_boton(self, piso):
        self.botones.add(piso)

    def liberar_boton(self, piso):
        self.botones.discard(piso)

    def obtener_pisos_solicitados(self):
        return sorted(self.botones)

class BotoneraDePlanta(Botonera):
    def __init__(self):
        super().__init__()

class BotoneraDeAscensor(Botonera):
    def __init__(self):
        super().__init__()