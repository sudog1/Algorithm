def solution(a, b, n):
    answer = 0
    while n >= a:
        res = (n//a) * b
        answer += res
        n = n % a + res
    return answer