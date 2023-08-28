import sys, math
from functools import cmp_to_key

input = sys.stdin.readline

def compare(key1, key2):
    _, x1, y1 = key1
    _, x2, y2 = key2
    if y1 == 0:
        if y2 == 0:
            return x1-x2
        else:
            return -1
    elif y2 == 0:
        return 1
    x1 *= y2
    x2 *= y1
    if x1 == x2:
        return y1-y2
    else:
        return x2-x1
        
c = int(input())
for _ in range(c):
    n, *arr = map(int, input().rstrip().split())
    point = []
    for i in range(n):
        point.append([i, arr[2*i], arr[2*i+1]])
    
    org_p, org_x, org_y = min(point, key=lambda x: (x[2], x[1]))
    rel_point = [[i, x-org_x, y-org_y] for i, x, y in point]
    rel_point.sort(key=cmp_to_key(compare))
    que = [rel_point.pop()]
    while True:
        _, x1, y1 = que[-1]
        _, x2, y2 = rel_point[-1]
        if x1*y2 == x2*y1:
            que.append(rel_point.pop())
        else:
            break
    rel_point += que
    order = [p[0] for p in rel_point]
    print(*order)