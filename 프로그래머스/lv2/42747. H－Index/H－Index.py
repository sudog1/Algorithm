def solution(citations):
    left = 0
    right = len(citations)
    h_index = 0
    while left <= right:
        mid = (left+right) // 2
        if sum(map(lambda x: 1 if x >= mid else 0, citations)) >= mid:
            h_index = max(h_index, mid)
            left = mid+1
        else:
            right = mid-1
    return h_index