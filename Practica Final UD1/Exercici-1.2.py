# Exercici 1.2 - Comparar dos números
# Objectiu: demanar dos números i indicar quin és més gran, o si són iguals.

# (a) Blocs del programa: entrada > comparació > sortida
# (b) Forma part d’un projecte senzill d’aplicació en Python
# (c) Es pot provar en qualsevol IDE (Thonny, IDLE, VS Code...)

# Entrada de dades 
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

# Comparació
# (d) Variables numèriques per emmagatzemar dades d'usuari
# (g) Operadors de comparació: >, <, ==
if num1 > num2:
    print(f"El número {num1} és major que {num2}.")
elif num1 < num2:
    print(f"El número {num1} és menor que {num2}.")
else:
    print(f"Els dos números són iguals.")

# (h) Conversió de tipus explícita amb float()
# (i) Comentaris explicatius
