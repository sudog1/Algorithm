def solution(arr, divisor):
    answer = sorted([e for e in arr if e%divisor == 0])
    return answer if answer else [-1]