def solution(keymap, targets):
    char_dict = {}
    for key in keymap:
        for i, c in enumerate(key):
            if c in char_dict:
                char_dict[c] = min(char_dict[c], i+1)
            else:
                char_dict[c] = i+1
                
    answer = []          
    for target in targets:
        count = 0
        for c in target:
            if c in char_dict:
                count += char_dict[c]
            else:
                count = -1
                break
        answer.append(count)
        
    return answer