def solution(s):
    word_to_num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    result = 0
    temp = []
    for i in range(len(s)):
        if len(temp) >= 3:
            word = ''.join(temp)
            if word in word_to_num:
                result = result*10 + word_to_num[word]
                temp = []
        if s[i].isnumeric():
            result = result*10 + int(s[i])
        else:
            temp.append(s[i])
    if temp:
        word = ''.join(temp)
        if word in word_to_num:
            result = result*10 + word_to_num[word]
        
    return result