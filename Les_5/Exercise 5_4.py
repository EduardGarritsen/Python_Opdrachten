import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")

naam=input("Wat is uw naam:")

with open('Hardlopers.txt', 'a') as file:
    file.write(s + ", " + naam)


