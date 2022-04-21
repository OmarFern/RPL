# Burbujeo Optimizado (Bubble Sort with Optimization)

def f():
    pass

def burbujeo_opt(l):
    n = len(l)
    for i in range(n):
        intercambio = False
        for j in range(0, n-i-1):
            if l[j] > l [j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                intercambio = True
        if not intercambio:
            return l
    return l

l = [4, 2, 1, 5, 3]

print(burbujeo_opt(l))