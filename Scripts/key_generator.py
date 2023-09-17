import random
import math
import rabin_miller  # Make sure rabin_miller module is available
import cmath1  # Make sure cmath1 module is available

def generate_rsa_key(k):
    """
    Generate an RSA key pair of size k bits.

    Args:
        k (int): The size of the key in bits.

    Returns:
        tuple: A tuple containing public and private keys (public, private).
    """
    p = rabin_miller.generate_prime_number(k)
    q = rabin_miller.generate_prime_number(k)
    n = p * q

    while True:
        e = random.randrange(2 ** (k - 1), 2 ** k - 1)
        if math.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    d = cmath1.modulo_inverse(e, (p - 1) * (q - 1))

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key
