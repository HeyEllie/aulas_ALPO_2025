'''
Faça um programa que receba o salário base de um funcionário.
Calcule e mostre o salário a receber, sabendo que esse funcionário tem gratificação de R$50,00 e paga imposto de 10% sobre o salário base.
'''

#variaveis
salario_b = 0.0
salario_f = 0.0
imposto = 0.0

#programa
salario_b = float(input("Informe o valor do salário base: "))

imposto = (salario_b *10 /100)
salario_f = (salario_b - imposto) + 50


print(f"O salário final é: R${salario_f}")
