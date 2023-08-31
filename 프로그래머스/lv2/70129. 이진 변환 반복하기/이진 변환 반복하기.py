def solution(s):
    count_zero = 0
    count_convert = 0
    while s != '1':
        count_convert += 1
        count_zero += len(s)
        s = ''.join((filter(lambda x: x == '1', s)))
        count_zero -= len(s)
        s = bin(len(s))[2:]
    
    return [count_convert, count_zero]