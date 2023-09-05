def solution(word):
    weight = [1]
    seq = {
        'A': 0,
        'E': 1,
        'I': 2,
        'O': 3,
        'U': 4
    }
    for _ in range(4):
        weight.append(weight[-1]*5+1)
    weight.reverse()
    total = 0
    for i, c in enumerate(word):
        total += weight[i]*seq[c]+1
    return total