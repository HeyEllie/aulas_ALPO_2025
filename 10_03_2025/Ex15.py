'''
Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. 
Esse programa deve calcular e mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.
'''

#variaveis
custo_espetaculo = 0.0
preco_convite = 0.0
calculo = 0.0

#programa
custo_espetaculo = float(input("Informe o custo do espetáculo: "))
preco_convite = float(input("Informe o preço do convite: "))

calculo = (custo_espetaculo // preco_convite) + 1
#calculo = int(custo / preco_convite) + 1

print(f"A quantidade de convites que devem ser vendidos é: {calculo} convites ")


