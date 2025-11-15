from utilidades import print_color

def elegir_arma(jugador):
    print("\n=== ARMAS DISPONIBLES ===")
    print("1. Pistola (ataque +5)")
    print("2. Escopeta (ataque +15)")
    print("3. Lanzacohetes (ataque +25)")
    opcion = input("Elige tu arma: ")

    if opcion == "1":
        jugador["arma"] = "Pistola"
        jugador["ataque"] += 5
    elif opcion == "2":
        jugador["arma"] = "Escopeta"
        jugador["ataque"] += 15
    elif opcion == "3":
        jugador["arma"] = "Lanzacohetes"
        jugador["ataque"] += 25
    else:
        jugador["arma"] = "Puños"

    jugador["inventario"].append(jugador["arma"])
    print_color(f"Has equipado: {jugador['arma']}", "cyan")
