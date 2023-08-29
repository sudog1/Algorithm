import heapq

def solution(k, score):
    answer = []
    heap_list = []
    for i, s in enumerate(score):
        heapq.heappush(heap_list, s)
        if i >= k:
            heapq.heappop(heap_list)
        answer.append(heap_list[0])
    return answer