import json

try:
  
    with open('../dades_exercici.json', 'r') as fitxer:
        dades = json.load(fitxer)

    dades[0]["assignatures"].append("cARLOS SUBIELA")

    with open('../dades_exercici.json', 'w') as fitxer:
        json.dump(dades, fitxer, indent=4)
        print("asignatura añadida.")

except FileNotFoundError:
    print("No s'ha trobat l'arxiu")