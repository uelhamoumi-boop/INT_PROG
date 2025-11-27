print ("Programa per a comptar números, welcome :v")
numero= int(input("Disme un número: "))
positius= 0
while numero != 0:
    if numero > 0:
        positius= positius + 1
    numero= int(input("Fica un altre número: "))
print(positius)
