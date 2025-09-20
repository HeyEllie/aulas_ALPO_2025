'''ue leia 20 letras. Ao final o algoritmo deve infomar a qauntidade de voh
gais que foram digitadas e o número total de consoantes foram digitadas

'''
l = ""
vo = 0
ve = 0
va = 0
vi = 0
vu = 0
c = 0

for cont in range(1,21,1):
    l = input(f"Informe a {cont}° letra: ")
    if (l == "a"):
       va += 1
    else:
        if (l =="e"):
            ve += 1
        else:
            if (l=="i"):
                vi += 1
            else:
                if (l=="o"):
                    vo += 1
                else:
                    if (l =="u"):
                        vu += 1
                    else:
                        c +=1

print(f"O número de vogais A é: {va}, o número de E é: {ve}, o número de I é: {vi}, o número de O é: {vo}, o número de U é: {vu} e o número de consoantes é: {c}")