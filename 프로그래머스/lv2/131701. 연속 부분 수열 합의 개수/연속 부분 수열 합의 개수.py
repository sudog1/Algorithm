def solution(elements):
    result = set()
    for i in range(len(elements)):
        total = 0
        for j in range(len(elements)):
            total += elements[(i+j) % len(elements)]
            result.add(total)
    return len(result)