"""
Faça um algoritmo que leia 30 números reais em um vetor e depois mostre os números localizados nas posições ímpares.
O sistema deve percorrer todo o vetor e escolher somente os números das posições ímpares.
"""

#variaveis
cont = 0
vet = [0.0]*30

#algoritmo

for cont in range (0,30,1):
    vet[cont] = float(input(f"Informe o número para a posição {cont}: "))


print("========Mostrando os números nas posições ímpares========")
for cont in range (0,30,1):
    if(cont % 2 != 0):
      print(f"[{vet[cont]}]", end= ' ')