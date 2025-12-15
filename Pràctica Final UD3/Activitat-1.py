nom = input("Digues el teu nom: ")
edat = int(input("Disme la teua edat: "))

try:
    with open('./Fitxers-per-provar/dades usuari.txt', 'w') as fitxer:
        fitxer.write(f"Nom: {nom}\n")
        fitxer.write(f"Edat: {edat}\n")

    with open('./Fitxers-per-provar/dades usuari.txt', 'r') as fitxer:
        contingut = fitxer.read()
        print("Contingut del fitxer (1a lectura):")
        print(contingut)

    ciutat = input("Disme de ont eres: ")
    
    with open('./Fitxers-per-provar/dades usuari.txt', 'a') as fitxer:
        fitxer.write(f"Ciutat: {ciutat}\n")

    with open('./Fitxers-per-provar/dades usuari.txt', 'r') as fitxer:
        contingut = fitxer.read()
        print("Contingut del fitxer (2a lectura):")
        print(contingut)

except FileNotFoundError:
    print('Error: No existeix el fitxer')
except PermissionError:
    print('Error: Permis denegat')
except ValueError:
    print('Error: Introdueix una edat numèrica vàlida')
