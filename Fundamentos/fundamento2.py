# Dada uma matriz não vazia de inteiros, retorne o resultado da multiplicação dos valores em ordem. Exemplo:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

from math import prod

def grow(arr):
    arr = sorted(arr)
    return prod(arr)


print(grow([1,2,3,4]))

# Resolução mais eficiente

# from math import prod

# def grow(arr):
#     return prod(sorted(arr))