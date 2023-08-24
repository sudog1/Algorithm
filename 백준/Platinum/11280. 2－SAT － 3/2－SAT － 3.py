import sys
sys.setrecursionlimit(10**5+100)
input = sys.stdin.readline

def get_scc(v):
    if order[v]:
        return 
    order[0] += 1
    order[v] = order[0]
    res = order[v]
    stack.append(v)
    for child in graph[v]:
        if not order[child]:
            res = min(res, get_scc(child))
        elif not scc[child]:
            res = min(res, order[child])
    if res == order[v]:
        scc[0] += 1
        while True:
            e = stack.pop()
            scc[e] = scc[0]
            if e == v:
                break
    return res

n, m = map(int, input().rstrip().split())
order = [0]*(2*n+1)
scc = [0]*(2*n+1)
graph = [[] for _ in range(2*n+1)]
stack = []

def main():
    for _ in range(m):
        i, j = map(int, input().rstrip().split())
        graph[-i].append(j)
        graph[-j].append(i)
        
    for i in range(-n, n+1):
        if graph[i] and not scc[i]:
            get_scc(i)
    
    scc_set = [0]*(scc[0]+1)
    for i in range(-n, n+1):
        if scc[i]:
            if scc_set[scc[i]]:
                if -i in scc_set[scc[i]]:
                    return 0
                else:
                    scc_set[scc[i]].add(i)
            else:
                scc_set[scc[i]] = {i}
    return 1

print(main())