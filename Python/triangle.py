left = "/"
right = "\\"
base ="__"

t=int(input("Taille :"))

for i in range(t):
    print((t-i)* " " + left +((i*2)* " ") + right)
    if i == t -1:
        print(left + base*t +right)