def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        dist = int((r2*r2 - x*x)**.5)
        if x < r1:
            temp = (r1*r1 - x*x)**.5
            dist -= int(temp)
            dist += 1 if temp.is_integer() else 0
        else:
            dist += 1
        answer += dist
    return answer*4
