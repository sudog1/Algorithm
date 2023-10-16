def solution(n, l, r):
    l -= 1
    r -= 1
    l_rem = []
    r_rem = []
    for _ in range(n-1):
        l_rem.append(l % 5)
        r_rem.append(r % 5)
        l //= 5
        r //= 5
    l_rem.reverse()
    r_rem.reverse()
    arr = [1, 1, 0, 1, 1]
    l_val = arr[l]
    r_val = arr[r]
    count = sum(arr[l:r+1])
    for i in range(n-1):
        l = l*5 + l_rem[i]
        r = r*5 + r_rem[i]
        count *= 4
        if l_val:
            count -= sum(arr[:l_rem[i]])
            l_val = arr[l_rem[i]]
        if r_val:
            count -= sum(arr[r_rem[i]+1:])
            r_val = arr[r_rem[i]]
    return count