from jugador import crear_jugador, mostrar_estado, cargar_jugador
from demonios import demonio_aleatorio
from combate import batalla
from armas import elegir_arma
from utilidades import guardar_progreso, limpiar_consola, print_color

def juego():
    limpiar_consola()
    print_color("💀 BIENVENIDO A DOOM TERMINAL EDITION 💀", "rojo")

    jugador = cargar_jugador()  # Carga automática si hay progreso previo
    if not jugador:
        jugador = crear_jugador()
        elegir_arma(jugador)

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar demonio")
        print("2. Ver estado")
        print("3. Guardar y salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            enemigo = demonio_aleatorio()
            batalla(jugador, enemigo)
            guardar_progreso(jugador)

        elif opcion == "2":
            mostrar_estado(jugador)

        elif opcion == "3":
            guardar_progreso(jugador)
            print_color("🧩 Progreso guardado. ¡Hasta la próxima cacería, Marine!", "verde")
            break

if __name__ == "__main__":
    juego()
