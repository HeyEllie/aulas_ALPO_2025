''' 
que leia o nome e a média final de 5 alunos e guarde em um vetor. Ao final deve ser mostrado o nome e a média do aluno com maior média
'''
vet = [0.0] * 5
vetNome = [" "] *5
cont = 0
maior = 0

for cont in range (0,5,1):
    vet[cont] = float(input(f"Informe a média final do aluno {cont+1}: "))
    vetNome[cont] =  input(f"Informe o nome do aluno {cont+1}: ")
    if vet[cont] > maior:
        maior += 1

for cont in range(0,5,1):
    if (vet[cont] > maior):
        maior = vet[cont]
        nome_maior = vetNome[cont]
print(f"A maior média foi do aluno {nome_maior} com {maior}")