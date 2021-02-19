n =int( input(" Type the maximum value for the Fibonacci sequence:"))
val1 = 1
val2 = 0
val3 = 0
lista_fibonacci = []

while val1 <= n:
    lista_fibonacci.append(val1)
    val3 = val1 + val2
    val2 = val1
    val1 = val3

print(lista_fibonacci)