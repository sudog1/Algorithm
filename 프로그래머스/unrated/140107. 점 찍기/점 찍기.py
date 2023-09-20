def solution(k, d):
    cnt = 0
    for i in range(0, d+1, k):
        remain = int((d*d - i*i)**.5)
        cnt += remain // k + 1
    return cnt