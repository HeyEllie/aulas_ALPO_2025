'''
apresentar o total da soma de N números inteiros onde N é um número digitado pelo user
'''

n = 0

n = int(input("Informe o valor máximo do número a ser somado: "))
soma = 0

for contador in range(1, n + 1, 1):
    soma += contador 
#soma: soma + contador

print(f"O valor da soma é: {soma}")
