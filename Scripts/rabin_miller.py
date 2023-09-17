from random import randrange, getrandbits

def is_prime(n, k=128):
    """
    Check if a number is prime using the Miller-Rabin primality test.

    Args:
        n (int): The number to be tested for primality.
        k (int): The number of iterations (higher values increase accuracy).

    Returns:
        bool: True if the number is likely prime, False otherwise.
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    s = 0
    r = n - 1

    while r & 1 == 0:
        s += 1
        r //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)

        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1

            if x != n - 1:
                return False

    return True

def generate_prime_candidate(length):
    """
    Generate a random odd number of the given bit length.

    Args:
        length (int): The number of bits for the generated candidate.

    Returns:
        int: A randomly generated odd number.
    """
    candidate = getrandbits(length)
    candidate |= (1 << (length - 1)) | 1
    return candidate

def generate_prime_number(length):
    """
    Generate a prime number of the given bit length using the Miller-Rabin test.

    Args:
        length (int): The desired bit length of the prime number.

    Returns:
        int: A prime number of the specified bit length.
    """
    candidate = 4  # Initialize candidate with a non-prime value.

    while not is_prime(candidate, 128):
        candidate = generate_prime_candidate(length)

    return candidate
