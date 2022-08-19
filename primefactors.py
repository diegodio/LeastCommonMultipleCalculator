def primes(n):
    prime_factor_list = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            prime_factor_list.append(d)
            n //= d
        d += 1
    if n > 1:
       prime_factor_list.append(n)
    return prime_factor_list

