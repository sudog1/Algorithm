def solution(food):
    answer = []
    for i in range(len(food)):
        for j in range(food[i]//2):
            answer.append(str(i))
    return ''.join([*answer, str(0), *reversed(answer)])