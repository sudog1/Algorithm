from math import inf

def find_node(line1, line2):
    a, b, e = line1
    c, d, f = line2
    deno = a*d - b*c
    if deno == 0:
        return False
    x = (b*f-e*d) / deno
    y = (e*c-a*f) / deno
    if int(x) == x and int(y) == y:
        return (int(x), int(y))
    return False


def solution(line):
    result = set({False})
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            result.add(find_node(line[i], line[j]))
    result.remove(False)
    s_x = inf
    s_y = inf
    e_x = -inf
    e_y = -inf
    for x, y in result:
        s_x = min(s_x, x)
        s_y = min(s_y, y)
        e_x = max(e_x, x)
        e_y = max(e_y, y)
    answer = []
    for y in range(e_y, s_y-1, -1):
        row = []
        for x in range(s_x, e_x+1):
            row.append('*' if (x, y) in result else '.')
        answer.append(''.join(row))
    return answer