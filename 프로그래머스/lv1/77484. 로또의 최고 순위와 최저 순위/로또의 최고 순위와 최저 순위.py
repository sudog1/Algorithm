def solution(lottos, win_nums):
    win_index = [0]*46
    for num in win_nums:
        win_index[num] = 1
    match_cnt = 0
    zero_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
            continue
        if win_index[lotto]:
            match_cnt += 1
    best = min(6, 7-(match_cnt+zero_cnt))
    lowest = min(6, 7-match_cnt)
    return [best, lowest]