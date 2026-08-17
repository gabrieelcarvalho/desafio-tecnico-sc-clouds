def p_iterativo(N):

    if N <= 1:
        return "N deve ser maior que 1"
    
    primos = []
    for numeros in range(2, N + 1):
        primo = True

        for i in range(2, int(numeros ** 0.5) + 1):
            if numeros % i == 0:
                primo = False
                break

        if primo:
            primos.append(numeros)
            
    return primos

N = int(input())
print(f"p({N}) = {p_iterativo(N)}")
