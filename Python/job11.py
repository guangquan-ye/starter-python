with open("domains.xml", "r") as f :
    read_data =f.read()
    print(len(read_data.split('domain')))