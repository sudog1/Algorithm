def solution(answers):
    arr = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    count = [0]*len(arr)
    for i, answer in enumerate(answers):
        for j in range(len(arr)):
            if answer == arr[j][i % len(arr[j])]:
                count[j] += 1
    max_score = max(count)
    result = [i+1 for i in range(len(arr)) if count[i] == max_score]
    return result