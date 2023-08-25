def solution(s):
    if len(s) % 2:
        l = len(s)//2
        r = l+1
    else:
        l = len(s)//2 - 1
        r = l+2
    return s[l:r]