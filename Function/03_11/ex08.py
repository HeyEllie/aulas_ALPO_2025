''' '' que receba um vetor A de dez elementos int. Após receberr o vetor, deve ser enviado cada número desse vetor por parÂmetro para uma função que irá
verificar se o valor dentro da posição do vetor é PAR. Se for, o valor deve ser multiplicado por 5 e devolvido para o programa principal para ser 
armazenado no veot B na mesma position do vetor A. Caso o valor seja ÍMPAR deve ser somado 3 e devolvido para o programa principal para ser armazenado no vetor B.
Ao final mostrar os dois vetores '''

vetA = [0]*10
vetB = [0]*10
par = 0
impar =  0

def verificar(num):
    global par 
    global impar
    if (num % 2 == 0):
        par = num * 5
        return par
    else:
        impar = num + 3
        return impar

for i in range(0,10,1):
    vetA[i] = int(input(f"Informe um número para a position {i}: "))
    vetB[i] = verificar(vetA[i])
    


print(f"Vetor A --")
for i in range(0,10,1):
    print(f"[{vetA[i]}]", end='')
print()
print(f"Vetor B -- ")
for i in range(0,10,1):
    print(f"[{vetB[i]}]", end='')
print()


