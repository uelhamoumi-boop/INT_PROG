#   PART 1
with open('./Fitxers-per-provar/prueba.txt', 'w') as fitxer:
        fitxer.write(f"Primera línia")
        fitxer.write("\n")

with open('./Fitxers-per-provar/prueba.txt', 'w') as fitxer:
        fitxer.write(f"Segona línia")
        fitxer.write("\n")

#El que pasa es que primer se escruiu "primera línea" però 
#sols si no está el segon with, una volta estiga el segon with
#es machaca "primera línea" per "segona línia"

#   PART 2
#with open('./Fitxers-per-provar/prueba.txt', 'x') as fitxer:
        #fitxer.write(f"Tercera línia")
#Python me llança la exepció de "FileExistsError" lo cual significa
#que el arxiu ja exisiteix per lo cual no fa la acció de crear el arxiu
#però si borre el arxiu pasa el mateix, a menys que 
#o es borren o comenten els dos primers "with open", es a dir un resum complet
#que com estan els dos primers "with open" pues no es crea el arxiu per que
#ja existeix
#    AQUEST WITH EL COMENTE PER A QUE FUNCIONE TOT LO DE DESPUÉS
#   PER QUE SI NOS SEMPRE DONARA EL ERROR I NO DEIXARA SEGUIR EL EXERCICI

#   PART 3
with open('./Fitxers-per-provar/prueba.txt', 'a') as fitxer:
    fitxer.write(f"Quarta línia")
    fitxer.write("\n")
with open('./Fitxers-per-provar/prueba.txt', 'a') as fitxer:
    fitxer.write(f"Cinquena línia")
    fitxer.write("\n")
    fitxer.write(f"Sisena línia")
    fitxer.write("\n")
with open('./Fitxers-per-provar/prueba.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)

#Aquests 3 últims "with open" el que fan es:
#els dos primers escriuen al final de el arxiu, es a dir el que siga
#que li fiques que escriga ho escriu al final del arxiu
#l'últim  "with open" el que fa es escriure el contingut del arxiu

#   PART 4
with open('./Fitxers-per-provar/prueba.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)
    fitxer.close()

with open('./Fitxers-per-provar/proba.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)

#Obtenc el error de "FileNotFoundError" el qual significa que el arxiu no
#no s'ha trobat es a dir no existeix
