from functools import reduce


def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    S_i = []
    for i in range(row_begin-1, row_end):
        S_i.append(reduce(lambda acc, x: acc+x%(i+1), sorted_data[i], 0))
    return reduce(lambda acc, x: acc ^ x, S_i[1:], S_i[0])