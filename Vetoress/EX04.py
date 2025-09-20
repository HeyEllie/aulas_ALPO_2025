"""
Faça um algoritmo que leia 50 valores reais e armazene em um vetor.
Modifique o vetor de modo que os valores das posições ímpares sejam aumentados em 5%, e os das posições pares sejam aumentados em 2%.
Imprima depois o vetor original e o resultante.
OBS: Só pode ser utilizado um vetor.
"""

#variaveis
vet = [0.0]*50
cont = 0

#algoritmo
for cont in range (0,50, 1):
    vet[cont] = float(input(f"Informe o número para a posição {cont}: "))

print("=======Mostrando o vetor original=======")
for cont in range(0,50,1):
    print(f"{vet[cont]:.2f}", end=' ')

for cont in range (0,50,1):
    if (cont % 2 != 0):
        vet[cont] = (vet[cont]) + (5/100)*(vet[cont])
    else: 
        vet[cont] = (vet[cont]) + (2/100)*(vet[cont])


print("=======Mostrando o vetor resposta=======")
for cont in range(0,50,1):
    print(f"[{vet[cont]}]", end= ' ')  #end quebra a linha
