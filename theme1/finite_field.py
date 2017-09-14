from theme1.polynomial import Polynomial


class FiniteField:
    n = None
    mn = None

    def __init__(self, n: int, mn: Polynomial = None):
        self.n = n
        self.mn = mn

    def add(self, pol1: Polynomial, pol2: Polynomial) -> Polynomial:
        result = list(pol1.lst if len(pol1.lst) > len(pol2.lst) else pol2.lst)

        for i, v in enumerate(pol2.lst if len(pol1.lst) > len(pol2.lst) else pol1.lst):
            result[i] += v

        return Polynomial([i % self.n for i in result])

    def sub(self, pol1: Polynomial, pol2: Polynomial) -> Polynomial:
        return self.add(pol1, Polynomial([i * -1 for i in pol2.lst]))

    def mul(self, pol1: Polynomial, pol2: Polynomial) -> Polynomial:
        if len(pol1) * len(pol2) == 0:
            return Polynomial([])

        result = [0] * (len(pol1) + len(pol2) - 1)

        for i, v1 in enumerate(pol1.lst):
            for j, v2 in enumerate(pol2.lst):
                result[i + j] += v1 * v2

        return Polynomial([i % self.n for i in result])

    def mod_polynomial(self):
        # TODO: this
        pass


if __name__ == '__main__':
    pass
