def solution(sizes):
    a, b = map(max, zip(*map(sorted, sizes)))
    return a*b