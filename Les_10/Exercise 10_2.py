import datetime

def verdubbelB(x):
    x = x + x
    print(x)

b = 7

verdubbelB(b)


time = datetime.datetime.today()
print(time.strftime(("%H:%M:%S")))

def f(y):
    return 2*y + 1

def g(x):
    return 5 + x + 10

print(f(3)+g(3))

