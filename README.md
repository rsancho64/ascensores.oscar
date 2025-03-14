# ascensores

Simulacion con python de un edificio con ascensores, plantas, personas, colas de espera en las plantas, botoneras en las plantas y botoneras en los ascensores

Quiero construir un sistema en python para ensayar simulaciones en un edificio con ascensores. 

Las clases iniciales son:

Edificio 
Ascensor
Planta
Persona
ColaDePersonas
Botonera
    botoneraDePlanta
    botoneraDeAscensor

Dame un codigo para todo ello en la "version 0"
Quiero un manejador propio en cada clase.

Quiero que el sistema tenga 
- modo CLI
- modo grafico en tkinter, y en este, un dashboard para el usuario que le permita el control total de las simulaciones: 
con:
- configuracion inicial (num. de ascensores, num, plantas, capacidades de los ascensores. )
- Inicio, parada, 
- configuracion de parametros en la generacion de eventos en las colas
- 



## notas v0:

Es una base funcional pero simple. Los ascensores se mueven en una dirección fija (por implementar lógica más compleja).
Falta la generación de eventos en las colas (se puede añadir en una versión futura).
El dashboard gráfico es básico pero permite control inicial.
Cada clase tiene su propio manejador (métodos como move, add_person, etc.).

