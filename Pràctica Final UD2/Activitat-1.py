print("Benvolgut al meu programa per a el oratge!")
temp=int(input("Perfavor disme la temperatura actual en graus celsius:"))

if temp < 0:
    print("Fa un fred polar!")

if temp >= 0 and temp <= 15:
    nuvols=str(input("Hi han núvols? "))
    if nuvols == "si":
        print("Fa fred i el dia esta trist")
    if nuvols == "no":
        print("Fa fresqueta però el sol alegra el dia.")

if temp >= 16 and temp <= 25:
    nuvols=str(input("Hi han núvols? "))
    if nuvols == "si":
        print("Temperatura agradable, però potser ploga.")
    if nuvols == "no":
        print("Dia perfecte per eixir a passejar!")

if temp >= 26 and temp <= 35:
    print("Fa calor, millor buscar ombra")

if temp > 35:
    nuvols=str(input("Hi han núvols? "))
    if nuvols == "si":
        print("Calor i humitat... una combinació infernal!")
    if nuvols == "no":
        print("Fa una calor que fon les pedres!")
