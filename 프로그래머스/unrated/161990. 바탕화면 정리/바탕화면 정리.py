def solution(wallpaper):
    cur_row = -1
    min_col = 50
    max_col = -1
    answer = []
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[r])):
            if wallpaper[r][c] == '#':
                if cur_row == -1:
                    answer.append(r)
                cur_row = r
                min_col = min(min_col, c)
                max_col = max(max_col, c)
    answer.append(min_col)
    answer.append(cur_row+1)
    answer.append(max_col+1)
    return answer