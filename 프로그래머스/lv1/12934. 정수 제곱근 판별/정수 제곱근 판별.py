def solution(n):
    i = 1
    while i**2 <= n:
        i += 1
    return i**2 if (i-1)**2 == n else -1