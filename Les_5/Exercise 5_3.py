filename = "Kaartnummers.txt"
infile = open('Kaartnummers.txt')
numLines = 0
kaartnummers = []

with open(filename, 'r') as file:
    for line in file:
        s = infile.readline()
        a, b = s.split(",")
        numLines += 1
        kaartnummers.append(a)

infile.close()

maxkaarnummer = max(kaartnummers)
indexnummer = kaartnummers.index(max(kaartnummers))
indexnummer += 1

print("Deze file telt " + str(numLines) + " regels")
print("Het grootste kaartnummer is: " + maxkaarnummer + " en dat staat op regel " + str(indexnummer))
