texte=(input("Entrez un texte"))
fichier=open("output.txt", "w")
fichier.write(texte)
fichier.close()
fichier=open("output.txt", "r")

print(fichier.read())


