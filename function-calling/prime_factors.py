def prime_factors(n: int) -> list[int]:
    """Returns the prime factors of a given number
    >>> prime_factors(10817567)
    [23, 47, 10007]
    """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
    return factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
