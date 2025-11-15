from colorama import Fore, Style
import time
import random

# Valores iniciales
vida = random.randint(0, 100)
energia = random.randint(0, 100)

print(Fore.CYAN + "===========================")
print(Fore.YELLOW + "💀 DOOM SLAYER STATUS 💀")
print(Fore.CYAN + "===========================\n")

# --- Estado de vida ---
if vida > 70:
    print(Fore.GREEN + f"❤️ Vida: {vida}% - Excelente estado")
elif vida > 30:
    print(Fore.YELLOW + f"💛 Vida: {vida}% - Cuidado, te están dañando")
else:
    print(Fore.RED + f"💔 Vida: {vida}% - ¡Peligro! Salud crítica")

# --- Estado de energía ---
if energia > 70:
    print(Fore.BLUE + f"🔋 Energía: {energia}% - Armas listas")
elif energia > 30:
    print(Fore.MAGENTA + f"⚡ Energía: {energia}% - Nivel medio")
else:
    print(Fore.RED + f"⚠ Energía: {energia}% - ¡Recarga urgente!")

print(Style.RESET_ALL)
print("\nActualizando estado...")

# --- Simula actualización ---
time.sleep(5)
print(Fore.CYAN + "✅ Datos sincronizados con el sistema UAC.")
print(Style.RESET_ALL)
