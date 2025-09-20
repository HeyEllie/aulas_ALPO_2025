''' faça um algoritmo que determine quanto será gasto para encher o tanque de um carro. O usuário fornecerá os seguintes dados: tipos de carro (TC) (G - gasolina ou A- álcool)
 e capacidade do tanque (CT), em litros. Após a escolha do tipo de veículo e da capacidade do tanque, o sistema irá imprimir uma mensagew falando o tipo do carro (Gasolina o Álcoo) 
 e pedirá para o usuário informar o valor do preço do litro do combustível. Como saída, será informado para o usuário, o valor, em reais, do preço de se encher tanque de combustivel.
'''

#variaveis
tc = ""
ct = 0.0
combustivel = 0.0
tipo = ""
valor = 0.0

#programa
tc = input("Informe o tipo de carro: ")
ct = float(input("Informe a capacidade do tanque: "))

if(tc.upper() == "G"):    #.upper() ->
    print(f"O tipo do carro é G")
else:
    if(tc == "A"):
        print(f"O tipo do carro é A")

preco = float(input("Informe o preço do litro do combustível: "))

valor = (ct * preco) 

print(f"O valor é R${valor:,.2f} ")

