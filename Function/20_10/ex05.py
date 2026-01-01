''' algo. que efetue o cálculo da tabuada de um número. O cálculo deverá ser realizado através de uma função que receberá o núm. e mostrará o resultado na tela'''

def calcular(n):
    for i in range (0,11,1):
        print(f"{n} x {i} = {n*i}")

num = int(input("Informe um número para saber sua tabuada: "))

calcular(num)