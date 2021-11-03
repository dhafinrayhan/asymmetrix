from textwrap import wrap


def string_to_blocks(s: str) -> list:
    return [int(x) for x in wrap(s, 4)]


def blocks_to_string(b: list) -> str:
    return ''.join([str(x).zfill(4) for x in b])


def str_to_int(s: str) -> int:
    try:
        return int(''.join(x for x in s if x.isnumeric()))
    except:
        return 0
