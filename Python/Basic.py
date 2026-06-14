class Solution:
    def somaPares(self, nums: list[int]) -> int:
        soma = 0  # Criamos a variável para acumular o total
        
        for i in nums:
            if i % 2 == 0:  # Se o resto da divisão por 2 for 0, ele é par!
                soma += i   # Somamos o número atual ao nosso total
                
        return soma  # No final, retornamos o resultado acumulado

solicitador = Solution()

lista_teste = [1, 2, 3, 4, 5, 6]

resultado = solicitador.somaPares(lista_teste)
print(f"A soma dos números pares é: {resultado}")