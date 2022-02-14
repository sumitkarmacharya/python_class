mylist = [1,4,2,5,2,1,4,9,7,5]
def removeduplicate(a):
    for i in mylist:
        for x in range(1,len(mylist)-1):
            if x==i:
                mylist.sort()
                mylist.remove(i)
    return mylist
print(removeduplicate(mylist))