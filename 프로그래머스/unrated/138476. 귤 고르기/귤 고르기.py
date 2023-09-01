def solution(k, tangerine):
    cnt_dict = {}
    for t in tangerine:
        if t in cnt_dict:
            cnt_dict[t] += 1
        else:
            cnt_dict[t] = 1
            
    temp = list(sorted(cnt_dict.values(), reverse=True))
    type_cnt = 0
    for a in temp:
        if k <= 0:
            break
        k -= a
        type_cnt += 1
        
    return type_cnt