string = "leeg"

while string != "drop":
    string = input("Geef een string van vier letters: ")
    if string != "drop":
        aantal = str(len(string))
        print(string + " heeft " + aantal + " letters")

print("Inlezen van correcte string: drop is geslaagd")
