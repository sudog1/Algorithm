import heapq
from collections import deque

def get_standby_time(arr, m):
    standby_time = 0
    state_queue = []
    for a, b in arr:
        if m == 0:
            end_time = heapq.heappop(state_queue)
            m += 1
            if end_time > a:
                standby_time += end_time - a
                a = end_time
        m -= 1
        heapq.heappush(state_queue, a+b)
    return standby_time

def solution(k, n, reqs):
    answer = 0
    counsel = [[] for _ in range(k)]
    
    for a, b, c in reqs:
        counsel[c-1].append([a, b])
    standby_time_arr = [[get_standby_time(counsel[i], 1) for i in range(k)], [0]*k]
    time_gap = []
    
    for i in range(k):
        if standby_time_arr[0][i] == 0:
            continue
        standby_time = get_standby_time(counsel[i], 2)
        heapq.heappush(time_gap, [-(standby_time_arr[0][i] - standby_time), i, 2])
        standby_time_arr[1][i] = standby_time
        
    for _ in range(n-k):
        if not time_gap:
            break
        _, i, m = heapq.heappop(time_gap)
        standby_time = get_standby_time(counsel[i], m+1)
        heapq.heappush(time_gap, [-(standby_time_arr[1][i] - standby_time), i, m+1])
        standby_time_arr[0][i] = standby_time_arr[1][i]
        standby_time_arr[1][i] = standby_time
        
    return sum(standby_time_arr[0])