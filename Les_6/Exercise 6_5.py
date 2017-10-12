for i in range(1,11):
    y = 1
    x = i * y
    for y in range(1,11):
        print(str(i) + " x " + str(y) + " = " + str(x))
        y += 1
        x = i * y

