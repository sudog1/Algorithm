import sys
input = sys.stdin.readline


def make_tree():
    que = [1]
    for node in que:
        visit[node] = 1
        for i in range(1, 17):
            if not parent[i-1][node]:
                break
            parent[i][node] = parent[i-1][parent[i-1][node]]
            min_edge[i][node] = min(min_edge[i-1][node], min_edge[i-1][parent[i-1][node]])
            max_edge[i][node] = max(max_edge[i-1][node], max_edge[i-1][parent[i-1][node]])
        for b, c in graph[node]:
            if visit[b]:
                continue
            parent[0][b] = node
            min_edge[0][b] = c
            max_edge[0][b] = c
            depth[b] = depth[node]+1
            que.append(b)
        
def find_lca(a, b):
    min_res = 1_000_001
    max_res = 0
    a, b = (a, b) if depth[a] >= depth[b] else (b, a)
    while depth[a] != depth[b]:
        for i in range(1, 18):
            if not parent[i][a] or depth[parent[i][a]] < depth[b]:
                min_res = min(min_res, min_edge[i-1][a])
                max_res = max(max_res, max_edge[i-1][a])
                a = parent[i-1][a]
                break
    if a == b:
        return (min_res, max_res)
    while parent[0][a] != parent[0][b]:
        for i in range(1, 18):
            if not parent[i][a] or parent[i][a] == parent[i][b]:
                min_res = min(min_res, min_edge[i-1][a], min_edge[i-1][b])
                max_res = max(max_res, max_edge[i-1][a], max_edge[i-1][b])
                a = parent[i-1][a]
                b = parent[i-1][b]
                break
    min_res = min(min_res, min_edge[0][a], min_edge[0][b])
    max_res = max(max_res, max_edge[0][a], max_edge[0][b])
    return (min_res, max_res)

n = int(input())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
min_edge = [[1_000_001]*(n+1) for _ in range(18)]
max_edge = [[0]*(n+1) for _ in range(18)]
parent = [[0]*(n+1) for _ in range(18)]
depth = [0]*(n+1)
depth[1] = 1
for _ in range(n-1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

make_tree()
k = int(input())
for _ in range(k):
    a, b = map(int, input().rstrip().split())
    print(*find_lca(a, b))