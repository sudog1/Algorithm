def solution(n):
    s = ['수', '박']
    return ''.join([s[i%2] for i in range(n)])