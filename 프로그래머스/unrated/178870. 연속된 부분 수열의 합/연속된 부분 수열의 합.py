def solution(sequence, k):
    total = 0
    s_idx = 0
    e_idx = -1
    answer = [len(sequence), s_idx]
    
    while True:
        if total == k:
            if e_idx-s_idx < answer[0]:
                answer = [e_idx-s_idx, s_idx]
        if total <= k:
            e_idx += 1
            if e_idx >= len(sequence):
                break
            total += sequence[e_idx]
        else:
            total -= sequence[s_idx]
            s_idx += 1
            if s_idx > e_idx:
                break
    return [answer[1], sum(answer)]