cont=0 
vet=[0.0]*12
med=0
tot=0
for cont in range (0,12,1):
    vet[cont] = float(input(f"informe o quanto choveu do determinado mes {cont+1} :  "))
    med+=1
    tot+=vet[cont]
print(f"a media é {tot/med}  total é {tot}")