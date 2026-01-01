''' algoritmo que receba o nome, o mês e o ano de nascimento de uma pessoa. Envie como parâmetro para uma função que irá mostrar os valores na tela'''

def mostrar(n, m, a):
    print(f"O nome da pessoa é {n} e seu mês e ano de nascimento são respectivamente {m} e {a}")

nome = input("Informe o nome: ")
mes = input("Informe o mês de nascimento: ")
ano = int(input("Informe o ano que a pessoa nasceu: "))

mostrar(nome, mes, ano)