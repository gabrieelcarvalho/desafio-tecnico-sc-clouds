def primo(numero, divisor):

    if divisor > numero ** 0.5:
        return True
    
    if numero % divisor == 0:
        return False
    
    return primo(numero, divisor + 1)

def p_recursiva(N, numero, lista_primos):

    if numero > N:
        return lista_primos
    
    if primo(numero, 2) is True:
        lista_primos.append(numero)

    return p_recursiva(N, numero + 1, lista_primos)

numero = 2
lista_primos = []

N = int(input())
if N <= 1:
    print("N deve ser maior que 1")
else:
    print(f"p({N}) = {p_recursiva(N, numero, lista_primos)}")