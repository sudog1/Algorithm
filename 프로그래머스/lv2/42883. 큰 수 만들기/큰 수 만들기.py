def solution(number, k):
    number_arr = list(number)
    result = []
    for digit in number_arr:
        while k and result and result[-1] < digit:
            result.pop()
            k -= 1
        result.append(digit)
    for i in range(k):
        result.pop()
    return ''.join(result)