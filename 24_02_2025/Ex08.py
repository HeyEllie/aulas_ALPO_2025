'''
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas.
Faça um programa que receba o salário fixo de um funcionário e o valor total de suas vendas.
Calcule e mostre a comissão recebida em reais e o salário final do funcionário( salário fixo + comissão )
'''

#variaveis
salario_fixo = 0.0
comissao = 0.0
salario_final = 0.0

#programa
salario_fixo = float(input("Informe o valor do salário: "))
comissao = float(input("Informe o valor da comissão: "))
 
salario_final = salario_fixo + (comissao * 4 / 100)

print(f"O salário do funcionário é: {salario_final} ")