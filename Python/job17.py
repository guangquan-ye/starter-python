def mf(*nb) :
    

    mylist=[nb]
    mylist=list(nb)
    #even = list(filter(lambda x: not x%2, mylist))
    #print("list:" , even)
    for i in mylist:
        if i%2==0:
            print(i)
mf(9, 3, 8, 4, 5, 7, 12, 16)
