import sys


def quad_compress(arr, x_ran, y_ran):
    x1, x2 = x_ran
    y1, y2 = y_ran
    step = (x2-x1) // 2
    if step == 0:
        if arr[x1][y1]:
            return [0, 1]
        else:
            return [1, 0]
    result = []
    for i in range(2):
        for j in range(2):
            result.append(quad_compress(arr,(x1+i*step, x1+(i+1)*step),(y1+j*step, y1+(j+1)*step)))
    cnt_0, cnt_1 = map(sum, zip(*result))
    if cnt_0 == 0:
        return [0, 1]
    elif cnt_1 == 0:
        return [1, 0]
    else:
        return [cnt_0, cnt_1]
    
    
def solution(arr):
    return quad_compress(arr, (0, len(arr)), (0, len(arr)))