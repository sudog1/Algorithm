from itertools import permutations
from functools import reduce


def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    for i in range(2, int(n**.5) + 1 if n**.5.is_integer() else 0):
        if n % i == 0:
            return False
    return True
    
def solution(numbers):
    num_arr = set()
    for i in range(1, len(numbers)+1):
        num_arr = num_arr.union(set(map(lambda x: int(''.join(x)), permutations(numbers, i))))
    return len(list(filter(lambda x: is_prime(x), num_arr)))