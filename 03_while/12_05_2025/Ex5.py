'''

'''
ca = 1
calculo1  = 0
calculo2  = 0
calculo3  = 0
calculo4  = 0
calculo5 = 0
total_c9 = 0
total_p = 0
total_c12 = 0
total_c23 = 0
total_c40 = 0
total_outros = 0

# total-p            total-p ----- 100%
#total-c            total-c ------- x
#x * total-p
#x = total-c * 100 / total-p
while ca != 0:
    ca = int(input("Informe o canal  (9 | 12| 23| 40): "))
    if (ca == 9):        
        total_c9 += 1
        total_p += 1
    else:
        if (ca == 12):
            total_c12 += 1
            total_p += 1
        else:
            if (ca == 23):
                total_c23 += 1
                total_p += 1
            else:
                if (ca == 40):
                    total_c40 += 1
                    total_p += 1
                else:
                    if (ca != 0):
                        total_p += 1
                        total_outros += 1

calculo1 = total_c9 * 100 / total_p
calculo2 = total_c12 * 100 / total_p
calculo3 = total_c23 * 100 / total_p
calculo4 = total_c40 * 100 / total_p
calculo5 = total_outros * 100 / total_p

print(f"A audiência do canal 9 é: {calculo1:,.2f}%")
print(f"A audiência do canal 12 é: {calculo2:,.2f}%")
print(f"A audiência do canal 23 é: {calculo3:,.2f}%")
print(f"A audiência do canal 40 é: {calculo4:,.2f}%")
print(f"A audiência dos outros canais é: {calculo5:,.2f}%")
                    