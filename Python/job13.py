nb_lettres = int(input("Entrer un nombre de lettres: "))

file = open('data.txt')
file_read = file.read()
text = file_read.replace('. ', ' ').replace(', ', ' ').replace('; ', ' ').replace('! ', ' ').replace('? ', ' ').replace(': ', ' ').replace("'", " ")
split_file = text.split()
print(split_file)


def nbMots(split_file):
    count = 0
    for i in split_file:
        if len(i) == nb_lettres:
            count = count + 1
    return count


result = nbMots(split_file)
print(result) 