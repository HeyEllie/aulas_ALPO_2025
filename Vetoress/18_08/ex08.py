'''
'' que leia um vetor de 5 elemnetos int. 
Calcule e mostre a soma desses elementos, a média, quantos elementos que são = ou maiores do que a média,
 o percentual dos lementos que são maiores ou = a média  e 
 mostre quantos desses elementos são positivos e quantos são  negativos
'''

'''    soma = sum(vet)
soma += vet[cont]
    media = soma /len(vet)
'''
vet = [0] * 5
soma = 0
media = 0
cont = 0
ele_maiores = 0
negativos = 0
positivos = 0

for cont in range(0,5,1):
    vet[cont] = int(input(f"Informe o valor do elemento {cont+1}ª: "))
    if (vet[cont] < 0):
        negativos += 1
    else:
        positivos += 1

soma = sum(vet)
media = soma / 5

for cont in range(0,5,1):
    if (vet[cont] >= media):
        ele_maiores += 1

percentual = (ele_maiores * 5 ) / 100

print(f"Os elementos maiores ou iguais a média são {ele_maiores}\nO percentual é {percentual}")
print(f"A soma de todos os elementos é {soma}\nA média é {media}")
print(f"Os números negativos são {negativos} e os positvos são {positivos}")


