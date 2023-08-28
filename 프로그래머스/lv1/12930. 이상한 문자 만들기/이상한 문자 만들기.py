def conv_str(x):
    return ''.join([x[i].lower() if i%2 else x[i].upper() for i in range(len(x))])

def solution(s):
    return ' '.join(map(conv_str, s.split(' ')))
