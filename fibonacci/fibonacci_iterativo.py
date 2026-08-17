def fib_iterativo(N):

    if N <= 0:
        return "N deve ser maior que 0"
    
    elif N == 1:
        return 1
    
    else:
        valores = [1, 1]
        
        for i in range(3, N + 1):
            fib_i = sum(valores[-2:])
            valores.append(fib_i)
        return valores[-1]

N = int(input())
print(f"fib({N}) = {fib_iterativo(N)}")