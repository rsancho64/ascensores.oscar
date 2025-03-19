from ascensor import Ascensor
from planta import Planta
from persona import Persona


class Edificio:
    def __init__(self, num_plantas, num_ascensores, capacidad_ascensor):
        self.plantas = [Planta(i) for i in range(num_plantas)]
        self.ascensores = [Ascensor(i, capacidad_ascensor) for i in range(num_ascensores)]
        self.personas = []
        self.num_plantas = num_plantas

    def agregar_persona(self, id_persona, origen, destino, peso, ascensor):
        if not (0 <= origen < self.num_plantas and 0 <= destino < self.num_plantas):
            print(f"⚠️ ERROR: Planta de origen ({origen}) o destino ({destino}) fuera de rango.")
            return
        
        if ascensor not in self.ascensores:
            print(f"⚠️ ERROR: Ascensor seleccionado no válido.")
            return
        
        persona = Persona(id_persona, origen, destino, peso)
        
        if (sum(p.peso for p in ascensor.ocupantes) + peso) <= ascensor.capacidad:
            ascensor.agregar_ocupante(persona)
            self.personas.append(persona)
            print(f"✅ Persona {id_persona} agregada en planta {origen} con destino {destino} (Peso: {peso}kg) en Ascensor {ascensor.id}")
        else:
            print("⚠️ ERROR: El ascensor seleccionado no puede soportar más peso. Seleccione otro ascensor.")
    
    def mostrar_estado(self):
        print("\n📊 Estado del edificio:")
        for ascensor in self.ascensores:
            ocupantes_info = ", ".join([str(p) for p in ascensor.ocupantes]) or "Vacío"
            print(f"🚀 Ascensor {ascensor.id} en Planta {ascensor.piso_actual} - Ocupantes: {ocupantes_info} (Carga: {sum(p.peso for p in ascensor.ocupantes)}/{ascensor.capacidad}kg)")
        for persona in self.personas:
            print(f"👤 {persona}")