# Exercici 3.3 - Funció amb valor per defecte (versió millorada)

# a) Estructura clara amb blocs
# b) Miniaplicació funcional
# c) Executable en qualsevol IDE (Thonny, IDLE, VS Code...)
# d) Variables d'entrada i càlcul
# e) Modificació i ús de variables
# f) Constants i literals (textos en print)
# g) Ús d'operadors aritmètics (+)
# h) Conversió de tipus explícita amb int()
# i) Comentaris al codi

# Definim una funció amb un valor per defecte
def suma(a, b=2):
    """Retorna la suma de dos nombres. El segon és opcional."""
    return a + b

# Entrada de dades
num1 = int(input("Introdueix el primer número: "))

# L’usuari pot decidir si vol introduir el segon valor
text = input("Vols introduir un segon número? (s/n): ")

if text.lower() == "s":
    num2 = int(input("Introdueix el segon número: "))
    resultat = suma(num1, num2)
else:
    # S'usa el valor per defecte (b=2)
    resultat = suma(num1)

# Resultat
print(f"El resultat de la suma és: {resultat}")
