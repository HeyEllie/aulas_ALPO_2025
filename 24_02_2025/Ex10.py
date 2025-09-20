'''
Faça um algoritmo que receba o valor do salário mínimo e o valor do salário que um trabalhador recebe. Calcular e mostrar quantos salário mínimos esse trabalhador recebe.
'''

#variaveis
salario_m = 0.0
salario_recebido = 0.0
total_salarios = 0.0

#programa 
salario_m = float(input("Informe o salário mínimo: "))
salario_recebido = float(input("Informe o salário que o trabalhador recebe: "))

total_recebido = salario_recebido / salario_m

print(f"O trabalhador recebe: {total_recebido} salários mínimos")
