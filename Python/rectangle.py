rows = int(input("Hauteur: "))
columns = int(input("Largeur: "))

for i in range(rows):
    rect = "|"
    for j in range(columns - 1):
        if i == 0 or i == (rows-1) :
            rect+= "-"
        else:
            rect+= " "
    rect += "|"
    print(rect)