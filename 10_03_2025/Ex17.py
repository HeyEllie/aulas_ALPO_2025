'''
Faça um programa que receba o número de lados de um polígono convexo, calcule e mostre o número de diagonais desse polígono, onde N é o número de lados do polígono.
Sabe-se que ND = N*(N-3)/2
'''

#variaveis
numero_lados = 0
numero_diagonais = 0


#programa
numero_lados = int(input("Informe o número de lados do polígono: "))

numero_diagonais = numero_lados * (numero_lados - 3) / 2
print(f"O número de diagonais do polígono é: {numero_diagonais}")