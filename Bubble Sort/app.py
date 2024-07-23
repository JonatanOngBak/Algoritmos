from Bubble import bubbleSort
from random import randint

random_list = [randint(1, 100) for _ in range(50)]
print("\033[30m Lista antes da ordenação:", random_list)
print("=" * 70)
bubbleSort(random_list)
print("\033[32m Lista após a ordenação:", random_list)

