cont =0 
vet=[0.0]* 10

for cont in range (0,10,1):
    vet[cont] = float(input("informe o numero de posiçao {cont}:  "))
for cont in range (9,-1,-1):
    print(f"[{vet[cont]}]",end = '')