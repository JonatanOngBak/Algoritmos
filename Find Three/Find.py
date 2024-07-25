"""
def find_three(num):
    for i in range(len(num)):
        for j in range
"""   
def find_Three(list):
    if len(list) < 3:
        return "A arrey deve ter pelo menos 3 elementos"
    
    maior1 = float()
    maior2 = float()
    maior3 = float()

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
