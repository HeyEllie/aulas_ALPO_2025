''' '' que receba N números e mostre positivo ser for postivo, negativo ou zero para cada  número.
Após informar o num. e mostrar a resposta, deve ser perguntadno se deseja informar mais um núm. (s-sim ou n-não).
OBS: a verificação deve ser realizada em uma função e depois devolvida para ser mostrado na tela.
'''
r = " "

def verifica(n):
    if n > 0:
        return("O número que você digitou é positivo")
    elif n == 0:
        return("O número que você digitou é zero")

    else:
        return("O número que você digitou é negativo")


while r != "N":
    num = int(input("Informe um número para fazer a verificação: "))
    verifica(num)
    print(verifica(num))
    r = input("Deseja fazer a verificação de outro número? S-sim; N-não: ").upper()
