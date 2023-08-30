def solution(survey, choices):
    pers_type = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    type_score = {
        'R': 0,
        'C': 0,
        'J': 0,
        'A': 0,
    }
    for i, s in enumerate(survey):
        if s[0] in type_score:
            type_score[s[0]] += 4-choices[i]
        else:
            type_score[s[1]] -= 4-choices[i]
            
    result = []
    for i in range(0, len(pers_type), 2):
        if type_score[pers_type[i]] >= 0:
            result.append(pers_type[i])
        else:
            result.append(pers_type[i+1])
            
    return ''.join(result)