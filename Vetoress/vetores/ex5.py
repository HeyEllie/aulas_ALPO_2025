cont=0 
vet=[0.0]*5
med=0
tot=0
al=0
for cont in range (0,5,1):
    vet[cont] = float(input(f"informe a nota do perspectivo aluno{cont+1} :  "))
    med+=1
    tot+=vet[cont]
for cont in range (0,5,1):
    if vet[cont]>=tot/med:
        al+=1
print(f"a media é {tot/med} os alunos acima da media é {al} ")
