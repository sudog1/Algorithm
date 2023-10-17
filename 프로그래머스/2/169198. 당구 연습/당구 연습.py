def solution(m, n, startX, startY, balls):
    answer = []
    x_arr = [-startX, startX, 2*m-startX, startX]
    y_arr = [startY, -startY, startY, 2*n-startY]
    for ball_x, ball_y in balls:
        min_square_dist = (2*n)**2 + (2*m)**2
        for i in range(len(x_arr)):
            cur_x = x_arr[i]
            cur_y = y_arr[i]
            if cur_x == ball_x:
                if startY > ball_y:
                    if cur_y < 0:
                        continue
                else:
                    if cur_y > 0:
                        continue
            elif cur_y == ball_y:
                if startX > ball_x:
                    if cur_x < 0:
                        continue
                else:
                    if cur_x > 0:
                        continue
            cur_dist = (cur_x-ball_x)**2 + (cur_y-ball_y)**2
            min_square_dist = min(min_square_dist, cur_dist)
        answer.append(min_square_dist)
    return answer