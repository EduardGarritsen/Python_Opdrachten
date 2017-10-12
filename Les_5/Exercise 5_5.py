def gemiddelde():
    zin = input('Type hier een zin: ')
    woorden = zin.split()
    gemiddeld = sum(len(woord) for woord in woorden) / len(woorden)
    print(gemiddeld)

gemiddelde()
