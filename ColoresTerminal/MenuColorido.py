from colorama import Fore, Back, Style

while True:
    print(Back.BLACK + Fore.CYAN + "==============================")
    print(Fore.YELLOW + "🎮 MENÚ PRINCIPAL DOOM SLAYER 🎮")
    print(Back.BLACK + Fore.CYAN + "==============================\n")

    print(Fore.RED + "1. Atacar demonio")
    print(Fore.GREEN + "2. Recargar energía")
    print(Fore.BLUE + "3. Consultar estado")
    print(Fore.MAGENTA + "4. Salir")
    print(Style.RESET_ALL)

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        print(Fore.RED + "💥 ¡Ataque ejecutado! Demonio eliminado.\n")
    elif opcion == "2":
        print(Fore.GREEN + "🔋 Energía recargada correctamente.\n")
    elif opcion == "3":
        print(Fore.BLUE + "📊 Estado: Vida 85%, Energía 70%.\n")
    elif opcion == "4":
        print(Fore.CYAN + "👋 Saliendo del sistema... ¡Hasta luego!\n")
        break
    else:
        print(Fore.WHITE + "⚠ Opción no válida. Intenta de nuevo.\n")

    print(Style.RESET_ALL)
