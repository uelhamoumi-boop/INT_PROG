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
    logging.debug(f"La suma de {num1} + {num2} es igual a {suma}")
    logging.debug(f"La resta de  {num1} - {num2} es igual a {resta}")
    logging.debug(f"La multiplicació de {num1} * {num2} es igual a {multiplicacio}")
    logging.debug(f"La divisió de {num1} / {num2} es igual a {divisio}")
except ZeroDivisionError:
    logging.debug("El número 0 no es pot dividir, proba un altre")
except ValueError:
    logging.debug("Soles pots posar números enters")
