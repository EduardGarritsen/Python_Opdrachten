lijst = eval(input("Geef lijst met minimaal 10 strings: "))
vier = []

for word in lijst:
    if len(word) == 4:
        vier.append(word)
    else:
        continue

print(vier)
