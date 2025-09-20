'''
faça um algo que leia a nota de 5 alunos e armezene em um vetor, calcular a média e mostrar essa média, as notas e exibir também quantos alunos ficaram com as notas
iguais ou acima da média
'''
cont = 0
vet = [0.0] * 5
m = 0
tot = 0
alM = 0

for cont in range(0,5,1):
    vet[cont] = float(input(f"Informe a nota do aluno{cont}: "))
    cont += 1
    m += 1
    tot += vet[cont]

for cont in range(0,5,1):
        if vet[cont]>=tot/m:
            alM +=1
print(f"a media é {tot/m} os alunos acima da media é {alM} ")

'''
for cont in range(0,5,1):
    notas[cont] = float(input(f"Infrome a {cont+1} nota:"))
    som_notas += notas[cont]

calc_media = som_notas / 5

fro cont in range (0,5,1):
if (notas[cont] >= calc_media):
    n_notas +=1

fro cont in range (0,5,1):
    print(f"A nota {cont} é: {notas[cont]}")

print(f"a média foi {calc_media}")
print(f" um total de {n_notas} alunos ficaram com a nota igual ou acima da média")
'''