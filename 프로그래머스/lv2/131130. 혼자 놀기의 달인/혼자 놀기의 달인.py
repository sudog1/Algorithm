def solution(cards):
    answer = 0
    box = [0 for _ in range(len(cards))]
    result = []
    for i, card in enumerate(cards):
        if box[i]:
            continue
        box[i] = 1
        count = 1
        while not box[card-1]:
            box[card-1] = 1
            card = cards[card-1]
            count += 1
        result.append(count)
    if len(result) < 2:
        return 0
    result.sort(reverse=True)
    return result[0]*result[1]