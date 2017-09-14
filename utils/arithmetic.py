def find_st(n: int) -> (int, int):
    s = 0
    t = n - 1
    while t % 2 == 0:
        s += 1
        t >>= 1
    return s, t


def find_prime_numbers(n: int) -> list:
    n = abs(n) + 1
    prime_numbers = []

    numbers = [True] * n
    numbers[0] = False

    for i in range(2, n):
        if numbers[i]:
            prime_numbers.append(i)
            for j in range(i, n, i):
                numbers[j] = False

    return prime_numbers


def fast_mod_pow(x: int, a: int, n: int) -> int:
    x %= n
    a %= n
    result = 1
    for i in '{0:b}'.format(a)[:-1]:
        if i == '1':
            result *= x
        result = (result * result) % n
    return result if a & 1 == 0 else result * x % n
