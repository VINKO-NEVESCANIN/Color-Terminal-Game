import random

demonios = [
    {"nombre": "Imp", "vida": 40, "ataque": 10},
    {"nombre": "Cacodemon", "vida": 70, "ataque": 15},
    {"nombre": "Hell Knight", "vida": 100, "ataque": 20},
    {"nombre": "Cyberdemon", "vida": 150, "ataque": 25}
]

def demonio_aleatorio():
    demonio = random.choice(demonios)
    print(f"\n👹 Aparece un {demonio['nombre']} del infierno...")
    return demonio.copy()
