def quicksort(arr):
    if len(arr) < 2: return(arr)
    s = []
    e = []
    b = []

    p = arr[0]

    for i in arr:
        if i < p: s.append(i)
        elif i > p: b.append(i)
        else: e.append(i)
    
    return quicksort(s)+ e + quicksort(b)
