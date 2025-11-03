a = [5, 10, 15]
b = 20

if 5 in a:
    b -= 5
elif 10 in a:
    b -= 10
else:  
    b -= 15

print(b)
 # Només s’executa el primer if perquè és cert (5 in a). b passa de 20 a 15 i no entra en les altres condicions. Resultat final: b = 15.