"""
Criar um algoritmo que leia 10 números pelo teclado e exiba os números na ordem inversa da que os números foram digitados.
"""

#variaveis 
cont = 0
vet = [0]*10

#algoritmo
for cont in range(0,10,1):
    vet[cont]= int(input(f"Informe um número para a posição {cont+1}: "))

print("=========Mostrando o vetor na ordem inversa=========")
for cont in range (9,-1,-1):
    print(f"{vet[cont]}]", end= ' ')