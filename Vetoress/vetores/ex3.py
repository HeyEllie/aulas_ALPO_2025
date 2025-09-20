cont =0 
vet=[0.0]* 10

for cont in range (0,10,1):
    vet[cont] = float(input("informe o numero {cont}:  "))
for cont in range (0,10,1):
    if cont %2!= 0:
        print(f"impar = [{vet[cont]/100*105}]",end = '')
    if cont %2== 0:
        print(f"par = [{vet[cont]/100*102}]",end = '')