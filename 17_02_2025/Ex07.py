'''
Faça um programa que receba o salário de um funcionário e a porcentagem de aumento. Calcule e mostre o salário final.
nota linha 17: há somente o valor de aumento, por isso precisa ainda somar com o salário
17/02/2025
'''

#variaveis
salario = 0.0
aumento = 0.0
porcentagem_aumento = 0.0
salario_final = 0.0

#programa
salario = float(input("Informe o salário do funcionário: "))
porcentagem_aumento = float(input("Informe a porcentagem de aumento: "))

aumento = (salario * (porcentagem_aumento) / 100)       #há somente o valor de aumento, por isso precisa ainda somar com o salário
salario_final = salario + aumento 

print(f"O salário final é R${salario_final}")