def solution(arr):
    min_num = min(arr)
    answer = [i for i in arr if i != min_num]
    return answer if answer else [-1]