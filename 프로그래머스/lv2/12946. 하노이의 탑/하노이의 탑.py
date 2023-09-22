def hanoi_shift(n, process, pillars):
    if n == 0:
        return
    start, middle, end = pillars
    hanoi_shift(n-1, process, [start, end, middle])
    process.append([start, end])
    hanoi_shift(n-1, process, [middle, start, end])

def solution(n):
    process = []
    hanoi_shift(n, process, [1, 2, 3])
    return process