def solution(s):
    x = ''
    answer = 0
    for c in s:
        if x:
            if c == x:
                x_count += 1
            else:
                x_count -= 1
            if x_count == 0:
                answer += 1
                x = ''
        else:
            x = c
            x_count = 1
    if x:
        answer += 1
    return answer