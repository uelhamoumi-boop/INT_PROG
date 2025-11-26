# Exercici 5.1 - Calculadora d’IMC

# (a) Blocs: entrada > càlcul > classificació > resultat
# (b) Projecte d’aplicació real (calculadora d’IMC)
# (c) Executable en IDE

# Entrada
pes = float(input("Introdueix el teu pes (kg): "))
altura = float(input("Introdueix la teua altura (m): "))

# Càlcul de l’IMC
IMC = pes / (altura ** 2)

# Classificació del resultat
if IMC < 18.5:
    print(f"IMC: {IMC:.2f} → Inferior al pes saludable.")
elif 18.5 <= IMC <= 24.9:
    print(f"IMC: {IMC:.2f} → Pes saludable.")
else:
    print(f"IMC: {IMC:.2f} →  Carlos Subiela?")
