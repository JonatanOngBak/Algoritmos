def Busca_Binaria(list, ini, fim, alvo):
    while ini <= fim:
        meio = ini + (fim - ini) // 2 
        if list[meio] == alvo:
            return meio
        elif list[meio] < alvo:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1           