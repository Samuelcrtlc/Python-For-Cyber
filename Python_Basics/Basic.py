# 0
#EN - This is a code that sums only the even numbers of a list of integers, returning the final result.

#BR - Este é um código que soma apenas os números pares de uma lista de inteiros, retornando o resultado final.
class Solution:
    def sum_even(self, nums: list[int]) -> int:
        total = 0                   # Create the variable to accumulate the total /// Criamos a variável para acumular o total 
        for i in nums:
            if i % 2 == 0:          # If the remainder of the division by 2 is 0, it's even! /// Se o resto da divisão por 2 for 0, ele é par!

                total += i          # Add the current number to our total /// Somamos o número atual ao nosso total 
        return total                # At the end, we return the accumulated result /// No final, retornamos o resultado acumulado

call = Solution()                   # Call the class + function /// Chamar a classe + função

test_list = [1, 2, 3, 4, 5, 6]      # Test list /// Lista de teste 

result = call.sum_even(test_list)
print(f"Test list: {test_list}")
print(f"The sum of the even numbers is: {result}")  # RESULT: 2 + 4 + 6 = 12

print()
# --------------------------------------------------------------------------

# 1
#EN - This is a solution to the "Two Sum" problem of LetCode, where we need to find two numbers in a list that add up to a specific target.

#BR - Esta é uma solução para o problema "Two Sum" do LeetCode, onde precisamos encontrar dois números em uma lista que somam um alvo especifico.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):                # i goes through all the positions of the "nums" list /// i percorre toda a posição da lista de "nums"

            for j in range(i + 1, len(nums)):     # starts j = i + 1 to avoid repetitive combinations /// começa com j = i + 1 para não repetir combinações

                if nums[i] + nums[j] == target:   # verify if the sum of the two elements (i+j) is equal to the target /// verficar se a soma dos dois elementos (i+j) é igual ao alvo (target)

                    return [i,j]                  # return the positions of the elements that sum up to the target /// retorna a posição dos elementos que somam o alvo (target)

call = Solution()                                 # Call the class + function /// Chamar a classe + função

test_list = [2, 7, 11, 15]                        # Test list /// Lista de teste 
target = 9                                        
result = call.twoSum(test_list, target)

print(f"Test list: {test_list}")
print(f"The indices of the numbers that sum up to {target} are: {result}")  # If dont find the result it will return "none" Null
