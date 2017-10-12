letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'A', 'A', 'C', 'C', 'B')

a = letters.count('A')-1
b = letters.count('B')-1
c = letters.count('C')-1

lijst = [a, b, c]

lijst.sort()

print(lijst)
