class Polynomial:
    lst = []

    def __copy__(self):
        return Polynomial(list(self.lst))

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return ' + '.join(
            (('{0:-d}x^{1}' if i > 1 else '{0:-d}' if i == 0 else '{0:-d}x')
             .format(v, i)) for i, v in enumerate(self.lst) if v != 0)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            m = min(len(self), len(other))
            return self[:m] == other[:m] and all(v == 0 for v in self[m:]) and all(v == 0 for v in other[m:])
            # return self.__dict__ == other.__dict__
        return False

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):
        return self.lst[item]

    def __iter__(self):
        return iter(self.lst)

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __reversed__(self):
        return reversed(self.lst)


if __name__ == '__main__':
    pass
