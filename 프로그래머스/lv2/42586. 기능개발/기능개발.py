def solution(progresses, speeds):
    result = []
    for i in range(len(progresses)):
        if progresses[i] >= 100:
            continue
        count = 0
        while progresses[i] < 100:
            for j in range(i, len(progresses)):
                progresses[j] += speeds[j]
        for j in range(i, len(progresses)):
            if progresses[j] < 100:
                break
            count += 1
        result.append(count)
    return result