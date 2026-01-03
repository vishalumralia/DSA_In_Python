from math import sqrt

def is_prime_optimize(n) -> bool:
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return True
    
    index = 5
    while index <= sqrt(n):
        if n % index == 0 or n % (index + 2) == 0:
            return False
        index += 6
    
    return True

def is_prime_brute_force(n) -> bool:
    if n <= 1:
        return False
    
    for num in range(2, n):
        if n % num == 0:
            return False
    
    return True

def is_prime_better(n) -> bool:
    if n <= 1:
        return False
    
    for num in range(2, int(sqrt(n)) + 1):
        if n % num == 0:
            return False
    
    return True

if __name__ == "__main__":
    n = 1000000007832
    if is_prime_optimize(n):
        print("Prime : ", n)
    else:
        print("Not Prime : ", n)