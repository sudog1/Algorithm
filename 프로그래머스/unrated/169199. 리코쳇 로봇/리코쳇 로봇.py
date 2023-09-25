def move(board, x, y, dx, dy):
    while True:
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
            break
        if board[nx][ny] == "D":
            break
        x = nx
        y = ny
    return [x, y]


def solution(board):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visit = [[0]*len(board[0]) for _ in range(len(board))]
    que = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                que.append([i, j, 0])
                visit[i][j] = 1
                break
    for x, y, dist in que:
        for k in range(4):
            nx, ny = move(board, x, y, dx[k], dy[k])
            if visit[nx][ny]:
                continue
            visit[nx][ny] = 1
            if board[nx][ny] == "G":
                return dist+1
            que.append([nx, ny, dist+1])
    return -1