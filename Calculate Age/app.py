from datetime import datetime
from findAge import findAge


data_atual = datetime.now().day
mes_atual = datetime.now().month
ano_atual = datetime.now().year

data_nascimento = 1
mes_nascimento = 1
ano_nascimento = 1988

# Chamada da função
findAge(data_atual, mes_atual, ano_atual, data_nascimento, mes_nascimento, ano_nascimento)

