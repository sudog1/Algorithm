def solution(n):
    arr = []
    while n:
        arr.append(n%10)
        n //= 10
    answer = 0
    for i in sorted(arr, reverse=True):
        answer *= 10
        answer += i
    return answer