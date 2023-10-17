def solution(grid):
    def shoot(x, y, d):
        cycle_len = 0
        while not visit[x][y][d]:
            visit[x][y][d] = 1
            if grid[x][y] == 'L':
                d = (d+3) % 4
            elif grid[x][y] == 'R':
                d = (d+1) % 4
            x = (x+dx[d]+len(grid)) % len(grid)
            y = (y+dy[d]+len(grid[0])) % len(grid[0])
            cycle_len += 1
        return cycle_len
        
    visit = [[[0]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    answer = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for d in range(len(dx)):
                if visit[i][j][d]:
                    continue
                answer.append(shoot(i, j, d))
    return sorted(answer)