def solution(n,a,b):
    a, b = min(a, b), max(a, b)
    count = 1
    while True:
        if b-a == 1 and a%2:
            break
        if a%2:
            a += 1
        a //= 2
        if b%2:
            b += 1
        b //= 2
        count += 1
    return count