'''
Faça un algoritmo que leia a idade ne N pessoas. O sistema deve calcular: a média das idade, a menor e a maior idade informada.
'''
n = 0
maior = 0
menor = 0
soma = 0

n = int(input("Informe o número de pessoas: "))
for cont in range(1,n+1,1):
    nu = int(input(f"Informe o valor do número {cont}: "))
    if (cont == 1):
        maior = nu
        menor = nu
    else:
        if (nu > maior):
            maior = nu
        if (nu < menor):
             menor = nu
    soma += nu

media = soma / n

print(f"A média é: {media}, a maior idade é: {maior} e a menor idade é: {menor}")