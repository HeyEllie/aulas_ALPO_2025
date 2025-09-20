'''
'' que calcula a tabuada de um num e mostra na tela.
o algo. deve solicitar um num e mostrar a tabuada deste num até que o num0 seja digitado
não calcula a do 0 e deve utilizar somente while
'''

n = 1
contador = 0

while n != 0:
    n = int(input("Informe um número para tabuada: "))
    if n != 0:
        contador = 0
        while contador <= 10:
            contador += 1
            print(f"{n} X {contador} = {n * contador}")
