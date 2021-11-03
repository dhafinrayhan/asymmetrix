import math


def __lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def __egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = __egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def __modinv(a, m):
    g, x, y = __egcd(a, m)
    if g != 1:
        raise Exception('wrong input')
    else:
        return x % m


def rsa_generate(p: int, q: int) -> str:
    n = p * q
    toitent = (p - 1) * (q - 1)

    return 'n: ' + str(n) + '\nΦ(n): ' + str(toitent)


def elgamal_generate(p: int, g: int, x: int) -> str:
    y = (g ** x) % p

    return 'y: ' + str(y)


def paillier_generate(p: int, q: int, g: int) -> str:
    n = p * q
    la = __lcm(p-1, q-1)
    mu = __modinv((((g ** la) % (n ** 2)) - 1) // n, n)

    return 'n: ' + str(n) + '\nλ: ' + str(la) + '\nμ: ' + str(mu)
