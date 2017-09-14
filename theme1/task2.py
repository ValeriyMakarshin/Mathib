from theme1.task7 import is_prime_mr
from utils.arithmetic import egcd


def field_order(a, n):
    if is_prime_mr(n):
        return n - 1
    d, _, _ = egcd(a, n)
    if d != 1:
        return None

    i = 1
    x = a
    while x != 1 and i < n:
        i += 1
        x = (x * a) % n
    return i if x == 1 else None


if __name__ == '__main__':
    print(field_order(3, 22))
    print(pow(3, 10, 22))
