from math import sqrt

def solution(n):
    x = sqrt(n)
    if x.is_integer():
        answer = (x+1)**2
    else:
        answer = -1
    return answer