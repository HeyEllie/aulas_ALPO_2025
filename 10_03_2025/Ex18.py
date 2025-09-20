'''
Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro quadrado, deve-se usar 18 W de potência. 
Faça um programa que receba as duas dimensões de um cômodo (em metros), calcule e mostre a sua área ( em metros quadrados) e a potência de iluminação que deverá ser utilizada.
'''

#variaveis
dimensqo1 = 0.0
dimensao2 = 0.0
area = 0.0
iluminacao = 0.0

#programa
dimensao1 = float(input("Informe o valor da primeira dimensão: "))
dimensao2 = float(input("Informe o valor da segunda dimensão: "))
area = dimensao1 * dimensao2
iluminacao = area * 18
print(f"A área é de: {area} metros quadrados e a potência de iluminação que deverá ser utilizada é de: {iluminacao} ")