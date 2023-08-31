def solution(s):
    temp = s.split()
    temp = list(map(lambda x: int(x), temp))
    return f'{min(temp)} {max(temp)}'