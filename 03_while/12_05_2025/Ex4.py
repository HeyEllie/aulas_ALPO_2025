"""
'' que solicite N números inteiros at´w que o número 0 seja digitado. Ao final o algoritmo deve
informar o maior e o menor número digitado.
OBS: o número 0 não pode ser contado
"""
nu = 1
maior = 0
contador = 1
menor = 0

#nu = int(input(f"Informe o valor do número: "))
while nu != 0:
    nu = int(input(f"Informe o valor do número: "))
    if (contador == 1):
        maior = nu
        menor = nu
        contador = 2
    else:
        if (nu > maior):
            maior = nu
        if (nu < menor ) and ( nu != 0):
            menor = nu

print(f"O maior número digitado é: {maior} e o menor é: {menor}")