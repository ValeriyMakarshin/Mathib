import random


def fast_mod_pow(x: int, a: int, n: int) -> int:
    x %= n
    a %= n
    result = 1
    for i in '{0:b}'.format(a)[:-1]:
        if i == '1':
            result *= x
        result = (result * result) % n
    return result if a & 1 == 0 else result * x % n


def is_prime_mr(n: int, k: int = None) -> bool:
    n = abs(n)
    if n <= 3:
        return True

    s = 0
    t = n - 1
    while t % 2 == 0:
        s += 1
        t >>= 1

    for _ in range(k if k is not None else len('{0:b}'.format(n))):
        a = random.randint(2, n - 2)
        x = fast_mod_pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = fast_mod_pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                continue
        return False
    return True


if __name__ == '__main__':
    print(is_prime_mr(2147483647))
