from Remove import Solution

solucao = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

k = solucao.removeElement(nums, val)
print(f"\nNúmero de elementos não iguais a {val}: {k}")
print(f"Array modificado:\033[33m {nums[:k]}\033[m\n ") 