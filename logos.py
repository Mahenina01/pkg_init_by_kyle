import os,sys , time, pyfiglet

from termcolor import colored


def afficher(logo, delai=0.1):
    for lettre in logo:
        sys.stdout.write(lettre)
        sys.stdout.flush()
        time.sleep(delai)
    print("  ")
print("=="*40)
logo = pyfiglet.figlet_format("By Nehemia", font="speed")

colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
background = "on_grey" 


for i, line in enumerate(logo.split("\n")):
    affichage_color = colored(line, colors[i % len(colors)], background)
    afficher(affichage_color, delai=0.003)
print("=="*40)
