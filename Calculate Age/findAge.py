def findAge(data_atual, mes_atual, ano_atual, data_nascimento, mes_nascimento, ano_nascimento):

    # Verifica se é ano bissexto e ajusta fevereiro
    def eh_ano_bissexto(ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
    
    # Lista de dias em cada mês
    meses = [31, 29 if eh_ano_bissexto(ano_atual) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if data_nascimento > data_atual:
        mes_atual -= 1
        data_atual += meses[mes_nascimento - 1]

    
    # Ajuste se o mês de nascimento for maior que o mês atual
    if mes_nascimento > mes_atual:
        ano_atual -= 1
        mes_atual += 12

    # Calcula da idade
    dias_calculados = data_atual - data_nascimento
    meses_calculados = mes_atual - mes_nascimento
    anos_calculados = ano_atual - ano_nascimento

    # Impresão da idade calculada
    print("Idade Atual")
    print("Anos:", anos_calculados, "Meses:", meses_calculados, "Dias:", dias_calculados)

