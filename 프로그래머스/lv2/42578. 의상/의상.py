from functools import reduce

def solution(clothes):
    cloth_dict = {}
    for _, part in clothes:
        if part in cloth_dict:
            cloth_dict[part] += 1
        else:
            cloth_dict[part] = 2
    return reduce(lambda acc, x: acc*x, cloth_dict.values(), 1) - 1