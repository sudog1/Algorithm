def solution(price, money, count):
    return max(sum(i for i in range(1, count+1))*price - money, 0)