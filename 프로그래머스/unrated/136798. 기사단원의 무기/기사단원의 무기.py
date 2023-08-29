def count_divisor(num):
    if num == 1:
        return 1
    result = 1
    square_root = num**0.5
    for i in range(2, int(square_root)+1):
        if num % i == 0:
            result += 1
    result *= 2
    if square_root.is_integer():
        result -= 1 
    return result

def solution(number, limit, power):
    offense_score = [count_divisor(i) for i in range(1, number+1)]
    return sum(map(lambda x: x if x <= limit else power, offense_score))