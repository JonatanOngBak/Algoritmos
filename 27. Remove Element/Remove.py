from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Inicializa um ponteiro para a posição dos elementos não iguais a val
        k = 0
        
        # Itera sobre cada elemento de nums
        for i in range(len(nums)):
            # Se o elemento atual não for igual a val
            if nums[i] != val:
                # Coloca o elemento na posição indicada por k e incrementa k
                nums[k] = nums[i]
                k += 1
        
        # Retorna o número de elementos que não são iguais a val
        return k
 