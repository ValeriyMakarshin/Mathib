class FiniteField:
    n = None
    mn = None

    def __init__(self, n: int, mn: list = None):
        self.n = n
        self.mn = mn

    def add(self, var1: list, var2: list) -> list:
        result = list(var1 if len(var1) > len(var2) else var2)

        for i, v in enumerate(var2 if len(var1) > len(var2) else var1):
            result[i] += v

        return [i % self.n for i in result]

    def sub(self, var1: list, var2: list):
        return self.add(var1, [i * -1 for i in var2])

    def mul(self, var1: list, var2: list) -> list:
        if len(var1) * len(var2) == 0:
            return []

        result = [0] * (len(var1) + len(var2) - 1)

        for i, v1 in enumerate(var1):
            for j, v2 in enumerate(var2):
                result[i + j] += v1 * v2

        return [i % self.n for i in result]

    def mod_polynomial(self):
        # TODO: this
        pass


if __name__ == '__main__':
    pass
