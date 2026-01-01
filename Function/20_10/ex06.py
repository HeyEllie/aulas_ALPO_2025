''' alo. que recebe 5 números e ao final mostre quem é o maior e o menor múm. digitado. Deve-se fazer uma função para verificar o maior e outra para verificar o menor.
Omenor e o maior núm. devem ser retornados para o programa principal para serem mostrados'''
max = 0
min = 9999999


def maior(x):
    global max
    if x > max:
        max = x
    
    print(f"O maior é {max}")


def minimo(y):
    global min
    if y < min:
        min = y
    
    print(f"O minimo é {min}")


for i in range(0,5,1):
    num = int(input("Informe o número: "))
    maior(num)
    minimo(num)
