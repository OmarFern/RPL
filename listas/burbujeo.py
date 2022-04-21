# Burbujeo / Bubble Sort

def burbujeo(l):
    n = len(l)
    for i in range(n):
        # Desde la primera posición hasta la anteúltima
        for j in range(0, n-i-1):
            # Comparo adyacentes e intercambio desordenados
            if l[j] > l [j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

l = [4, 2, 1, 5, 3]

print(burbujeo(l))