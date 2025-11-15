from colorama import Fore, Style

vida = 25

if vida > 60:
    print(Fore.GREEN + f"Vida: {vida}%")
elif vida > 30:
    print(Fore.YELLOW + f"Vida: {vida}%")
else:
    print(Fore.RED + f"Vida: {vida}% ⚠")
print(Style.RESET_ALL)
