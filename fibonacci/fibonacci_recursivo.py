def fib_recursivo(N):

    if N < 0:
        return "O valor de n precisa ser maior que 0."
    
    elif N == 0:
        return 0
    
    elif N == 1:
        return 1
    
    return fib_recursivo(N - 1) + fib_recursivo(N - 2)

N = int(input())
print(f"fib({N}) = {fib_recursivo(N)}")