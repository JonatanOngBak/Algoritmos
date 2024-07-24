def MinSum(list):
    # Encontrando o menor número na lista
    menor_valor = min(list)
    # Calculando e retornando o resultado
    return menor_valor * (len(list) - 1)
    