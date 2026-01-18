def bin_search(L,v):
    if len(L)<1:
        return False
    low = 0
    high = len(L)-1
    if L[low]==v or L[high]==v:
        return True
    while low < high-1:
        midpoint = low + (high-low)//2
        if L[midpoint] == v:
            return True
        elif L[midpoint] < v:
             low = midpoint
        else:
            high = midpoint
    return False

####### SORTING ######
def quicksort(L):
    n = len(L)
    L1 = []
    L2 = []

    if n<=1:
        return
    pivot = L[0]

    for i in L[1:]:
        if i < pivot:
            L1.append(i)
        else:
            L2.append(i)
    quicksort(L1)
    quicksort(L2)

    L[:] = []

    for i in L1:
        L.append(i)
    L.append(pivot)

    for i in L2:
        L.append(i)

    return

def merge(L,L1,L2):
    i = 0
    j = 0
    k = 0

    while j<len(L1) or k<len(L2):
        if j < len(L1):
            if k < len(L2):
                #we are not at the end of l1 or l2, so pull the smaller value
                if L1[j] < L2[k]:
                    L[i] = L1[j]
                    j+=1
                else:
                    L[i] = L2[k]
                    k+=1
            else:
                #we are at the end of L2, so pull from L1
                L[i] = L1[j]
                j+=1
        else:
            L[i] = L2[k]
            k+=1
        i +=1

    return
def mergeSort(L):
    n = len(L)
    if n<=1:
        return
    L1 = L[:n//2]
    L2 = L[n//2:]

    mergeSort(L1)
    mergeSort(L2)
    merge(L,L1,L2)
    return

favorite_foods=['pizza','barbeque','gumbo','chicken and dumplings', 'pecan pie','ice cream']
mergeSort(favorite_foods)
print(favorite_foods)