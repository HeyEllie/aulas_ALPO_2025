cont =0 
vet=[0.0]* 10

for cont in range (0,30,1):
    vet[cont] = float(input("informe o numero de posiçao {cont}:  "))
for cont in range (0,30,1):
    if vet[cont]%2!= 0:
        print(f"[{vet[cont]}]",end = '')