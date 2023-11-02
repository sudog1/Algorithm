from collections import deque, defaultdict
from math import inf

def solution(temperature, t1, t2, a, b, onboard):
    # 실외온도에서 희망온도로 이동
    if temperature - t1 > 0:
        step = -1
    else:
        step = 1
    # 온도 범위
    if step < 0:
        left = t1
        right = temperature
    else:
        left = temperature
        right = t2
    dp = [[inf]*52 for _ in range(len(onboard))]
    dp[0][temperature] = 0
    deq = deque()
    # 비용, 현재 온도
    deq.append([0, temperature])
    for time in range(len(onboard)-1):
        # 최저 비용 저장
        check = defaultdict(lambda: inf)
        while deq:
            cost, temp = deq.popleft()
            gap = temperature - temp
            if gap > 0:
                r_step = 1
            elif gap == 0:
                r_step = 0
            else:
                r_step = -1
            if check[temp+r_step] > cost:
                check[temp+r_step] = cost
            if check[temp+step] > cost+a:
                check[temp+step] = cost+a
            if check[temp] > cost+b:
                check[temp] = cost+b
        for temp in check:
            if onboard[time+1]:
                if not t1 <= temp <= t2:
                    continue
            if not left <= temp <= right:
                continue
            dp[time+1][temp] = check[temp]
            deq.append([dp[time+1][temp], temp])
    return min(dp[len(onboard)-1])