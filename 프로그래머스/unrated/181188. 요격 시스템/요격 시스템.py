def solution(targets):
    targets = sorted(targets, key=lambda x: x[0])
    cnt = 0
    prev_e = 0
    for s, e in targets:
        if prev_e <= s:
            cnt += 1
            prev_e = e
        else:
            prev_e = min(e, prev_e) 
    return cnt