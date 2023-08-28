def solution(t, p):
    count = 0
    for i in range(len(t)-len(p)+1):
        for j in range(len(p)):
            if t[i+j] < p[j]:
                count += 1
                break
            elif t[i+j] > p[j]:
                break
        else:
            count += 1
    return count