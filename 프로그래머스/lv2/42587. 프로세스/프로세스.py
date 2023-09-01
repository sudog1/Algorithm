from collections import deque

def solution(priorities, location):
    deq = deque(enumerate(priorities))
    remain = sorted(priorities)
    count = 0
    while deq:
        i, p = deq.popleft()
        if p == remain[-1]:
            count += 1
            if i == location:
                return count
            remain.pop()
        else:
            deq.append([i, p])