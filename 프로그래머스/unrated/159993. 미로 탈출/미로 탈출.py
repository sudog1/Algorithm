dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find(maps, start_pos, target):
    que = [start_pos]
    visit = [[0]*len(maps[0]) for _ in range(len(maps))]
    for x, y, dist in que:
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < len(maps) and 0 <= ny < len(maps[0])):
                continue
            if maps[nx][ny] == 'X':
                continue
            if maps[nx][ny] == target:
                return [nx, ny, dist+1]
            if visit[nx][ny]:
                continue
            visit[nx][ny] = 1
            que.append([nx, ny, dist+1])
    return 0
    
    
def solution(maps):
    total_dist = 0
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                lever_pos = find(maps, [i, j, 0], 'L')
                if lever_pos:
                    result = find(maps, lever_pos, 'E')
                    return result[2] if result else -1
                else:
                    return -1   
                