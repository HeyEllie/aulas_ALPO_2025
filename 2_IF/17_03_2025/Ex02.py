''' Faça um programa que receba duas notas e calcule a média. Caso a média seja no mínimo 6 o mostrar a mensagem que o aluno está aprovado,
caso contrário o mesmo está reprovado
'''

#variaveis
n1 = 0.0
n2 = 0.0
m = 0.0

#programa
n1 = float(input("Informe o valor da primeira nota: "))
n2 = float(input("Informe o valor da segunda nota: "))

m = (n1 + n2) /2

if (m >= 6):
    print("Você foi aprovado!")
else:
    print("você foi reprovado!")