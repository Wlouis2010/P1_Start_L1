# Schrijf een Python-programma dat aan de gebruiker twee vragen stelt:
# 1. Hoeveel mensen gaan er naar het concert?
# 2. Wat is de prijs per ticket?
#
# Bereken het totaalbedrag en print dat bedrag.
#
# Voorbeeldinvoer:
# Hoeveel mensen gaan er naar het concert?  3
# Wat is de prijs per ticket?  10.55
#
# Voorbeelduitvoer:
# De totale prijs bedraagt 31.65 euro.
print('hallo, welkom')

prijs = float(input("Wat is je de prijs van je tickets in euro's? "))
Aantal = int(input("Hoeveel tickets wil je kopen? "))
print("je moet ",   prijs * Aantal , "euro betalen")