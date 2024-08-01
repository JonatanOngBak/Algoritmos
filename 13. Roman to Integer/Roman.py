class Solucao:
    def romanoParaInteiro(self, s: str) -> int:
        # Mapeamento dos valores dos numerais romanos
        valores = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        
        valor_Anterior = 0

        # Iterar sobre cada caractere do numeral romano na ordem inversameral
        for caractere in reversed(s):
            valor = valores[caractere]

            # Se o valor atual for menor que o valor anterior, subtrair do total
            if valor < valor_Anterior:   
                total -= valor
            else:
                total += valor
            valor_Anterior = valor    
        return total
    
