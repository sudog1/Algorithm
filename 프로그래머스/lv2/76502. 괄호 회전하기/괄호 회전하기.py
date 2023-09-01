from collections import deque

def inspect(s, n):
    stack = []
    for i in s:
        if stack:
            if n[stack[-1]] < 5:
                if n[i] < 5:
                    stack.append(i)
                else :
                    stack.pop()
            else:
                return 0
        else:
            stack.append(i)
    return 1
def solution(s):
    answer = 0
    s = deque(s)
    stack = []
    n = {'[':1, '{':2, '(':3, ')':7, '}':8, ']':9}
    for i in s:
        if stack:
            if n[stack[-1]] < 5:
                if n[i] < 5:
                    stack.append(i)
                elif n[stack[-1]] + n[i] == 10:
                    stack.pop()
                else:
                    return 0
            else:
                if n[stack[-1]] + n[i] == 10:
                    stack.pop()
                else:
                    stack.append(i)
        else:
            stack.append(i)                             
    if stack:
        return 0
    for _ in range(len(s)):
        answer += inspect(s, n)
        s.append(s.popleft())
    return answer