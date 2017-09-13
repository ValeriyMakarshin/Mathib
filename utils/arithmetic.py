
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
