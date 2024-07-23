def bubbleSort(list):
    n = len(list)
    for i in range(n):
        troca = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                troca = True
        if not troca:
            break
