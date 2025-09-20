'''
' ' que clcule a média aritmética de vários valores int positivos, lidos externamente. 
O final da leitura acontecerá quando for lido um valor negativo
'''
m = 0 
n = 0
nt = 0
cont = 0

while n >= 0:
    n = int(input("Informe um número inteiro positivo: "))
    if n >= 0:
        cont += 1
        nt += n
    

m =  nt / cont
print(f"A média foi de: {m}")
