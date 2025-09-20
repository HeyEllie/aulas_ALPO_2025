''' faça um algoritmo que receba o nome e duas notas de um aluno. Calcule a média e ao final mostre o nome do aluno, média e a sua situação.
 Caso a média seja no mínimo 6, o aluno está aprovado, se a média foi inferior a 6 e no mínimo 4 o aluno está de Exame e se a média for inferior a 4 o mesmo está reprovado
'''

#variaveis
n = ""
n1 = 0.0
n2 = 0.0

#programa
n = input("informe o nome do aluno: ")
n1 = float(input("Informe a primeira nota do aluno: "))
n2 = float(input("Informe a segunda nota do aluno: "))

m = (n1 + n2) /2

if(m >= 6):
    print(F"{n}, sua média é {m} e você está aprovado!!")
else:
    if(m <= 6) and ( m >= 4):
        print(f"{n}, sua média é {m} e você está de Exame!!")
    else:
        print(f"{n}, sua média é {m} e você está reprovado!!")