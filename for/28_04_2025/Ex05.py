'''
faça um algo que solicite N números inteiros. Ao final o algoritmo deve informa o maior número digitado
'''

n = 0
nu  = 0
maior = 0

n = int(input("Informe o número: "))

for contador in range(1,n+1,1):
    nu = int(input(f"Informe o valor do número {contador}: "))
    if (nu > maior):
        maior = nu

print(f"O maior número digitado é: {maior}")
    
    
