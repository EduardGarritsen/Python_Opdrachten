def gemiddelde_per_student(studentencijfers):
    for x in studentencijfers:
        y = sum(studentencijfers[x])/3
        print(y)
#def gemiddelde_van_alle_studenten(studentencijfers):

    #return antw

studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

print(gemiddelde_per_student(studentencijfers))
#print(gemiddelde_van_alle_studenten(studentencijfers))
