import math

def fatora(num):
    raiz = int(math.sqrt(num))
    
    lista = [x for x in range(2, num + 1) if (x % 2 != 0) or (x == 2)]
    aux = 3
    
    while aux <= raiz:
        for i in lista:
            if ((i % aux) == 0) and i != aux:
                lista[lista.index(i)] = 0
        aux += 1
        
    primos = []
    
    for i in lista:
        if i != 0:
            primos.append(i)
    
    fatorado = []
    index = 0
    den = primos[index]
    
    while num != 1:
        if (num % primos[index]) == 0:
            num = num / primos[index]
            fatorado.append(primos[index])
        else:
            index += 1

    return fatorado

if __name__ == '__main__':
    fatores = fatora(126)
    print(fatores)