def kwadraten_som(x):
    s=0
    for getal in x:
        if getal >= 0:
            getal = getal**2
            s += getal
    return s

grondgetallen = [ 4, 5, 3, -81 ]

print(kwadraten_som(grondgetallen))
