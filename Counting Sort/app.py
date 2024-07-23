from Counting import count_sort

input_array = [4, 3, 12, 1, 5, 5, 3, 9, 15]
output_array = count_sort(input_array)
for num in output_array:
    print(num, end=" ")