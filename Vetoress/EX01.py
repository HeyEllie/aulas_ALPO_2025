"""
Desenvolver um algoritmo que leia cinco números com casas decimais e armazene em um vetor.
"""

#variaveis 
cont = 0
vet = [0.0]*5

#algoritmo
for cont in range(0,5,1):
    vet[cont] = float(input(f"Informe o número para a posição {cont}: "))

for cont in range (0,5,1):
    print(f"[{vet[cont]}]", end= ' ')