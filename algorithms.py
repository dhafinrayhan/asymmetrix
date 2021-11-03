import tools


def __rsa(mc: str, ed: int, n: int) -> str:
    blocks = tools.string_to_blocks(mc)

    new_blocks = [(block ** ed) % n for block in blocks]

    return tools.blocks_to_string(new_blocks)


def rsa_encrypt(m: str, e: int, n: int) -> str:
    return __rsa(m, e, n)


def rsa_decrypt(c: str, d: int, n: int) -> str:
    return __rsa(c, d, n)


def elgamal_encrypt(m: str, y: int, g: int, p: int, k: int) -> str:
    blocks = tools.string_to_blocks(m)

    a = (g ** k) % p
    b_blocks = [((y ** k) * block) % p for block in blocks]

    return 'a: ' + str(a) + '\nb: ' + tools.blocks_to_string(b_blocks)


def elgamal_decrypt(a: int, b: str, x: int, p: int) -> str:
    blocks = tools.string_to_blocks(b)

    reciprocal_ax = (a ** (p - 1 - x)) % p
    new_blocks = [(block * reciprocal_ax) % p for block in blocks]

    return tools.blocks_to_string(new_blocks)


def paillier_encrypt(m: str, g: int, n: int, r: int) -> str:
    blocks = tools.string_to_blocks(m)

    new_blocks = [(g ** block) * (r ** n) % (n ** 2) for block in blocks]

    return tools.blocks_to_string(new_blocks)


def paillier_decrypt(c: str, la: int, mu: int, n: int) -> str:
    blocks = tools.string_to_blocks(c)

    new_blocks = [((((block ** la) % (n ** 2)) - 1) // n * mu) % n
                  for block in blocks]

    return tools.blocks_to_string(new_blocks)
