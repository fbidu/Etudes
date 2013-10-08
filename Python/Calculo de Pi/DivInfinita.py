n = int(input("Digite o número de interações: "))
i = 0
x = 1
pi = 1/4
p = 1
while i < n:
    y = (x+2) + (i+1)**2
    z = x + (i**2)/y
    p = p/z
    i += 1
    x += 2
    pi = p/4
print(pi)
