nb1=int(input("Premier nombre ?"))
nb2=int(input("Deuxieme nombre ?"))

for i in range (nb1+1 , nb2) or reversed(range(nb2+1 , nb1)):
    print (i)
if nb1 == nb2 :
    print("Valeurs égales")