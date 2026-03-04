notes = [5, 7, 9, 4, 6, 3, 1, 8, 2, 10]

for nota in notes:
    print(nota)

recompte_aprovats = 0
recompte_suspesos = 0

print("Notes aprovades:")

for nota in notes:
    if nota >= 5:
        print(f"- {nota}")
        recompte_aprovats += 1
    else:
        recompte_suspesos += 1

print (f"\nTotal d'aprovats: {recompte_aprovats}")
print (f"Total de suspesos:  {recompte_suspesos}")