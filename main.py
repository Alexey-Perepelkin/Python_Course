def exponent(a, b):
    while b > 1:
        a*=a
        b-=1
        q = exponent(a,b)
    return a
print(exponent(2, 3))
