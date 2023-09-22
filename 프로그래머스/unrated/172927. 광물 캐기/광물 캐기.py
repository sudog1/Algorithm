from math import inf


def convert(mineral):
    if mineral == "diamond":
        return 25
    elif mineral == "iron":
        return 5
    else:
        return 1


def solution(picks, minerals):
    minerals_num = list(map(convert, minerals))
    dp = [[[inf]*6 for _ in range(6)] for _ in range(6)]
    dia, iron, stone = picks
    dp[dia][iron][stone] = 0
    que = [[*picks, 0, 0]]
    min_fatigue = inf
    for *picks_state, mine_idx, fatigue in que:
        if mine_idx >= len(minerals):
            min_fatigue = min(min_fatigue, fatigue)
            continue
        dia, iron, stone = picks_state
        if dp[dia][iron][stone] < fatigue:
            continue
        for pick_idx in range(len(picks)):
            if picks_state[pick_idx] == 0:
                continue
            picks_state[pick_idx] -= 1
            pick_power = 5**(2-pick_idx)
            temp = fatigue
            for i in range(mine_idx, min(mine_idx+5, len(minerals_num))):
                temp += minerals_num[i] // pick_power + (1 if minerals_num[i] % pick_power else 0)
            dia, iron, stone = picks_state
            if dp[dia][iron][stone] <= temp:
                picks_state[pick_idx] += 1
                continue
            dp[dia][iron][stone] = temp
            que.append([*picks_state, mine_idx+5, temp])
            picks_state[pick_idx] += 1
    if dp[0][0][0] == inf:
        return min_fatigue
    return dp[0][0][0]