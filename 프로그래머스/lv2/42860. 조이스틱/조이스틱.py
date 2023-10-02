def solution(name):
    answer = 0
    operation = list(map(lambda x: min(ord('Z') - ord(x) + 1, ord(x) - ord('A')), name))
    l = []
    flag = False
    for i in range(1, len(operation)):
        if operation[i] == 0:
            if flag:
                continue
            l.append(i-1)
            flag = True
        else:
            flag = False
    r = []
    flag = False
    for i in range(1, len(operation)):
        if operation[-i] == 0:
            if flag:
                continue
            r.append(i-1)
            flag = True
        else:
            flag = False
    r = r[::-1]
    min_move = len(operation)-1
    for i in range(len(l)):
        a, b = sorted([l[i], r[i]])
        min_move = min(min_move, 2*a + b)
    return sum(operation) + min_move