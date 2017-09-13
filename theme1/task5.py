from math import sqrt

from utils.config import PRIME, COMPOSITE


def is_primary(n: int) -> bool:
    n = abs(n)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True if n != 0 else False


if __name__ == '__main__':
    for i in range(100):
        print('{0} is {1}'.format(i, PRIME if is_primary(i) else COMPOSITE))

