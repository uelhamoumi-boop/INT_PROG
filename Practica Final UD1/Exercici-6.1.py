a = [5, 10, 15]
b = 20

if 5 in a:
    b -= 5
if 10 in a:
    b -= 10
if 15 in a:
    b -= 15

print(b)
#Es comprova si els valors 5, 10, 15 estan dins la llista a. Cada vegada que la condició és certa, es resta el valor corresponent a b.b comença en 20, i es van restant 5, 10 i 15 → resultat final b = -10.