num = float(input("Comença a escriure números:" ""))
contador=0
while num != 0 :
    if(num%2 == 0):
        contador+=1
    num = float(input("Un altre número: " ""))

print("Tinc "+str(contador)+" numeros parells")
