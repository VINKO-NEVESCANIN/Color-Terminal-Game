import os
import random
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

# --- Configuración inicial ---
WIDTH = 20
HEIGHT = 12
SNAKE_CHAR = "■"
FOOD_CHAR = "●"
SNAKE_COLOR = Fore.GREEN
FOOD_COLOR = Fore.RED
HEAD_COLOR = Fore.YELLOW
RESET = Style.RESET_ALL
DELAY = 0.15  # velocidad inicial (menor = más rápido)

# --- Detecta sistema operativo ---
WINDOWS = os.name == "nt"
if WINDOWS:
    import msvcrt
else:
    import termios, tty, select

# --- Función limpiar pantalla ---
def clear():
    os.system("cls" if WINDOWS else "clear")

# --- Entrada sin bloqueo ---
def key_pressed():
    if WINDOWS:
        return msvcrt.kbhit()
    else:
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        return dr != []

def get_key():
    if WINDOWS:
        return msvcrt.getch().decode("utf-8").upper()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            if select.select([sys.stdin], [], [], 0.1)[0]:
                ch = sys.stdin.read(1).upper()
            else:
                ch = ""
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# --- Dibuja tablero ---
def draw(snake, food, score):
    clear()
    print(Fore.CYAN + f"🐍 SNAKE GAME - Puntos: {score}\n" + RESET)
    print("+" + "-" * WIDTH + "+")
    for y in range(HEIGHT):
        row = "|"
        for x in range(WIDTH):
            if (x, y) == snake[0]:
                row += HEAD_COLOR + SNAKE_CHAR + RESET
            elif (x, y) in snake:
                row += SNAKE_COLOR + SNAKE_CHAR + RESET
            elif (x, y) == food:
                row += FOOD_COLOR + FOOD_CHAR + RESET
            else:
                row += " "
        row += "|"
        print(row)
    print("+" + "-" * WIDTH + "+")
    print(Fore.YELLOW + "Controles: W=↑ S=↓ A=← D=→ | Q=Salir" + RESET)

# --- Nueva comida ---
def new_food(snake):
    while True:
        f = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        if f not in snake:
            return f

# --- Movimiento ---
def next_pos(pos, direction):
    x, y = pos
    if direction == "W":
        y -= 1
    elif direction == "S":
        y += 1
    elif direction == "A":
        x -= 1
    elif direction == "D":
        x += 1
    return x, y

def out_of_bounds(pos):
    x, y = pos
    return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT

# --- Juego principal ---
def play():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = "D"
    food = new_food(snake)
    score = 0
    delay = DELAY

    while True:
        draw(snake, food, score)

        # Entrada
        if key_pressed():
            key = get_key()
            if key in ("W", "A", "S", "D"):
                # Evitar giro en U
                if (direction, key) not in [("W","S"),("S","W"),("A","D"),("D","A")]:
                    direction = key
            elif key == "Q":
                print(Fore.CYAN + "👋 Gracias por jugar." + RESET)
                break

        # Siguiente posición
        new_head = next_pos(snake[0], direction)

        # Colisión con bordes o cuerpo
        if out_of_bounds(new_head) or new_head in snake:
            draw(snake, food, score)
            print(Fore.RED + "\n💀 GAME OVER 💀")
            print(Fore.YELLOW + f"Puntuación final: {score}")
            time.sleep(1)
            again = input(Fore.CYAN + "¿Jugar de nuevo? (S/N): ").upper()
            if again == "S":
                return play()
            else:
                break

        # Mover
        snake.insert(0, new_head)
        if new_head == food:
            score += 10
            food = new_food(snake)
            delay = max(0.05, delay - 0.005)  # más rápido
        else:
            snake.pop()

        time.sleep(delay)

# --- Entrada principal ---
if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        print("\n" + Fore.CYAN + "👋 Juego interrumpido por el usuario." + RESET)
