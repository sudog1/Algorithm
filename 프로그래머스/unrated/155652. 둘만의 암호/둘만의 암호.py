def solution(s, skip, index):
    skip_idx = [0]*(26)
    result = []
    for c in skip:
        skip_idx[ord(c)-ord('a')] = 1
    for c in s:
        i = ord(c)-ord('a')
        temp = index
        while temp:
            i += 1
            i %= 26
            if not skip_idx[i]:
                temp -= 1
        result.append(chr(i+ord('a')))
            
    return ''.join(result)