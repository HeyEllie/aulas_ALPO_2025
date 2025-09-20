'''
Faça um programa que calcule e mostre a área de um trapézio.
Sabe-se que a fórmula para calcular a área do trapézio é:
Area = ((base maior + base menor) * altura) /2
'''
#variaveis
area = 0.0
base_maior = 0.0
base_menor = 0.0
altura = 0.0

#programa
base_maior = float(input("Informe o valor da base maior:"))
base_menor = float(input("Informe o valor da base menor: "))
altura = float(input("informe a altura do trapézio: "))

area = (base_maior + base_menor) * altura /2

print(f"A área do trapézio é {area}")