class Polynomial:
    lst = []

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return ' + '.join(
            (('{0:-d}x^{1}' if i > 1 else '{0:-d}' if i == 0 else '{0:-d}x')
             .format(v, i)) for i, v in enumerate(self.lst) if v != 0)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __len__(self):
        return len(self.lst)


if __name__ == '__main__':
    p = Polynomial([12, 2])
    p1 = Polynomial([12, 4])
    print(p == p1)
