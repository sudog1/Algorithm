from collections import deque

def solution(bridge_length, weight, truck_weights):
    deq = deque([0]*bridge_length)
    cur_weight = 0
    i = 0
    time = 0
    while i < len(truck_weights):
        cur_weight -= deq.popleft()
        if cur_weight+truck_weights[i] > weight:
            deq.append(0)
        else:
            deq.append(truck_weights[i])
            cur_weight += truck_weights[i]
            i += 1
        time += 1
    time += len(deq)
    return time