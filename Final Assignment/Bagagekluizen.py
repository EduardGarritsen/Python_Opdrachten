def toon_aantal_kluizen_vrij():
    file = open("kluizen.txt", "r")
    content = file.readlines()
    Aantal = 12
    ingebruik = 12
    for line in content:
        if line >= (";/n"):
            ingebruik -= 1
    Vrijekluizen = Aantal - ingebruik
    print(Vrijekluizen)

def nieuwe_kluis():
    file = open("kluizen.txt", "r")
    content = file.readlines()
    for lines in content:
        print(lines)

    password = input("type een wachtwoord")
    content[0] = lines[0] + ";" + password

    filew = open("kluizen.txt", "w")
    for line in filew:
        if line.contains('1;'):
            newline = line.replace('1;', content)
    filew.close()

optie = int(input("Kies een optie 1-3:"))
if optie == 1 or optie == 2 or optie == 3:
    if optie == 1:
        toon_aantal_kluizen_vrij()
    elif optie == 2:
        nieuwe_kluis()
else:
    print("deze optie is ongeldig")

