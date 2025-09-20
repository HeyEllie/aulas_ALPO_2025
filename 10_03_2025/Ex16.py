'''
Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma
residência. Calcule e mostre: 
a) o valor, em reais, de cada quilowatt;
b) o valor, em reais, a ser pago por essa residência;
c) o valor, em reais, a ser pago com desconto de 15%;
'''

#variaveis
salario = 0.0
quilowatt_gasto = 0.0
quilowatt = 0.0
valor_para_pagar = 0.0
desconto = 0.0


#programa
salario = float(input("Informe o valor do salário mínimo: "))
quilowatt_gasto = float(input("Informe o valor gasto de quilowatt: "))

quilowatt = salario / 5
valor_para_pagar = quilowatt * quilowatt_gasto
desconto = valor_para_pagar - (valor_para_pagar * 15) / 100

print(f"O valor de cada quilowatt é {quilowatt}")
print(f"O valor a ser pago sem desconto é{ valor_para_pagar}")
print(f"O valor a ser pago com desconto é {desconto}")