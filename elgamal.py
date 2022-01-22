import random

from params import p
from params import g

def keygen():
    sk = random.randint(0, (p - 1)/2)
    pk = pow(g, sk, p)
    return pk,sk

def encrypt(pk,m):
    r = keygen()[1]
    c1 = pow(g, r, p)
    x1 = pow(pk, r, p)
    x2 = m % p
    c2 = (x1 * x2) % p
    return [c1,c2]

def decrypt(sk,c):
    c1 = c[0]
    c2 = c[1]
    m = ((c2 % p) * (pow(c1, -sk, p))) % p
    return m

