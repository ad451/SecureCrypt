def egcd(a, b):
    if a == 0:
        return 0, 1
    else:
        y, x = egcd(b % a, a)
        return (x - (b // a) * y, y)

def modulo_inverse(a, m):
    x, y = egcd(a, m)
    return x%m