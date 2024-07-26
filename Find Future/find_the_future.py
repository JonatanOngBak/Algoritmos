import functools

def comp(s, t):
    ss = s.split("/")
    tt = t.split("/")
    date1 = [int(ele) for ele in ss]
    date2 = [int(ele) for ele in tt]

    if date1[2] != date2[2]:
        return date1[2] - date2[2]
    elif date1[1] != date2[1]:
        return date1[1] - date2[1]
    elif date1[0] != date2[0]:
        return date1[0] - date2[0]
    
    return 0

def nextClosestData(arr, q):
    arr.sort(key = functools.cmp_to_key(comp))
    l = 0
    r = len(arr) - 1
    ind = -1

    while l <= r:
        m = (l + r) // 2
        c = comp(q, arr[m])

        if c == 0:
            ind = m
            break
        elif c < 0:
            r = m - 1
            ind = m
        else:
            l = m + 1
    if ind == -1:
        return "-1"
    else:
        return arr[ind]            

def performQueries(arr, Q):
    for i in range(len(Q)):
        print(nextClosestData(arr, Q[i]))
        