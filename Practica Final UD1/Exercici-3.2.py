# Exercici 3.2 - Àrea d’un cercle
# Objectiu: calcular l’àrea d’un cercle a partir del radi.

# (a) Blocs: definició de funció > entrada > càlcul > sortida
# (b) Petit projecte funcional amb càlcul matemàtic
# (c) Executable en IDE

import math  # Llibreria per usar la constant PI (f)

# Definició de la funció
def area_cercle(radi):
    # (h) Conversió explícita per assegurar que el radi és numèric
    radi = float(radi)
    area = math.pi * (radi ** 2)
    return area

# Entrada i càlcul
radi_usuari = input("Introdueix el radi del cercle: ")
resultat = area_cercle(radi_usuari)

# Sortida
print(f"L’àrea del cercle és {resultat:.2f}")
