def PenjumlahanDeretGanjil(n):
    if n == 1:
        return 1
    else:
        return (2**n - 1) + PenjumlahanDeretGanjil(n - 1)
    
#Test Case
print(PenjumlahanDeretGanjil(3))
print(PenjumlahanDeretGanjil(4))