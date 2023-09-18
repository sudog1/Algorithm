def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visit = [[0]*len(maps[0]) for _ in range(len(maps))]
    stack = []
    result = []
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if not maps[i][j] == 'X' and not visit[i][j]:
                stack.append([i, j])
                visit[i][j] = 1
                food_cnt = 0
                while stack:
                    x, y = stack.pop()
                    food_cnt += int(maps[x][y])
                    for k in range(len(dx)):
                        nx, ny = x+dx[k], y+dy[k]
                        if not (0 <= nx < len(maps)) or not (0 <= ny < len(maps[i])):
                            continue
                        if maps[nx][ny] == 'X':
                            continue
                        if visit[nx][ny]:
                            continue
                        visit[nx][ny] = 1
                        stack.append([nx, ny])
                result.append(food_cnt)
    result = sorted(result)
    return result or [-1]