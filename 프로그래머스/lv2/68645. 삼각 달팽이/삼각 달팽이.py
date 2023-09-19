def solution(n):
    answer = []
    slag = [[0]*n for _ in range(n+1)]
    direct = [[1, 0], [0, 1], [-1, -1]]
    x, y = 0, 0
    cur_dir = 0
    for cnt in range(n, 0, -1):
        dx, dy = direct[cur_dir]
        for _ in range(cnt):
            nx = x+dx
            ny = y+dy
            slag[nx][ny] = slag[x][y]+1
            x = nx
            y = ny
        cur_dir = (cur_dir+1) % 3
    for i in range(1, n+1):
        for j in range(i):
            answer.append(slag[i][j])
    return answer