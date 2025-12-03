# Programa amb errors: classifica alumnes per edat i assistència
print("Classificador d'alumnes per edat i assistència")

n = int(input("Quants alumnes vols processar? "))
i = 0

while i < n:
    nom = str(input("Nom: "))
    edat = int(input("Edat: "))
    assist = str(input("Assistència (S/N): ")).lower()

    if edat < 12:
        categoria = "infantil"
    elif edat >= 12 and edat <= 18:
        categoria = "adolescent"
    elif edat >= 18 and edat <= 65:
        categoria = "adult"
    else:
        categoria = "jubilat"
    
    if assist in ["s", "si", "sí"]:
        estat = "present"
    elif assist in ["n", "no"]:
        estat = "absent"
    else:
        print("Resposta no vàlida. S'assumeix 'absent'")
        estat = "absent"
    
    print(nom, "-", categoria, "-", estat)
    i = i + 1