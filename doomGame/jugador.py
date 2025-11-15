import json
from utilidades import print_color

def crear_jugador():
    nombre = input("Ingresa tu nombre, Marine: ")
    jugador = {
        "nombre": nombre,
        "vida": 100,
        "ataque": 20,
        "nivel": 1,
        "arma": "Puños",
        "inventario": [],
        "demonios_eliminados": 0
    }
    print_color(f"\nBienvenido, {nombre}. ¡El infierno te espera!", "amarillo")
    return jugador

def mostrar_estado(jugador):
    print("\n=== ESTADO DEL MARINE ===")
    for k, v in jugador.items():
        print(f"{k.capitalize()}: {v}")

def cargar_jugador():
    try:
        with open("progreso.json", "r") as archivo:
            jugador = json.load(archivo)
            print_color(f"\n✅ Progreso cargado. Bienvenido de nuevo, {jugador['nombre']}!", "verde")
            return jugador
    except FileNotFoundError:
        return None
