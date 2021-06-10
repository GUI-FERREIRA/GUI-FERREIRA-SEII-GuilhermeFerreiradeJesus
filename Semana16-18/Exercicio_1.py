#!/usr/bin/python3
#exercício 1
def eqdif_1(num):
    sequencia = []
    y = 1 
    for n in range(1,num+1):
        sequencia.append(y)
        y += 2
    return sequencia

def eqdif_2(num):
    sequencia = []
    y = 0
    for n in range(1,num+1):
        y = y + n
        sequencia.append(y)
    return sequencia

def eqdif_3(num):
    sequencia = []
    for n in range(1,num+1):
        y = n*n
        sequencia.append(y)
    return sequencia 

if __name__ == '__main__':
    num = 20   
    print(eqdif_1(num))
    print(eqdif_2(num))
    print(eqdif_3(num))