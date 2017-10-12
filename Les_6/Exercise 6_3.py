invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

invoerlijst = invoer.split("-")

Hoogstewaarde = max(invoerlijst)
Laagstewaarde = min(invoerlijst)
Aantal = len(invoerlijst)
Totaal = sum(list(map(int, invoerlijst)))
Gemiddelde = Totaal / Aantal

print("Gesorteerde listvan ints: " + str(invoerlijst))
print("Grootste getal: " + str(Hoogstewaarde) + " en Kleinste getal: " + str(Laagstewaarde))
print("Aantal getallen: " + str(Aantal) + " en de Som van de getallen : " + str(Totaal))
print("Gemiddelde: " + str(Gemiddelde))
