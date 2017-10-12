namenDict = {}
b = 0

def namen():
    naam = input("Volgende naam: ")
    while naam != "":
        naam = input("Volgende naam: ")
        b += 1
        namenDict.update(naam, b)



namen()

print(namenDict)
