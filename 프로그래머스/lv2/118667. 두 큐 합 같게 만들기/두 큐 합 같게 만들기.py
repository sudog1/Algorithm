from collections import deque


def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1 + sum2) % 2:
        return -1
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    for cnt in range(2*(len(deq1)+len(deq2))):
        if sum1 > sum2:
            sum1 -= deq1[0]
            sum2 += deq1[0]
            deq2.append(deq1.popleft())
        elif sum2 > sum1:
            sum2 -= deq2[0]
            sum1 += deq2[0]
            deq1.append(deq2.popleft())
        else:
            return cnt
    return -1