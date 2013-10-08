n = int(input("Digite o número de interações: "))
pi = 2
i = 0
x = 2
while i < n:
    pi = pi*(x/(x-1))*(x/(x+1))
    x += 2
    i += 1
    print(pi)
