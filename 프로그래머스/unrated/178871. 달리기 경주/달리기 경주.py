def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}
    temp = players[:]
    for c in callings:
        if rank[c]:
            cur_rank = rank[c]
            rank[temp[cur_rank-1]] += 1
            rank[c] -= 1
            temp[cur_rank], temp[cur_rank-1] = temp[cur_rank-1], temp[cur_rank]
            
    return temp