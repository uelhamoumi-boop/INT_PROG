# Programa d'anàlisi de temperatura i clima
print("=== ANALITZADOR DE TEMPERATURA I CLIMA ===\n")

# Demanar la temperatura a l'usuari
temperatura = float(input("Introdueix la temperatura (en graus Celsius): "))

# Demanar si està nuvolat
nuvolat_input = input("Està nuvolat? (si/no): ").lower()
nuvolat = nuvolat_input == "si"

print("\n--- RESULTAT ---")

# Analitzar les condicions amb estructures de selecció
if temperatura < 0:
    print("Fa un fred polar!")

elif temperatura >= 0 and temperatura <= 15:
    if nuvolat:
        print("Fa fred i el dia està trist.")
    else:
        print("Fa fresqueta però el sol alegra el dia.")

elif temperatura > 15 and temperatura <= 25:
    if nuvolat:
        print("Temperatura agradable, però potser ploga.")
    else:
        print("Dia perfecte per eixir a passejar!")

elif temperatura > 25 and temperatura <= 35:
    print("Fa calor, millor buscar ombra.")

else:  # temperatura > 35
    if nuvolat:
        print("Calor i humitat... una combinació infernal!")
    else:
        print("Fa una calor que fon les pedres!")

print("\n--- FI DE L'ANÀLISI ---")
