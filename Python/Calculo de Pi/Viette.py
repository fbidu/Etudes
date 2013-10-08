# -*- encoding: latin-1 -*- 
n = int(input("Digite o número de interações: "))
i = 0
x = 0
pi = 2
while i < n:
    x = ((2 + x)**0.5)
    pi = pi*(2/x)
    i += 1
    print(pi)