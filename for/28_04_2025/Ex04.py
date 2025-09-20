'''
costrua u mprograma que receba N números inteiros. O algo deve calcular e mostar a média dos números informados
'''
n = 0
soma = 0
media = 0.0


n = int(input("Informe o número: "))

for contador in range(1,n+1,1):
    nu = int(input("Informe o valor do número: "))
    soma += nu

media = soma / n

print(f"A méia é: {media}")