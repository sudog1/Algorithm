def gen_hail_series(k):
    hail_series = [k]
    while k > 1:
        if not k % 2:
            k /= 2
        else:
            k = k*3 + 1
        hail_series.append(k)
    return hail_series


def solution(k, ranges):
    hail_series = gen_hail_series(k)
    acc_list = [0]
    for i in range(1, len(hail_series)):
        acc_list.append(acc_list[i-1] + hail_series[i] / 2)
        acc_list[i] += (hail_series[i-1] / 2)
    answer = []
    for a, b in ranges:
        if a >= len(acc_list) or b <= -len(acc_list):
            answer.append(-1)
            continue
        acc_sum = acc_list[b-1] - acc_list[a]
        answer.append(acc_sum if acc_sum >= 0 else -1)
    return answer