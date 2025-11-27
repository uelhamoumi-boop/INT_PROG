suma = 0
comptador_parells = 0

for i in range(1, 7):
    if i % 2 == 0:
        suma = suma + i
        comptador_parells = comptador_parells + 1
    else:
        suma = suma - 1

print("Resultat final:")
print("suma =", suma)
print("comptador_parells =", comptador_parells)


#___________________________________________________________________________________
#| Iteració (i) | Condició i % 2 == 0 | Valor de suma | Valor de comptador_parells |
#|______________|_____________________|_______________|____________________________|
#|      1       |  Fals (1 % 2 == 1)	 |      -1       |             0           |
#|      2       |  Cert (2 % 2 == 0)	 |       1       |             1           |
#|      3       |  Fals (3 % 2 == 1)	 |       0       |             1           |
#|      4       |  Cert (4 % 2 == 0)	 |       4       |             2           |
#|      5       |  Fals (5 % 2 == 1)	 |       3       |             2           |
#|      6       |  Cert (6 % 2 == 0)	 |       9       |             3           |
