ruta_archivo1 = './Fitxers-per-provar/Fitxer-prova-exer2.1.txt'
ruta_archivo2 = './Fitxers-per-provar/Fitxer-prova-exer2.2.txt'
ruta_carpeta = './Fitxers-per-provar/guarda_arxiu'

texto_completo = ""
try:
    with open(ruta_archivo1, 'r') as fitxer_a:
        contenido_a = fitxer_a.read()
        texto_completo = texto_completo + contenido_a 

    with open(ruta_archivo2, 'r') as fitxer_b:
        contenido_b = fitxer_b.read()
        texto_completo = texto_completo + " " + contenido_b 
    
    with open(ruta_carpeta,'w') as fitxer:
        fitxer.write(f"La concatenació dels arxius es: {texto_completo}")

    print("El contenido de ambos ficheros es:")
    print(texto_completo)

except FileNotFoundError:
    print(f"Error: No se encontró uno de los archivos especificados.")
