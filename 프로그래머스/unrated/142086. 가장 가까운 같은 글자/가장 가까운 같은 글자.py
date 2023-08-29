def solution(s):
    near_idx = {}
    answer = []
    for i, c in enumerate(s):
        if c in near_idx:
            answer.append(i - near_idx[c])
        else:
            answer.append(-1)
        near_idx[c] = i
    return answer