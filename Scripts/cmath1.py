def extended_gcd(a, b):
    if a == 0:
        return 0, 1
    else:
        y, x = extended_gcd(b % a, a)
        return (x - (b // a) * y, y)

def modulo_inverse(a, m):
    x, y = extended_gcd(a, m)
    return x % m
