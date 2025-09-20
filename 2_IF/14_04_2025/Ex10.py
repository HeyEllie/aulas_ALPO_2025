'''
comstrua um algoritmo que solicite qual operação vc deseja executar:
A para adição
S subtração
M multiplicação
D divião
Ao escolher a operação o sistema deve solicitar dois números inteiros.
Após entrar com os números o sistema deve realizar o cálculo desejando e armazenar em uma var. e imprimir a mesma na tela ao final do algoritmo.
0 se o primeiro ou segundo núm. for 0 ou menor e a operação escolhida for de div., o resultado deve dar valor 0; O valor do resultado nunca pode ser -
'''

n1 = 0
n2 = 0
ope = ""
a = 0
s = 0
m = 0
d = 0


ope = input("Informe qual operação você deseja executar: ").upper()
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

if ope == "A" :
    a = n1 + n2
else:
    if ope == "S":
        s = n1 - n2
        if(s < 0):
            s = s * -1
        print(f"O resultado é: {s}")
    else:
        if ope == "M":
            m = n1 * n2
            print(f"O resultado é: {m}")
        else:
            if ope == "D":
                d = n1 / n2
                print(f"O resultado é: {d} ")
            else:                                                                                  
                if n1==0  or n2 == 0:
                    d = (n1 / n2) == 0    
                    print(f"O resultado é: {d}")



    


