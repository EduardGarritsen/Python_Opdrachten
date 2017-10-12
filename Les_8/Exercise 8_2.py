import random

def monopolyworp():
    hoogstewaarde = 6
    laagstewaarde = 1
    x = random.randint(laagstewaarde, hoogstewaarde)
    y = random.randint(laagstewaarde, hoogstewaarde)
    z = x + y

    a = 0

    if a == 3:
        print(str(x)+ " + " + str(y) + " = (direct naar de gevangenis)")
    elif x == y:
        a += 1
        print(str(x)+ " + " + str(y) + " = " +str(z) + "(dubbel)")
    else:
        print(str(x)+ " + " + str(y) + " = " +str(z))




monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
