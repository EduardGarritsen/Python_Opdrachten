studenten = {
    9.6: ['Eduard', 'Garritsen'],
    9.1: ['Nando', 'Reij'],
    6.9: ['Danny', 'Hoogerheide'],
    2.6: ['Nick','Beun'],
    9.3: ['Merlijn', 'van der Laan'],
    4.6: ['Jaimy', 'Gerrevink'],
    7.7: ['Rens', 'Koning'],
    1.8: ['Axel', 'Lap']
}

for student in studenten:
    if student >= 9.0:
        print(student, studenten[student])
