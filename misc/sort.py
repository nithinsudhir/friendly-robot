# Sorts a list of deposits by one certain attribute. Attribute must be unique. If attributen is negative, return in reverse order
def sort_deposits_by(attributen,deposits):
    if attributen > 0:
        uniquenums = [row[attributen] for row in deposits]
        uniquenums = mergesort(uniquenums)

        sorted_deposits = []
        for i in uniquenums:
            for row in deposits:
                if row[attributen] == i:
                    sorted_deposits.append(row)
    else:
        # Reverses order 
        attributen = -1*attributen

        uniquenums = [row[attributen] for row in deposits]
        uniquenums = mergesort(uniquenums)

        sorted_deposits = []
        for i in uniquenums:
            for row in deposits:
                if row[attributen] == i:
                    sorted_deposits.append(row)
        sorted_deposits.reverse()
    return sorted_deposits

def mergesort(unsorted_deposits):
    sorted_deposits=recursive_merge(list(unsorted_deposits),0,len(unsorted_deposits)-1)
    return sorted_deposits

def recursive_merge(u,lo,hi):
    a = list(u)
    if lo >= hi:
        pass
    else:
        mid = (lo+hi)//2
        a = recursive_merge(a,lo,mid)
        a = recursive_merge(a,mid+1,hi)
        a = merge(a,lo,mid,hi)
    

    return a

def merge(u,lo,mid,hi):
    a = u.copy()
    tmp = [None]*(hi-lo+1)
    x = lo
    y = mid+1

    i = 0
    while i < hi-lo+1:
        if x > mid:
            tmp[i] = a[y]
            y = y+1
        elif y > hi:
            tmp[i] = a[x]
            x = x+1
        elif a[x] <= a[y]:
            tmp[i] = a[x]
            x = x+1
        else:
            tmp[i] = a[y]
            y = y+1
        i = i+1

    # Much of this seems counterintuitive but is required to parallel with the limitations of Dafny
    i = 0
    while (i < hi-lo+1):
        a[lo+i] = tmp[i]
        i = i+1

    return a