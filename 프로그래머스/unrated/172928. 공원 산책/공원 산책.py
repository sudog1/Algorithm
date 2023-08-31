def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                cur_pos = [i, j]
    d = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    for route in routes:
        a, b = route.split()
        x, y = cur_pos
        dx, dy = d[a]
        for _ in range(int(b)):
            if not ( 0 <= x+dx < len(park) and 0 <= y+dy < len(park[0]) ):
                break
            if park[x+dx][y+dy] == 'X':
                break
            x += dx
            y += dy
        else:
            cur_pos = [x, y]
    return cur_pos