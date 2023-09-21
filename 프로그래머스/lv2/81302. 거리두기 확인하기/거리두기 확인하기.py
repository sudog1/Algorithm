def dfs(place, visit, r, c):
    que = [[r, c, 0]]
    for x, y, dist in que:
        if dist >= 2:
            continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue
            if visit[nx][ny]:
                continue
            if place[nx][ny] == 'X':
                continue
            elif place[nx][ny] == 'P':
                return 0
            visit[nx][ny] = 1
            que.append([nx, ny, dist+1])
    return 1
            
            

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
    
    
def solution(places):
    answer = []
    for k in range(len(places)):
        visit = [[0]*5 for _ in range(5)]
        flag = 1
        for i in range(5):
            if not flag:
                break
            for j in range(5):
                if places[k][i][j] == 'P' and not visit[i][j]:
                    visit[i][j] = 1
                    if not dfs(places[k], visit, i, j):
                        flag = 0
                        break
        answer.append(flag)
    return answer