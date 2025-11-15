# doom_control_panel_json.py
from colorama import Fore, Back, Style
import random, time, os, json

# --- Función para limpiar pantalla ---
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Función para mostrar logo con "DOOM" ---
def mostrar_logo():
    print(Fore.RED + r"""
██████╗  ██████╗  ██████╗ ███╗   ███╗
██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
██║  ██║██║   ██║██║   ██║██╔████╔██║
██║  ██║██║   ██║██║   ██║██║╚██╔╝██║
██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
""" + Fore.YELLOW + """
        DOOM SLAYER CONTROL PANEL
""" + Style.RESET_ALL)

# --- Función para cargar eventos desde archivo JSON ---
def cargar_registros():
    try:
        with open("doom_log.json", "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# --- Función para guardar eventos ---
def guardar_registros(registros):
    with open("doom_log.json", "w") as archivo:
        json.dump(registros, archivo, indent=4)

# --- Mostrar HUD con vida y energía ---
def mostrar_estado():
    vida = random.randint(0, 100)
    energia = random.randint(0, 100)
    print(Fore.CYAN + "===========================")
    print(Fore.YELLOW + "💀 DOOM SLAYER STATUS 💀")
    print(Fore.CYAN + "===========================\n")

    if vida > 70:
        print(Fore.GREEN + f"❤️ Vida: {vida}% - Excelente estado")
    elif vida > 30:
        print(Fore.YELLOW + f"💛 Vida: {vida}% - Cuidado, te están dañando")
    else:
        print(Fore.RED + f"💔 Vida: {vida}% - ¡Peligro! Salud crítica")

    if energia > 70:
        print(Fore.BLUE + f"🔋 Energía: {energia}% - Armas listas")
    elif energia > 30:
        print(Fore.MAGENTA + f"⚡ Energía: {energia}% - Nivel medio")
    else:
        print(Fore.RED + f"⚠ Energía: {energia}% - ¡Recarga urgente!")

    print(Style.RESET_ALL)
    print("\nSincronizando con UAC...")
    time.sleep(1.5)
    print(Fore.CYAN + "✅ Estado actualizado.\n" + Style.RESET_ALL)

# --- Registrar evento (usa JSON) ---
def registrar_evento(texto):
    registros = cargar_registros()
    evento = {
        "accion": texto,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    registros.append(evento)
    guardar_registros(registros)

# --- Mostrar registros desde JSON ---
def mostrar_registro():
    registros = cargar_registros()
    print(Fore.CYAN + "📜 REGISTRO DE EVENTOS\n")
    if not registros:
        print(Fore.RED + "⚠ No hay eventos registrados aún.")
    else:
        for r in registros:
            print(Fore.YELLOW + f"{r['timestamp']} - {Fore.WHITE}{r['accion']}")
    print(Style.RESET_ALL)

# --- Menú principal ---
def menu():
    while True:
        limpiar()
        mostrar_logo()

        print(Back.BLACK + Fore.RED + "🔥==============================🔥")
        print(Fore.YELLOW + "🎮 DOOM SLAYER CONTROL PANEL 🎮")
        print(Fore.RED + "🔥==============================🔥\n")

        print(Fore.GREEN + "1. Ver estado del Slayer")
        print(Fore.CYAN + "2. Registrar misión completada")
        print(Fore.MAGENTA + "3. Mostrar registro de log")
        print(Fore.RED + "4. Salir\n")

        opcion = input(Fore.WHITE + "Selecciona una opción (1-4): ")

        if opcion == "1":
            limpiar()
            mostrar_logo()
            mostrar_estado()
            registrar_evento("Consulta de estado realizada")
            input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")
        elif opcion == "2":
            mision = input("Nombre de la misión: ")
            registrar_evento(f"Misión completada: {mision}")
            print(Fore.GREEN + f"✅ Misión '{mision}' registrada.")
            time.sleep(1.5)
        elif opcion == "3":
            limpiar()
            mostrar_logo()
            mostrar_registro()
            input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")
        elif opcion == "4":
            print(Fore.CYAN + "👋 Cerrando sistema... Hasta pronto, Slayer.")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "⚠ Opción inválida.")
            time.sleep(1)

# --- Punto de entrada ---
if __name__ == "__main__":
    menu()
