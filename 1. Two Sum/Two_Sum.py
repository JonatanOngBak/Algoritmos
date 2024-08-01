from typing import List

class Solucao:
    def doisSomas(self, nums: List[int], alvo: int) -> List[int]:
        # Cria um dicionário para armazenar o valor e seu índice
        mapa_numeros = {}
        
        # Itera sobre a lista
        for i, num in enumerate(nums):
            # Calcula o complemento
            complemento = alvo - num
            
            # Verifica se o complemento está no dicionário
            if complemento in mapa_numeros:
                # Retorna os índices dos dois números
                return [mapa_numeros[complemento], i]
            
            # Adiciona o número e seu índice ao dicionário
            mapa_numeros[num] = i
        
        # Se nenhuma solução for encontrada, retorna uma lista vazia
        return []
