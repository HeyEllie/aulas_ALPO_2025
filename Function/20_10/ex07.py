''' que receba três notas de um launo como parÂmetros e o tipo da média que deverá ser calculada.
Se o tipo da média for "A" a função calcula a média aritmética das notas do aluno, se for "P" a função calcula a média ponderada com os pesos 5, 3 e 2 respectivamente. A média calculada
deve ser devolvida ao prgrama principal para, então, ser mostrada '''

''' poderia usar uma function só
def calc_media(n1,n2,3,tipo):
if tipo == "a":
    media_f = (n1+n2+n3) /3
    elif media_f = (n1*5 + n2 * 3 + n3*2)/(5+3+2)
    return mdia_f

media_media = calc_media (nota1, nota2, nota3, media)
print(media)
'''


def media_aritmetica(n1, n2, n3):
    med_a = (n1 + n2 + n3) / 3
    return med_a

def media_ponderada(n1, n2, n3):
    med_p = ((n1 /100)*50) + ((n2 / 100) * 30) + ((n3 / 100) * 20)
    return med_p


nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
media = input("Qual média deseja fazer? \nA - aritmética \nP - ponderada: ") #.upper()

if media == "p":
    print(f"A média foi de {media_ponderada(nota1, nota2, nota3)}")
elif media == "a":
    print(f"A média foi de {media_aritmetica(nota1, nota2, nota3)}")

