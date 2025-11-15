from colorama import Fore, Style

while True:
    print(Fore.RED + "🔥 MENÚ PRINCIPAL 🔥")
    print(Fore.YELLOW + "1. Atacar demonio")
    print(Fore.CYAN + "2. Cargar energía")
    print(Fore.GREEN + "3. Revisar salud")
    print(Fore.MAGENTA + "4. Salir")
    print(Style.RESET_ALL)
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print(Fore.RED + "💥 Ataque ejecutado!")
    elif opcion == "2":
        print(Fore.YELLOW + "🔋 Energía recargada.")
    elif opcion == "3":
        print(Fore.GREEN + "❤️ Salud al 100%.")
    elif opcion == "4":
        print(Fore.CYAN + "👋 Saliendo del sistema...")
        break
    else:
        print(Fore.WHITE + "Opción inválida, intenta de nuevo.")
    
    print(Style.RESET_ALL)
