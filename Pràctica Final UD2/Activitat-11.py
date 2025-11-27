import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filename= 'operacions.log',
    filemode='w'
)
try:
    num1= int(input("Disme el primer número: "))
    num2= int(input("Disme el segon número: "))
    suma= num1 + num2
    resta= num1 - num2
    multiplicacio= num1 * num2 
    divisio= num1 / num2
    print(f"La suma de {num1} + {num2} es igual a {suma}")
    print(f"La resta de  {num1} - {num2} es igual a {resta}")
    print(f"La multiplicació de {num1} * {num2} es igual a {multiplicacio}")
    print(f"La divisió de {num1} / {num2} es igual a {divisio}")
except ZeroDivisionError:
    print("El número 0 no es pot dividir, proba un altre")
except ValueError:
    print("Soles pots posar números enters")
