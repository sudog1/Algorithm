import sys
sys.setrecursionlimit(10**5+100)
input = sys.stdin.readline

def dfs(parent, cur):
    order[0] += 1
    order[cur] = order[0]
    min_dest = order[cur]
    for child in graph[cur]:
        if parent == child:
            continue
        if order[child]:
            min_dest = min(min_dest, order[child])
            continue
        result = dfs(cur, child)
        if result > order[cur]:
            artic_edge.append(sorted([cur, child]))
        else:
            min_dest = min(min_dest, result)
        
    return min_dest

v, e = map(int, input().rstrip().split())
graph = [[] for _ in range(v+1)]
order = [0]*(v+1)
artic_edge = []

for _ in range(e):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(0, 1)
print(len(artic_edge))
for a, b in sorted(artic_edge):
    print(a, b)