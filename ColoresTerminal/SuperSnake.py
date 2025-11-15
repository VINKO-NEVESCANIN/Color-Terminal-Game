import os
import random
import time
import sys
import json
from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)

# --- CONFIGURACIÓN ---
WIDTH = 20
HEIGHT = 12
SNAKE_CHAR = "■"
FOOD_CHAR = "●"
RESET = Style.RESET_ALL
BASE_DELAY = 0.15  # velocidad inicial

# Detectar sistema operativo
WINDOWS = os.name == "nt"
if WINDOWS:
    import msvcrt
else:
    import termios, tty, select

# --- LIMPIAR PANTALLA ---
def clear():
    os.system("cls" if WINDOWS else "clear")

# --- LOGO DOOM ---
def mostrar_logo():
    fig = Figlet(font="doom")
    print(Fore.RED + fig.renderText("SNAKE DOOM"))
    print(Fore.YELLOW + "🔥 DOOM SNAKE EDITION 🔥\n" + RESET)

# --- ENTRADA DE TECLAS ---
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

# --- DIBUJAR TABLERO ---
def draw(snake, food, score, color):
    clear()
    print(Fore.CYAN + f"🐍 SNAKE DOOM - Puntos: {score}\n" + RESET)
    print("+" + "-" * WIDTH + "+")
    for y in range(HEIGHT):
        row = "|"
        for x in range(WIDTH):
            if (x, y) == snake[0]:
                row += Fore.YELLOW + SNAKE_CHAR + RESET
            elif (x, y) in snake:
                row += color + SNAKE_CHAR + RESET
            elif (x, y) == food:
                row += Fore.RED + FOOD_CHAR + RESET
            else:
                row += " "
        row += "|"
        print(row)
    print("+" + "-" * WIDTH + "+")
    print(Fore.YELLOW + "Controles: W=↑ S=↓ A=← D=→ | Q=Salir" + RESET)

# --- COMIDA ---
def new_food(snake):
    while True:
        f = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        if f not in snake:
            return f

# --- MOVIMIENTO ---
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

# --- PUNTUACIONES JSON ---
def load_scores():
    try:
        with open("snake_scores.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_score(name, score):
    scores = load_scores()
    scores.append({"player": name, "score": score, "time": time.strftime("%Y-%m-%d %H:%M:%S")})
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:5]
    with open("snake_scores.json", "w") as f:
        json.dump(scores, f, indent=4)

def show_highscores():
    scores = load_scores()
    print(Fore.CYAN + "\n🏆 MEJORES PUNTUACIONES 🏆\n" + RESET)
    if not scores:
        print("No hay registros todavía.")
    else:
        for i, s in enumerate(scores, start=1):
            print(f"{i}. {s['player']} - {s['score']} puntos ({s['time']})")
    print()

# --- COLOR SEGÚN NIVEL ---
def get_snake_color(speed):
    if speed < 0.10:
        return Fore.MAGENTA
    elif speed < 0.13:
        return Fore.GREEN
    else:
        return Fore.BLUE

# --- JUEGO PRINCIPAL ---
def play(name):
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = "D"
    food = new_food(snake)
    score = 0
    delay = BASE_DELAY

    while True:
        color = get_snake_color(delay)
        draw(snake, food, score, color)

        if key_pressed():
            key = get_key()
            if key in ("W", "A", "S", "D"):
                if (direction, key) not in [("W","S"),("S","W"),("A","D"),("D","A")]:
                    direction = key
            elif key == "Q":
                print(Fore.CYAN + "👋 Saliendo del juego..." + RESET)
                time.sleep(1)
                break

        new_head = next_pos(snake[0], direction)
        if out_of_bounds(new_head) or new_head in snake:
            draw(snake, food, score, color)
            print(Fore.RED + "\n💀 GAME OVER 💀")
            print(Fore.YELLOW + f"Puntuación final: {score}")
            save_score(name, score)
            time.sleep(1)
            break

        snake.insert(0, new_head)
        if new_head == food:
            score += 10
            food = new_food(snake)
            delay = max(0.05, delay - 0.005)
        else:
            snake.pop()

        time.sleep(delay)

# --- MENÚ PRINCIPAL ---
def menu():
    while True:
        clear()
        mostrar_logo()
        print(Fore.GREEN + "1. Iniciar Juego")
        print(Fore.CYAN + "2. Ver Mejores Puntuaciones")
        print(Fore.MAGENTA + "3. Salir" + RESET)

        opcion = input("\nSelecciona una opción (1-3): ")
        if opcion == "1":
            name = input("Ingresa tu nombre: ") or "Jugador"
            play(name)
        elif opcion == "2":
            clear()
            mostrar_logo()
            show_highscores()
            input(Fore.YELLOW + "Presiona Enter para regresar al menú...")
        elif opcion == "3":
            print(Fore.CYAN + "\n👋 Gracias por jugar DOOM Snake Edition!" + RESET)
            break
        else:
            print(Fore.RED + "Opción inválida. Intenta de nuevo.")
            time.sleep(1)

# --- EJECUCIÓN ---
if __name__ == "__main__":
    menu()
