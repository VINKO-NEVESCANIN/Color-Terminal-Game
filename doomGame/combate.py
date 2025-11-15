import random
from utilidades import print_color

def batalla(jugador, demonio):
    print_color(f"\n🔥 Te enfrentas al {demonio['nombre']}!", "rojo")

    while jugador["vida"] > 0 and demonio["vida"] > 0:
        ataque_jugador = jugador["ataque"] + random.randint(-3, 5)
        ataque_demonio = demonio["ataque"] + random.randint(-3, 3)

        demonio["vida"] -= ataque_jugador
        jugador["vida"] -= ataque_demonio

        print(f"\n{jugador['nombre']} ataca con {jugador['arma']} ({ataque_jugador} daño)")
        print(f"{demonio['nombre']} contraataca ({ataque_demonio} daño)")
        print(f"Vida del {demonio['nombre']}: {max(demonio['vida'], 0)} | Tu vida: {max(jugador['vida'], 0)}")

    if jugador["vida"] > 0:
        jugador["nivel"] += 1
        jugador["vida"] = min(100, jugador["vida"] + 20)
        jugador["demonios_eliminados"] += 1
        print_color(f"\n💀 ¡{demonio['nombre']} eliminado! Has subido al nivel {jugador['nivel']}!", "verde")
    else:
        print_color("\n☠️ Has caído... el infierno te reclama.", "rojo")
