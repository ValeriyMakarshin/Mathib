from random import randint

from theme1.task6 import is_prime_witnesses
from utils.arithmetic import find_st


def is_prime_mr(n: int, k: int = None) -> bool:
    n = abs(n)
    if n <= 3:
        return True

    s, t = find_st(n)

    for _ in range(k if k is not None else len('{0:b}'.format(n))):
        a = randint(2, n - 2)
        if is_prime_witnesses(a, n, s, t):
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    print(is_prime_mr(2147483647))
