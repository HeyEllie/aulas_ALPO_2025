'''
Faça um algoritmo que veifica se o número digitado é impar ou par. OBS: para saber se um número é ímpar ou par, voc~e deve verificar o resto da divisão desse número por doi
para isso voc~e eve utiliZAR o comando %. Ex: 10 % 2 se o resultado for 0 então o número é par, no contrário ele é  ímpar
'''

#variaveis
n = 0.0

#programa
n = float(input("Informe o valor do número: "))

if n % 2 == 0:
    print("O seu número é par")
else:
    print("O seu número é ímpar")