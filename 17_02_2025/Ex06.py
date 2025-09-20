'''
Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%
17/02/2025
100------100%
x--------10%         x*100% + 100*10%  x = 100*10%
                                            100%           desc = v-prod * 10 / 100
                                            
'''

#variaveis
preco_produto = 0.0
novo_preco = 0.0


#programa
preco_produto = float(input("Informe o preço do produto: "))
novo_preco = (preco_produto) * 10 / 100

print("O novo preço é: {novo_preco} ")



