leeftijd=int(input('Geef je leeftijd: '))
paspoort=input('Nederlands paspoort: ')

if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')

# hier begint opdracht 3_3
else:
    print('Helaas, je mag niet stemmen')
