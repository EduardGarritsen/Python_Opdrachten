infile = open('Kaartnummers.txt')
x = 0
while x < 6:
    s = infile.readline()
    a, b = s.split(",")
    print(b + "heeft kaartnummer:" + a)
    x += 1

infile.close()
