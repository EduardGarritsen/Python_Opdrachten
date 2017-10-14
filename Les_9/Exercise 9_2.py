import datetime
import csv

bestand = 'inloggers.csv'

vandaag = datetime.datetime.today()
date = vandaag.strftime("%a %d %b %Y %H:%M:%S")

#gebruik hier een herhalingslus:
naam = input("Wat is je achternaam? ")
voorl = input("Wat zijn je voorletters? ")
gbdatum = input("Wat is je geboortedatum? ")
email = input("Wat is je e-mail adres? ")
#wanneer de volgende persoon inlogt is onbekendmeteen naar file, dus schrijf

with open(bestand, 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow((date, naam, voorl, gbdatum, email))
