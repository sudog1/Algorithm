def tenToThreeRvs(n):
    result = []
    while n >= 3:
        n, s = divmod(n, 3)
        result.append(str(s))
    if n > 0:
        result.append(str(n))
    result = ''.join(result)
    return result
    
def solution(n):
    answer = 0
    answer = int(tenToThreeRvs(n), 3)
    return answer