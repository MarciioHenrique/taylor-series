def termo_taylor(x, i, termo_anterior):
    return termo_anterior * (x / i)

def somar_termos(x, n, i=1, termo=1, resultado=1):
    if i >= n:
        return resultado
    novo_termo = termo_taylor(x, i, termo)
    return somar_termos(x, n, i + 1, novo_termo, resultado + novo_termo)

def calcular_ex_taylor(x, n):
    return somar_termos(x, n)

def calcular_ex_negativo(x, n):
    direto = calcular_ex_taylor(x, n)
    inverso = 1 / calcular_ex_taylor(-x, n)
    return direto, inverso
    
def criar_tabela_testes(valores_x, valores_n):
    print(f"{'x':^8} {'n':^8} {'e^x Direto':^15} {'1/e^-x':^15} {'Valor Esperado':^15}")
    print("-" * 65)
    
    import math  
    
    for x in valores_x:
        for n in valores_n:
            if x >= 0:
                resultado = calcular_ex_taylor(x, n)
                esperado = math.exp(x)
                print(f"{x:^8.2f} {n:^8} {resultado:^15.6f} {'-':^15} {esperado:^15.6f}")
            else:
                direto, inverso = calcular_ex_negativo(x, n)
                esperado = math.exp(x)
                print(f"{x:^8.2f} {n:^8} {direto:^15.6f} {inverso:^15.6f} {esperado:^15.6f}")


print("Digite os valores de x (separados por espaço): ")
valores_x = [float(x) for x in input().split()]

print("Digite os valores de n (número de termos, separados por espaço): ")
valores_n = [int(n) for n in input().split()]

criar_tabela_testes(valores_x, valores_n)
