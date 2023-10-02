def solution(board):
    cnt = {'O': 0, 'X': 0}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '.':
                cnt[board[i][j]] += 1
    gap = cnt['O'] - cnt['X']
    if not 0 <= gap <= 1:
        return 0
    
    winO = False
    winX = False
    for row in board:
        if row == "OOO":
            winO = True
        if row == "XXX":
            winX = True
    if winO:
        if winX:
            return 0
        if gap == 0:
            return 0
        return 1
    elif winX:
        if gap == 1:
            return 0
        return 1
    
    winO = False
    winX = False
    for col in map(lambda x: ''.join(x), zip(*board)):
        if col == "OOO":
            winO = True
        if col == "XXX":
            winX = True
    if winO:
        if winX:
            return 0
        if gap == 0:
            return 0
        return 1
    elif winX:
        if gap == 1:
            return 0
        return 1

    dia1 = ''.join([board[i][i] for i in range(3)])
    winO = False
    winX = False
    if dia1 == "OOO":
        winO = True
    elif dia1 == "XXX":
        winX = True
    if winO:
        if gap == 0:
            return 0
        return 1
    elif winX:
        if gap == 1:
            return 0
        return 1
    
    dia2 = ''.join([board[i][2-i] for i in range(3)])
    winO = False
    winX = False
    if dia2 == "OOO":
        winO = True
    elif dia2 == "XXX":
        winX = True
    if winO:
        if gap == 0:
            return 0
        return 1
    elif winX:
        if gap == 1:
            return 0
        return 1
        
    return 1