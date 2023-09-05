def solution(x, y, n):
    result = {x: 0}
    count = 0
    while y not in result:
        flag = 1
        for num, cnt in filter(lambda x: x[1] == count, list(result.items())):
            calc_result = [num+n, 2*num, 3*num]
            for calc in calc_result:
                if calc < y:
                    flag = 0
                if calc in result:
                    result[calc] = min(result[calc], cnt+1)
                else:
                    result[calc] = cnt+1
        count += 1
        if flag:
            break
    return result[y] if y in result else -1