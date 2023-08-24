def solution(n):
    answer = 0
    i = 1
    while i*i <= n:
        if not n % i:
            temp = n / i
            if i != temp:
                answer += i+temp
            else:
                answer += i
        i += 1
    return answer