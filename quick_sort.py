def partition(mylist, start, end):
    i= start
    pivot = mylist[end]
    pindex = start
    for i in range(start, end):
        if (mylist[i] < pivot or mylist[i] == pivot):
            temp = mylist[i]
            mylist[i] = mylist[pindex]
            mylist[pindex] = temp
            pindex +=1
    temp = mylist[pindex]
    mylist[pindex] = mylist[end]
    mylist[end] = temp
    return pindex

def quicksort(mylist, start, end):
    if (start < end):
        pindex = partition(mylist, start, end)
        quicksort(mylist, start, pindex - 1)
        quicksort(mylist, pindex + 1, end)
    return mylist

mylist = [7,2,5,1,29,6,4,19,11]
print(mylist)
sorted_list = quicksort(mylist, 0, len(mylist)- 1)
print(sorted_list)
