import random
a = 0
def monopolyworp():
    hoogstewaarde = 6
    laagstewaarde = 1
    x = random.randint(laagstewaarde, hoogstewaarde)
    y = random.randint(laagstewaarde, hoogstewaarde)
    z = x + y

    global a

    if a == 2 and x == y:
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
