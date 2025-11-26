# Exercici 1.1 - Calculadora simple
# Objectiu: fer operacions bàsiques entre dos números i treballar amb textos.

# (a) Identificació dels blocs: entrada de dades, càlculs i sortida
# (b) Creació d'un petit projecte amb funcionalitat real
# (c) Pot executar-se en qualsevol entorn (IDLE, Thonny, VS Code...)

# (d) Variables: s'utilitzen per emmagatzemar números i resultats
# (f) Constants i literals: els missatges de text i els valors numèrics directes
# (g) Operadors: +, -, *, /, //, %
# (h) Conversions de tipus: int() i float()
# (i) Comentaris explicatius com aquest mateix

# Entrada de dades
# Demanem dos números, un enter i un flotant
num1 = int(input("Introdueix un número enter: "))
num2 = float(input("Introdueix un número decimal: "))

# Operacions aritmètiques
suma = num1 + num2
resta = num1 - num2
multiplicacio = num1 * num2
divisio = num1 / num2
divisio_entera = num1 // int(num2)     # conversió explícita a int
modul = num1 % num2

# Resultats 
print("\nResultats de les operacions:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicació:", multiplicacio)
print("Divisió:", divisio)
print("Divisió entera:", divisio_entera)
print("Mòdul:", modul)

# Concatenació de textos (f strings)
# Mostrem un missatge amb concatenació i literals
missatge = f"Els números que has posat son {num1} i {num2}. Gràcies per utilitzar la meua calculadora!"
print("\n" + missatge)
