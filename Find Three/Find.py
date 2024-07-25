def find_Three(list):
    if len(list) < 3:
        return "A arrey deve ter pelo menos 3 elementos"
    
    maior1 = float('-inf')   # usar '-inf' garante que seu código funcionará corretamente 
    maior2 = float('-inf')   # independentemente dos valores no array, sejam eles positivos
    maior3 = float('-inf')   # negativos ou uma combinação de ambos.

    for num in list:
        if num > maior1:
            maior3 = maior2
            maior2 = maior1
            maior1 = num
        elif num > maior2:
            maior3 = maior2
            maior2 = num
        elif num > maior3:
            maior3 = num
    
    return [maior1, maior2, maior3]
