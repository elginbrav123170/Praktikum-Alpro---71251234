def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

#Test Case
print(sum_digits(234))
print(sum_digits(98765))