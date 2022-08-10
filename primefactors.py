def primes(n):
    primeFactor = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primeFactor.append(d)
            n //= d
        d += 1
    if n > 1:
       primeFactor.append(n)
    return primeFactor

