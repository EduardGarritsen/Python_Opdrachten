def code(invoerstring):
    for string in invoerstring:
        string = chr(ord(string)+3)
        print(string, end='')

code("RutteAlkmaarDen Helder")
