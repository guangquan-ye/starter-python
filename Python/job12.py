with open ("data.txt", "r") as f:
    read_data = f.read()
    per_word = read_data.split()
    print(len(per_word))