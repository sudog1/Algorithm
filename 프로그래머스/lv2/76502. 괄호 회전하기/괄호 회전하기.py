from collections import deque

def solution(s):
    s = deque(s)
    temp = deque()
    deq = deque()
    bk = {'[':1, '{':2, '(':3, ')':5, '}':6, ']':7}
    while s:
        if not deq:
            temp.append(s[0])
            deq.append(s[0])
            s.popleft()
        else:
            if bk[deq[-1]] < 4:
                if bk[s[0]] < 4:
                    deq.append(s[0])
                    temp.append(s[0])
                    s.popleft()
                elif bk[deq[-1]] + bk[s[0]] == 8:
                    temp.append(s[0])
                    deq.pop()
                    s.popleft()
                else:
                    return 0
            else:
                if bk[s[-1]] > 4:
                    deq.appendleft(s[-1])
                    temp.appendleft(s[-1])
                    s.pop()
                elif bk[deq[0]] + bk[s[-1]] == 8:
                    temp.appendleft(s[-1])
                    deq.popleft()
                    s.pop()
                else:
                    return 0
    if deq:
        return 0
    
    count = 0
    stack = []
    for c in temp:
        if bk[c] < 4:
            stack.append(c)
        else:
            stack.pop()
        if not stack:
            count += 1
    
    return count