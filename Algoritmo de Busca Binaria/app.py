from Busca import Busca_Binaria

lista = [
    "Aaron", "Abigail", "Adam", "Alan", "Albert", "Alex", "Alice", "Amanda", "Amber", "Amy",
    "Andrew", "Angela", "Anna", "Arthur", "Austin", "Barbara", "Benjamin", "Betty", "Beverly", "Billy",
    "Brandon", "Brian", "Brittany", "Bruce", "Carl", "Carol", "Charles", "Charlotte", "Cheryl", "Chris",
    "Cynthia", "Daniel", "David", "Deborah", "Dennis", "Donald", "Dorothy", "Douglas", "Edward", "Elizabeth",
    "Emily", "Eric", "Evelyn", "Frank", "Gary", "George", "Gregory", "Hannah", "Heather", "Helen" ]


nome_procurado = "david"

resultado = Busca_Binaria(lista, 0, len(lista)-1, nome_procurado)
if resultado != -1:
    print(f"O elemento esta no indice {resultado}")
else:
    print("O elemento nao esta na lista")
