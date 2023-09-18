def dfs(maps, visit, x, y):
    stack = []
    visit[x][y] = 1
    stack.append([x, y])
    food_cnt = 0
    while stack:
        x, y = stack.pop()
        food_cnt += int(maps[x][y])
        for k in range(len(dx)):
            nx, ny = x+dx[k], y+dy[k]
            if not (0 <= nx < len(maps)) or not (0 <= ny < len(maps[x])):
                continue
            if maps[nx][ny] == 'X':
                continue
            if visit[nx][ny]:
                continue
            visit[nx][ny] = 1
            stack.append([nx, ny])
    return food_cnt

            
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(maps):
    result = []
    visit = [[0]*len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if not maps[i][j] == 'X' and not visit[i][j]:
                result.append(dfs(maps, visit, i, j))
    result = sorted(result)
    return result or [-1]