getal = 1
getallen = 0
som = 0

while getal != 0:
    getal = int(input("Geef een getal: "))
    getallen += 1
    som += int(getal)

getallen -= 1

print("Er zijn " + str(getallen) + " getallen ingevoerd, de som is: " + str(som))
