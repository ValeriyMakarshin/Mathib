from theme1.polynomial import Polynomial
from utils.arithmetic import egcd


class FiniteField:
    n = None
    mn = None

    def __init__(self, n: int, mn: Polynomial = None):
        self.n = n
        self.mn = mn

    def add(self, pol1: Polynomial, pol2: Polynomial) -> Polynomial:
        result = (pol1 if len(pol1) > len(pol2) else pol2).__copy__()

        for i, v in enumerate(pol2 if len(pol1) > len(pol2) else pol1):
            result[i] += v

        return Polynomial([i % self.n for i in result])

    def sub(self, pol1: Polynomial, pol2: Polynomial) -> Polynomial:
        return self.add(pol1, Polynomial([i * -1 for i in pol2.lst]))

    def mul(self, pol1: Polynomial, pol2: Polynomial) -> Polynomial:
        if len(pol1) * len(pol2) == 0:
            return Polynomial([])

        result = [0] * (len(pol1) + len(pol2) - 1)

        for i, v1 in enumerate(pol1):
            for j, v2 in enumerate(pol2):
                result[i + j] += v1 * v2

        return Polynomial([i % self.n for i in result])

    def mod_polynomial(self, pol: Polynomial) -> Polynomial:
        pol = Polynomial(list(j % self.n for j in pol))

        if self.mn is None:
            return pol
        result = pol

        d, a, _ = egcd(self.mn[-1], self.n)

        # print('polynomial = {0}\na = {1}'.format(pol, a))

        for i in reversed(range(len(pol) - len(self.mn) + 1)):
            temp = int((a * result[i + len(self.mn) - 1] / d) % (self.n / d)) if result[i + len(self.mn) - 1] % d == 0 \
                else result[i + len(self.mn) - 1] // self.mn[-1]
            for index, v in reversed(list(enumerate(self.mn))):
                result[index + i] -= temp * v
                # print(result)
            result = Polynomial(list(j % self.n for j in result))
            # print(result)
        return result


if __name__ == '__main__':
    pass
