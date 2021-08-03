import cmath1
import rabin_miller
import random
import math
def key(k):
    p=rabin_miller.generate_prime_number(k)
    q=rabin_miller.generate_prime_number(k)
    n=p*q
    while True:
      e = random.randrange(2 ** (k-1), 2 ** (k)-1)
      if math.gcd(e, (p - 1) * (q - 1)) == 1:
         break
    d = cmath1.modulo_inverse(e,(p - 1) * (q - 1)); 
    public=(n,e)
    private=(n,d)
    return public,private       


