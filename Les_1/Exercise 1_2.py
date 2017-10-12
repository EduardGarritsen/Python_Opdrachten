a = len('Supercalifragilisticexpialidocious')
print(a)

b = 'Supercalifragilisticexpialidocious'
if 'ice' in b:
   print('success')

c1 = len('Antidisestablishmentarianism')
c2 = len('Honorificabilitudinitatibus')

c = c1 > c2
print(c)

d = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
d.sort()
print('Als eerst komt ' + d[0] + ' en als laats komt ' + d[-1])
