'''
Desenvolva um algoritmo que:
- Solicite o nome do usuário.
- Solicite o ano de nascimento e o ano atual.
- Calcule a idade em dias.
- Mostre o nome e a idade calculada.
17/02/2025
 float = coverter em casas decimais  int = em números inteiros
'''

#variaveis
nome = ""
ano_atual = 0
ano_nascimento = 0
idade = 0


#programa
nome = input("Informe o nome do usuário: ")
ano_atual= int(input("Informe o ano atual: "))
ano_nascimento= int(input("Informe o ano de nascimento: "))

idade = (ano_atual - ano_nascimento) * 365


print(f"A idade em dias do usuário é: {nome} é {idade}")


