from math import gcd
from functools import reduce

def solution(arr):
    return reduce(lambda acc, x: acc*x//gcd(acc, x), arr, 1)