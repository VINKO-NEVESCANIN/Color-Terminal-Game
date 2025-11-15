# snake_colorama.py
import os
import random 
import time
from colorama import init, Fore, Back, Style

# Inicializa colorama (Windows)
init(autoreset=False)

WIDTH = 20
HEIGHT = 12
EMPTY = " "
SNAKE_CHAR = "■"   # o "O"
FOOD_CHAR = "●"

# Colores
SNAKE_COLOR = Fore.GREEN
FOOD_COLOR = Fore.RED
BORDER_COLOR = Fore.WHITE
TITLE_COLOR = Fore.CYAN
RESET = Style.RESET_ALL

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def crear_tablero():
    return [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

def dibujar_tablero(snake, food, score):
    clear()
    # título
    print(TITLE_COLOR + f" SNAKE - Score: {score} " + RESET)
    # borde superior
    print(BORDER_COLOR + "+" + "-"*WIDTH + "+" + RESET)
    for y in range(HEIGHT):
        row = "|"
        for x in range(WIDTH):
            if (x, y) == food:
                row += FOOD_COLOR + FOOD_CHAR + RESET
            elif (x, y) in snake:
                # cabeza diferente color
                if (x, y) == snake[0]:
                    row += Fore.YELLOW + SNAKE_CHAR + RESET
                else:
                    row += SNAKE_COLOR + SNAKE_CHAR + RESET
            else:
                row += EMPTY
        row += BORDER_COLOR + "|" + RESET
        print(row)
    # borde inferior
    print(BORDER_COLOR + "+" + "-"*WIDTH + "+" + RESET)

def colocar_comida(snake):
    while True:
        fx = random.randint(0, WIDTH-1)
        fy = random.randint(0, HEIGHT-1)
        if (fx, fy) not in snake:
            return (fx, fy)

def siguiente_pos(pos, direccion):
    x, y = pos
    if direccion == "W":
        return (x, y-1)
    if direccion == "S":
        return (x, y+1)
    if direccion == "A":
        return (x-1, y)
    if direccion == "D":
        return (x+1, y)
    return pos

def fuera_de_rango(pos):
    x, y = pos
    return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT

def juego():
    # serpiente: lista de tuplas, cabeza en índice 0
    mid_x, mid_y = WIDTH // 2, HEIGHT // 2
    snake = [(mid_x, mid_y), (mid_x-1, mid_y), (mid_x-2, mid_y)]
    direccion = "D"  # D = derecha por defecto
    food = colocar_comida(snake)
    score = 0

    instrucciones = (
        "Controles: W=arriba S=abajo A=izq D=der | Q para salir\n"
        "Pulsa la tecla y Enter para mover."
    )

    while True:
        dibujar_tablero(snake, food, score)
        print(instrucciones)
        move = input("Tu movimiento (W/A/S/D): ").strip().upper()
        if move == "Q":
            print("Saliendo... gracias por jugar.")
            break
        if move not in ("W","A","S","D"):
            print("Movimiento inválido. Usa W/A/S/D. Presiona Enter para continuar.")
            input()
            continue

        nueva_cabeza = siguiente_pos(snake[0], move)

        # colisión con muro
        if fuera_de_rango(nueva_cabeza):
            dibujar_tablero(snake, food, score)
            print(Fore.RED + "¡Has chocado contra el muro! GAME OVER." + RESET)
            break

        # colisión con cuerpo
        if nueva_cabeza in snake:
            dibujar_tablero(snake, food, score)
            print(Fore.RED + "¡Te mordiste a ti mismo! GAME OVER." + RESET)
            break

        # insertar nueva cabeza
        snake.insert(0, nueva_cabeza)

        # si come comida, no eliminar la cola y generar nueva comida
        if nueva_cabeza == food:
            score += 10
            food = colocar_comida(snake)
        else:
            # mover: eliminar cola
            snake.pop()

        # opcional: velocidad o pausa mínima
        time.sleep(0.05)

    print(f"Puntuación final: {score}")

if __name__ == "__main__":
    juego()
