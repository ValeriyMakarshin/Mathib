from utils.arithmetic import find_st, fast_mod_pow


def is_prime_witnesses(a: int, n: int, s: int = None, t: int = None) -> bool:
    if s is None or t is None:
        s, t = find_st(n)

    x = fast_mod_pow(a, t, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = fast_mod_pow(x, 2, n)
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False
