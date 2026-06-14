class Solution:
    def somaPares(self, nums: list[int]) -> int:
        soma = 0                    # Create the variable to accumulate the total / Criamos a variável para acumular o total 
        for i in nums:
            if i % 2 == 0:          # If the remainder of the division by 2 is 0, it's even! / Se o resto da divisão por 2 for 0, ele é par!

                soma += i           # Add the current number to our total / Somamos o número atual ao nosso total 
        return soma                 # At the end, we return the accumulated result / No final, retornamos o resultado acumulado

solicitador = Solution()            

lista_teste = [1, 2, 3, 4, 5, 6]

resultado = solicitador.somaPares(lista_teste)
print(f"A soma dos números pares é: {resultado}")
# RESULT: 2 +4+6 = 12 
