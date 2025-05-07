from edificio import Edificio

def mostrar_menu():
    print("\nSimulación de Edificio con Ascensores")
    print("1. Configurar Edificio")
    print("2. Agregar Persona")
    print("3. Iniciar Simulación")
    print("4. Salir de la simulación")
    print("5. Mostrar información del edificio")  

def main():
    edificio = None
    personas_agregadas = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            num_plantas = int(input("Número de plantas: "))
            num_ascensores = int(input("Número de ascensores: "))
            capacidad = int(input("Capacidad de los ascensores (kg): "))
            edificio = Edificio(num_plantas, num_ascensores, capacidad)
            print("Edificio configurado.")
        
        elif opcion == "2" and edificio:
            id_persona = len(personas_agregadas)
            origen = int(input("Planta de origen: "))
            destino = int(input("Planta de destino: "))
            peso = int(input("Peso de la persona (kg): "))
            
            print("Ascensores disponibles:")
            for ascensor in edificio.ascensores:
                print(ascensor)
            
            ascensor_id = int(input("Seleccione el ID del ascensor: "))
            if 0 <= ascensor_id < len(edificio.ascensores):
                ascensor = edificio.ascensores[ascensor_id]
                edificio.agregar_persona(id_persona, origen, destino, peso, ascensor)
                personas_agregadas.append(id_persona)
            else:
                print("⚠️ ERROR: ID de ascensor no válido.")
        
        elif opcion == "3" and edificio:
            edificio.mostrar_estado()

        elif opcion == "5" and edificio:  
            print(f"Edificio con {edificio.num_plantas} plantas y {len(edificio.ascensores)} ascensores.")
            print("Capacidad por ascensor:", edificio.capacidad)
        
        elif opcion == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida o configure el edificio primero.")

if __name__ == "__main__":
    main()

