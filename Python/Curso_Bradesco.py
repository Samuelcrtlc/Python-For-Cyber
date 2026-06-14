# Adição			+
# Subtração		-
# Multiplicação		*
# Divisão Real		/
# Divisão Inteiro		//
# Exponenciação	        **
# Resto da Divisão	%

# Igual a			==
# Diferente de		!=
# Maior que		>
# Menor que		<
# Maior ou igual a	>=
# Menor ou igual a	<=

# E	and
# OU	or
# Não	not

# for i in range (10, -43 ,-2):
#     print (i)



######    Funçôes

# def happy_birthday(name, age):
#     print(f"Happy birthday to you")
#     print(f"Happy birthday dear {name}")
#     print(f"you are {age} years old")
#     print()

# happy_birthday("Maria", 25)
# happy_birthday("Mario", 30)


# se a função não tiver um return, ela retorna None por padrão. Por isso, quando chamamos print(teste()), ele imprime "Teste" e depois imprime "None".
# todo número em python é um objeto, e o tipo de um número inteiro é "int". Portanto, quando chamamos teste(5), ele imprime "<class 'int'>", que é a representação do tipo do número 5. O resultado final da chamada print(teste(5)) será:
# obrigatoriamente botar um self como primeiro parâmetro de um método dentro de uma classe, para que ele possa acessar os atributos e métodos da classe. No entanto, no código fornecido, o método estudar() não tem um parâmetro self, o que causará um erro quando tentarmos chamar esse método em uma instância da classe Aluno. Para corrigir isso, devemos adicionar self como primeiro parâmetro do método estudar(), assim:

#-------------------------------------------------------------------
# Aula de POO Na Faculdade:

# Explicação de Classes e Herança:
# class pai:
#     def mostrarOi(self):
#         print("oi")

# class filho(pai):
#     def mostrarOla(self):
#         super().mostrarOi()

# p = pai()
# f = filho()
# p.mostrarOi()  # Isso imprimirá "oi"
# f.mostrarOi()  # Isso também imprimirá "oi" porque a classe filho herda o método mostrarOi() da classe pai

#-------------------------------------------------------------------