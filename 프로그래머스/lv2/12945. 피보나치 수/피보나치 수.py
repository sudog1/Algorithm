def solution(n):
    fibo_num = [0, 1]
    for i in range(n-1):
        fibo_num[i%2] = (fibo_num[0]+fibo_num[1]) % 1234567
    return fibo_num[n%2]