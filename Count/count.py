"""Contar maiúsculas, minúsculas, caracteres especiais e valores numéricos
Dada uma string, escreva um programa para contar a ocorrência de caracteres minúsculos
caracteres maiúsculos, caracteres especiais e valores numéricos."""


def Count(entrada):
    maiúsculas = minúsculas = numéricos = especiais = 0
    for i in range(len(entrada)):
        if entrada[i].isupper():
            maiúsculas += 1
        elif entrada[i].islower():
            minúsculas += 1
        elif entrada[i].isnumeric():
            numéricos += 1
        else:
            especiais += 1
    print(f'maiúsculas {maiúsculas}\nminúsculas {minúsculas}\nnuméricos {numéricos}\nespeciais {especiais}')        

            