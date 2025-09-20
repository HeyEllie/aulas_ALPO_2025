'''
'' que leia 20 letras. Ao final o algoritmo deve infomar quantas voh
gais e quantas consoantes foram digitadas
'''
l = ""
nv = 0
nc = 0

for cont in range(1,21,1):
    l = input(f"Informe a {cont}° letra: ")
    if (l == "a") or  (l =="e") or (l=="i") or  (l=="o") or (l =="u"):
       nv += 1
    else:
        nc += 1

print(f"O número de consoantes é: {nc} e o número de de vogais é: {nv}")
    
