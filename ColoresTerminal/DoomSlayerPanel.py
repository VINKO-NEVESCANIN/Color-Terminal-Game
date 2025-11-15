# doom_control_panel.py
from colorama import Fore, Back, Style
import random, time, os

# Función para limpiar pantalla
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar HUD de estado
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

# Función para registrar log en archivo
def registrar_evento(texto):
    with open("doom_log.txt", "a") as archivo:
        archivo.write(f"{texto}\n")

# Menú principal
def menu():
    while True:
        limpiar()
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
            print(Fore.CYAN + "📜 REGISTRO DE EVENTOS\n")
            try:
                with open("doom_log.txt", "r") as archivo:
                    for linea in archivo:
                        print(Fore.WHITE + linea.strip())
            except FileNotFoundError:
                print(Fore.RED + "⚠ No hay registros todavía.")
            input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")
        elif opcion == "4":
            print(Fore.CYAN + "👋 Cerrando sistema... Hasta pronto, Slayer.")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "⚠ Opción inválida.")
            time.sleep(1)

menu()
