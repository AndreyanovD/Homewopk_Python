# Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fibonacci(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return Fibonacci(n-1) + Fibonacci(n-2)
     
number = int(input('Введите число: '))
fib = [0]
for i in range(1, number + 1):
    fib.append(Fibonacci(i))
    sign = (-1)**(i+1)
    fib.insert(0, sign * Fibonacci(i))

print(fib)
