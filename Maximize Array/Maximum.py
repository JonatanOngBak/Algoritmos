def maximumSum(lista, n, k):
    for i in range(1, k + 1):
        min = +2147483647
        index = -1

        for j in range(n):
            if lista[j] < min:
                min = lista[j]
                index = j
        lista[index] = -lista[index]
    return sum(lista)
