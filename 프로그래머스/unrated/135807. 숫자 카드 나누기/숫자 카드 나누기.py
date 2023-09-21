from functools import reduce
from math import gcd


def solution(arrayA, arrayB):
    gcd_A = reduce(lambda acc, x: gcd(acc, x), arrayA, arrayA[0])
    if list(filter(lambda x: not x%gcd_A, arrayB)):
        gcd_A = 0
    gcd_B = reduce(lambda acc, x: gcd(acc, x), arrayB, arrayB[0])
    if list(filter(lambda x: not x%gcd_B, arrayA)):
        gcd_B = 0
    return max(gcd_A, gcd_B)