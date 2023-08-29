def solution(n, m, section):
    count = 0
    last_idx = 0
    for wall in section:
        if wall > last_idx:
            count += 1
            last_idx = wall+m-1
    return count