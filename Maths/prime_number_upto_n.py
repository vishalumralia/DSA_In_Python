from typing import List

def sieve_of_eratosthenes_algorithm(n) -> List:
    result = []
    primes = [True] * (n + 1)

    prime = 2
    while prime * prime <= n:
        if primes[prime]:
            for num in range(prime * prime, n + 1, prime):
                primes[num] = False
        prime += 1

    for index in range(2, n+1):
        if primes[index]:
            result.append(index)

    return result

if __name__ == "__main__":
    n = 40
    print("Prime Numbers Upto : ",n, sieve_of_eratosthenes_algorithm(n))