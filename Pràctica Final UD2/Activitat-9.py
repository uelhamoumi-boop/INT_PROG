elements= ["poma", "pera", "taronja", "plàtan"]
seleccio= None
try:
    pos= int(input("Disme un número de el 0 al 3 i et dire a quina fruta correspon: "))
    seleccio= elements[pos]
    print(f"La fruta en la posicio {pos} es: {seleccio}")
except ValueError:
    print("Introdueix un numero sencer")
except IndexError:
    print("La fruta no existeix en la llista")
finally:
    print("Intent Completat")
    print(f"La longitud de la llista es: {len(elements)}")
    seleccio= None
    print("La variable seleccio a segut reiniciada a None")
