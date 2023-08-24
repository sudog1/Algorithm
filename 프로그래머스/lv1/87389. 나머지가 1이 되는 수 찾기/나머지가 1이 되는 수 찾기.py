def solution(n):
    answer = 0
    n -= 1
    if not n % 2:
        answer = 2
    else:
        for x in range(3, n+1, 2):
            if not n % x:
                answer = x
                break
    return answer