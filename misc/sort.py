# Sorts a list of deposits by one certain attribute. If attributen is negative, return in reverse order
def sort_deposits_by(attributen,deposits):
    if attributen > 0:
        deposits = mergesort(attributen,deposits)
    else:
        # Reverses order 
        attributen = -1*attributen
        deposits = mergesort(attributen,deposits)
        deposits.reverse()

    return deposits

def mergesort(attributen,unsorted_deposits):
    sorted_deposits=recursive_merge(attributen,list(unsorted_deposits),0,len(unsorted_deposits)-1)
    return sorted_deposits

def recursive_merge(attributen,u,lo,hi):
    a = list(u)
    if lo >= hi:
        pass
    else:
        mid = (lo+hi)//2
        a = recursive_merge(attributen,a,lo,mid)
        a = recursive_merge(attributen,a,mid+1,hi)
        a = merge(attributen,a,lo,mid,hi)
    

    return a

def merge(attributen,u,lo,mid,hi):
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
        elif a[x][attributen] <= a[y][attributen]:
            tmp[i] = a[x]
            x = x+1
        else:
            tmp[i] = a[y]
            y = y+1
        i = i+1

    # Much of this seems counterintuitive but is required to parallel with the limitations of Dafny
    i = 0
    while (i < hi-lo+1):
        a[lo+i] = list(tmp[i])
        i = i+1

    return a