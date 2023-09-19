import heapq
from math import inf

def dijk(graph, start, N):
    dist = [inf]*(N+1)
    dist[start] = 0
    prev = []
    heapq.heappush(prev, (dist[start], start))
    while prev:
        cur_dist, cur_node = heapq.heappop(prev)
        if cur_dist > dist[cur_node]:
            continue
        for i, d in enumerate(graph[cur_node]):
            if i and d < 10001:
                if dist[cur_node] + d < dist[i]:
                    dist[i] = dist[cur_node] + d
                    heapq.heappush(prev, (dist[i], i))
                    
    return dist
        
def solution(N, road, K):
    answer = 0
    graph = [[10001]*(N+1) for _ in range(N+1)]
    
    for s,e,d in road:
        graph[s][e] = min(graph[s][e], d)
        graph[e][s] = min(graph[e][s], d)
            
    dist = dijk(graph, 1, N)
    
    for i, d in enumerate(dist):
        if d <= K:
            answer += 1
    
    return answer