def solution(numbers):
    answer = []
    for number in numbers:
        temp = ~number & -~number
        answer.append(number + temp - temp//2)
    return answer