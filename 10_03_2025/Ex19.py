'''
O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos ao preço de fábrica.
Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos.
Calcule e mostre: a) o valor correspondente ao lucro do distribuidor;
b) o valor correspondente ao imposto;
c)o preço final do veículo
'''

#variaveis
preco_veiculo = 0.0
percentual_lucro = 0.0
percentual_impostos = 0.0
valor_lucro_distribuidor = 0.0
valor_imposto = 0.0

#Programa
preco_veiculo = float(input("Informe o valor de fábrica do veículo: "))
percentual_lucro = float(input("Informe o percentual de lucro do distribuidor: "))
percentual_impostos = float(input("Informe o percentual de impostos: "))

valor_imposto = preco_veiculo * (percentual_impostos / 100)
valor_lucro_distribuidor = preco_veiculo * (percentual_lucro / 100)
preco_f = preco_veiculo + valor_lucro_distribuidor + valor_imposto

print(f"O valor correspondente ao lucro do distribuidor é de: R${valor_lucro_distribuidor:,.2f}")  #R${valor_lucro_distribuidor:,.2f} -> no máximo duas casas depois da vírgula
print(f"O valor correspondente ao imposto é de: R${valor_imposto:,.2f}")
print(f"O preço final do veículo é de: R${preco_f:,.2f}")

