def solution(X, Y):
    x_cnt = [0]*10
    y_cnt = [0]*10
    for c in X:
        x_cnt[int(c)] += 1
    for c in Y:
        y_cnt[int(c)] += 1
    digit_list = []
    for i in range(9, 0, -1):
        for _ in range(min(x_cnt[i], y_cnt[i])):
            digit_list.append(f'{i}')
            
    if not digit_list:
        if min(x_cnt[0], y_cnt[0]):
            return '0'
        else:
            return '-1'
        
    for _ in range(min(x_cnt[0], y_cnt[0])):
        digit_list.append('0')
        
    return ''.join(digit_list)