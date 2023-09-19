import heapq


def dijkstra(N, graph, cost, K):
    dist = [K+1]*(N+1)
    dist[1] = 0
    heap = [[dist[1], 1]]
    while heap:
        d, node = heapq.heappop(heap)
        if dist[node] < d:
            continue
        for adj in graph[node]:
            if dist[adj] > d+cost[node][adj]:
                dist[adj] = d+cost[node][adj]
                heapq.heappush(heap, [dist[adj], adj])
    return dist


def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    cost = [[0]*(N+1) for _ in range(N+1)]
    for a, b, c in road:
        if cost[a][b]:
            if cost[a][b] > c:
                cost[a][b] = c
                cost[b][a] = c
        else:
            graph[a].append(b)
            graph[b].append(a)
            cost[a][b] = c
            cost[b][a] = c
    dist = dijkstra(N, graph, cost, K)
    return len(list(filter(lambda x: x <= K, dist)))