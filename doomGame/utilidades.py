import json
import os

# === Colores en consola ===
def print_color(texto, color):
    colores = {
        "rojo": "\033[91m",
        "verde": "\033[92m",
        "amarillo": "\033[93m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }
    print(f"{colores.get(color, '')}{texto}{colores['reset']}")

# === Limpiar consola ===
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

# === Guardar progreso con JSON ===
def guardar_progreso(jugador):
    with open("progreso.json", "w") as archivo:
        json.dump(jugador, archivo, indent=4)
    print_color("✅ Progreso guardado automáticamente.", "verde")
