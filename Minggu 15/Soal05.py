def kombinasi(n, r):
    if r == 0 or r == n:
        return 1
    return kombinasi(n - 1, r - 1) + kombinasi(n - 1, r)

#Test Case
print(kombinasi(5, 2))
print(kombinasi(6, 3))