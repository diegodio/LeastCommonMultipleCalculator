def primes(n):
    primeFactorList = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primeFactorList.append(d)
            n //= d
        d += 1
    if n > 1:
       primeFactorList.append(n)
    return primeFactorList

