from functools import cmp_to_key

def comp(a, b):
    i = 0
    j = 0
    count = 0
    while count < 4:
        if a[i] == b[j]:
            i = (i+1) % len(a)
            j = (j+1) % len(b)
            count += 1
        elif a[i] < b[j]:
            return -1
        else:
            return 1
    return -1

def solution(numbers):
    if max(numbers) == 0:
        return '0'
    return ''.join(sorted(map(str, numbers), key=cmp_to_key(comp), reverse=True))