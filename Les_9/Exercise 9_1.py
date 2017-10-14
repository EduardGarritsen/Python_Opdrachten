Aantal = int(input('Geef het aantal personen: '))

if(Aantal == abs(Aantal)):
    try:
        kosten = (4356 / Aantal)
        print(kosten)
    except ValueError:
        print("Gebruik cijfers voor het invoeren van het aantal!")
    except ZeroDivisionError:
        print('Delen door nul kan niet!')
    except :
        print('onjuiste invoer')

else:
    print("Negatieve getallen zijn niet toegestaan!")
