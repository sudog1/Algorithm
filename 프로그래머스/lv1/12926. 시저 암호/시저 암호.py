def solution(s, n):
    a = ord('a')
    A = ord('A')
    cnt = ord('z') - a + 1
    res = []
    for c in s:
        if c == ' ':
            res.append(c)
        elif c.islower():
            res.append(chr(((ord(c)-a+n) % cnt)+a))
        else:
            res.append(chr(((ord(c)-A+n) % cnt)+A))
    return ''.join(res)