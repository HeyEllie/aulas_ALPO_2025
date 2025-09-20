'''
Contrua um algoritmo que leia o valor de uma conta de luz(LC) e, caso o valor seja maior que R$80,00 apresente a mensagem: "Você está gastando muito!!!". 
Caso contráro exiba a mensagem : Seu gasto foi nomrla!!!"
'''

#variaveis
valor_conta = 0.0
x = ""
y = 0

#programa
valor_conta = float(input("Informe o valor da conta: "))

if(valor_conta > 80):
    print(f"Você está gastando muito!!!")
else:
    print(f"Seu gasto foi normal!!!")