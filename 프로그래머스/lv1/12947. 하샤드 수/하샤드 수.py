def solution(x):
    digit_sum = 0
    temp = x
    while temp:
        digit_sum += temp%10
        temp //= 10
    return not x % digit_sum