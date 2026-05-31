def primaAtauBukan(n, divisor=2):
    if n < 2:
        return False

    if divisor * divisor > n:
        return True

    if n % divisor == 0:
        return False

    return primaAtauBukan(n, divisor + 1)


# Test Case
print(primaAtauBukan(25))
print(primaAtauBukan(23))
