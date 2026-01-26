import math

# Zmenili sme int na float, aby to bralo aj desatinné miesta
ciel = float(input("Zadaj kolko chces nasetrit: "))
vreckove = float(input("Zadaj kolko dostavas vreckove mesacne: "))
mam = float(input("Zadaj kolko mas: "))

if mam >= ciel:
    print("Gratulujem! Už máš nasporené dosť peňazí!")
else:
    chyba = ciel - mam
    mesiace = math.ceil(chyba / vreckove)
    
    # Používame :.2f, aby sa suma zobrazila pekne na dve desatinné miesta (ako peniaze)
    print(f"Ešte ti chýba nasetriť {chyba:.2f} eur.")
    print(f"Budeš musieť čakať ešte {mesiace} mesiacov.")