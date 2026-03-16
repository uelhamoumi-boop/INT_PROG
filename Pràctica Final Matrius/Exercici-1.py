import numpy as np

temperatures = np.array(
    [
        [18, 20, 17],
        [19, 21, 18],
        [17, 19, 16],
        [22, 24, 20],
        [21, 23, 19],
        [15, 22, 18],
        [18, 20, 17],
    ]
)

print("La matriu sencera es:\n",temperatures)

print ("La temperatura de la 2a ciutat el 5é dia es:\n", temperatures [4,1],"º")
print ("La temperatura del 4t dia en la 1a ciutat:\n", temperatures [3,0], "º")

columna = [fila[2] for fila in temperatures]
print ("La temperatura de la 3a ciutat:\n", columna)

print ("La temperatura del 1r dia:\n", temperatures [0,0],"º")

print("La temperatura dels dos primers dies:\n", temperatures[:2, :])

print("Temperaturas dies 3 a 5 (1ª ciutat):\n", temperatures[2:5, 0])


# Les temperatures menors de 18 ºC
print("Aquestes temperatures son menors a 18 graus, quina gelor xe:\n",temperatures[temperatures < 18])

# Les temperatures majors de 20 ºC
print("Aquestes temperatures son de lo millor ni calor ni fred, per a viure chill:\n",temperatures[temperatures > 20])

# Les temperatures que siguen exactament 19 ºC
print("19 graus a voltes esta bé si fa sol:\n",temperatures[temperatures == 19])
