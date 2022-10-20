def mf (*nb) :
    
    mylist=[nb]
    
    mylist=list(nb)
    
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[i]>mylist[j]:
                mylist[i],mylist[j]=mylist[j],mylist[i]
    
    return(mylist)
def display(d):
    print(d)    
display(mf(1,2,5,7,3,8,4,6))
                      























