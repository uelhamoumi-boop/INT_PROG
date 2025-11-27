elements = ["poma", "pera", "taronja", "plàtan"]
seleccio = None
try:
    pos = int(
        input("Disme un numero del 0 al 3 y te diré a quina fruta correspon: "))
    assert pos >= 0 and pos < len(elements)
    seleccio = elements[pos]
    print(f"L'element en la posicio {pos} es: {seleccio}")
except AssertionError:
    print("Has de ficar un numero del 0 al 3: ")
except ValueError:
    print("Has de introduir un numero enter")
finally:
    print("Comprovació finalitzada")
    print(f"La longitud de la llista es: {len(elements)}")
    seleccio = None
    print("Seleccio reiniciada a None") 