'''
faça um algo que solicite N números inteiros. Ao final o algoritmo deve informa o maior e o menor número digitado

'''
n = 0
nu = 0
maior = 0
menor = 0

n = int(input("Informe o número: "))
for contador in range(1,n+1,1):
    nu = int(input(f"Informe o valor do número {contador}: "))
    if (contador == 1):
        maior = nu
        menor = nu
    else:
        if (nu > maior):
            maior = nu
        if (nu < menor):
            menor = nu

print(f"O maior número digitado é: {maior} e o menor é: {menor}")