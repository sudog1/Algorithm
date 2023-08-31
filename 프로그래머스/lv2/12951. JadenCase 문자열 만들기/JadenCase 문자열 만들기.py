def solution(s):
    temp = list(s)
    state = 0
    for i in range(len(temp)):
        if temp[i] == ' ':
            state = 0
            continue
        if state:
            temp[i] = temp[i].lower()
        else:
            temp[i] = temp[i].upper()
            state = 1
            
    return ''.join(temp)