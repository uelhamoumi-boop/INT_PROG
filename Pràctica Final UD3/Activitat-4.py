import shutil
import os

try:
    shutil.move('./Directori-Original/Arxiu-a-moure.txt', './Directori-Desti')
    print(f"Archivo movido a: {'./Directori-Desti'}")
    fitxers = os.listdir('./Directori-Desti')
    print(f"Dins de ./Directori-Desti el que hi ha es : {fitxers}")

except FileNotFoundError:
    # Aquest error ix si el arxiu no existeix en la ruta de origen
    print(f"ERROR: No s'ha pogut trobar el fitxer en la ruta de origen'{'./Directori-Original'}")
    print("Asegurat de que el arxiu existeix en aquesta ruta avans de intentar menejarlo.")

except shutil.Error as e:
    # Aquest error bota si hi ha algun problema durant el procés de moure el arxiu
    print(f"ERROR: No s'ha pogut moure el arxiu")
    print(f"Detalls del error: {e}")
