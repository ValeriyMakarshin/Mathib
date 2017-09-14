from theme1.polynomial import Polynomial
from utils.arithmetic import mod_inv


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
        result = pol.__copy__()

        a = mod_inv(self.mn[-1], self.n)

        # print('polynomial = {0}\na = {1}'.format(pol, a))

        if a is not None:
            for i in reversed(range(len(pol) - len(self.mn) + 1)):
                temp = (a * result[i + len(self.mn) - 1] % self.n)
                for index, v in reversed(list(enumerate(self.mn))):
                    result[index + i] -= temp * v
                # print(result)
                result = Polynomial(list(j % self.n for j in result))
        return result


if __name__ == '__main__':
    p1 = Polynomial([1, 2, 3, 4, 5])
    p2 = Polynomial([3, 4, 5])
    pmn = Polynomial([-1, 2])
    ff = FiniteField(7, pmn)
    print(ff.add(p1, p2))
