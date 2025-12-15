import csv

try:
  
    with open('./dades_exercici.csv', 'r') as fitxer:
        lector = csv.reader(fitxer)
        dades_originals = list(lector)
        print(dades_originals)

    nou_alumne = ["Ubay", "17", "SMX-A-2"]
    dades_originals.append(nou_alumne)
 
    with open('./dades_exercici.csv', 'a') as fitxer:
        escriptor = csv.writer(fitxer)
        escriptor.writerow(nou_alumne)
   

except Exception as e:
    print("Error amb el fitxer CSV:", e)