from utils.arithmetic import find_prime_numbers


def fun_euler(n):
    result = 1
    dividers = {k: 0 for _, k in enumerate(find_prime_numbers(int(n)))}
    dividers
    used_dividers = set()
    for i in dividers:
        while n % i == 0:
            dividers[i] += 1
            used_dividers.add(i)
            n /= i

    for i in used_dividers:
        result *= int(pow(i, dividers[i] - 1) * (i - 1))

    return result


if __name__ == '__main__':
    print(fun_euler(11))
