import heapq

def solution(n, k, enemy):
    answer = 0
    invinc = enemy[:k]
    heapq.heapify(invinc)
    for i in range(k, len(enemy)):
        if enemy[i] > invinc[0]:
            n -= heapq.heappop(invinc)
            heapq.heappush(invinc, enemy[i])
        else:
            n -= enemy[i]
        if n < 0:
            return i
    return len(enemy)